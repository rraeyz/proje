"""Radyal hiz (RV) egilimi -> Romer etkisinin ongordugu donem degisimi.
Kullanim:
  python rv_analiz.py knutson HAT-P-7 2.204737 2454954.358572 18.28 4.05
  python rv_analiz.py bouma   WASP-4  1.338231 2455804.515679 -6.43 0.56
  python rv_analiz.py dosya.csv  AD   P  T0  dPdt  hata      (csv: BJD,RV,hata,alet)
Son iki sayi: O-C'den buldugun dP/dt ve hatasi (ms/yil).
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from oc_diyagrami import vizier

C_ISIK = 2.998e8                       # m/s
YIL_S = 365.25 * 86400.0


def rv_oku(kaynak, yildiz):
    """(t [BJD], v [m/s], hata [m/s], alet) dizileri."""
    if kaynak == "knutson":                                     # Keck/HIRES, Knutson vd. 2014
        r = vizier("J/ApJ/785/126/table3", Name=yildiz)
        t = [float(x["BJD"]) for x in r]; v = [float(x["RV"]) for x in r]
        s = [float(x["e_RV"]) for x in r]; a = ["HIRES"] * len(r)
    elif kaynak == "bouma":                                     # WASP-4: CORALIE + HARPS + HIRES, Bouma vd. 2020
        r = vizier("J/ApJ/893/L29/table2")
        t = [float(x["BJD"]) + 2450000 for x in r]; v = [float(x["RV"]) for x in r]
        s = [float(x["e_RV"]) for x in r]; a = [x["Tel"] for x in r]
    else:                                                       # kendi derledigin CSV
        d = np.genfromtxt(kaynak, delimiter=",", dtype=None, encoding=None, names=True)
        t, v, s, a = d[d.dtype.names[0]], d[d.dtype.names[1]], d[d.dtype.names[2]], d[d.dtype.names[3]]
    return np.array(t, float), np.array(v, float), np.array(s, float), np.array(a, str)


def rv_uydur(t, v, s, alet, P, T0, egrilik=False):
    """v = gamma_alet + gdot*(t-tref) [+ gddot*(t-tref)^2] + A*sin(faz) + B*cos(faz)  (dairesel yorunge).
    Her alet kendi sifir noktasini (gamma) alir: farkli spektrograflarin RV'leri dogrudan karsilastirilamaz."""
    tref = np.mean(t)
    faz = 2 * np.pi * (t - T0) / P
    aletler = sorted(set(alet))
    kol = [(alet == x).astype(float) for x in aletler]          # alet basina bir gamma
    kol += [(t - tref) / 365.25, np.sin(faz), np.cos(faz)]
    if egrilik:
        kol.append(((t - tref) / 365.25) ** 2)
    X = np.column_stack(kol)
    A, b = X / s[:, None], v / s
    p, *_ = np.linalg.lstsq(A, b, rcond=None)
    kov = np.linalg.inv(A.T @ A)
    chi2 = float(np.sum((b - A @ p) ** 2))
    olcek = np.sqrt(max(chi2 / (len(t) - len(p)), 1.0))      # hatalar kucukse olcekle (yildiz titresimi/jitter)
    return p, np.sqrt(np.diag(kov)) * olcek, X, tref, len(aletler)


def romer_pdot(P, gdot):
    """dP/dt (ms/yil) = P * (dv/dt) / c ;  gdot m/s/yil."""
    return P * 86400 * (gdot / YIL_S) / C_ISIK * YIL_S * 1e3


if __name__ == "__main__":
    kaynak, yildiz = sys.argv[1], sys.argv[2]
    P, T0, pdot_g, pdot_gh = map(float, sys.argv[3:7])
    t, v, s, alet = rv_oku(kaynak, yildiz)
    p, h, X, tref, na = rv_uydur(t, v, s, alet, P, T0)
    gdot, gdot_h = p[na], h[na]                               # m/s/yil
    pr, prh = romer_pdot(P, gdot), romer_pdot(P, gdot_h)
    fark = (pdot_g - pr) / np.hypot(pdot_gh, prh)
    print(f"{yildiz}: {len(t)} RV ({', '.join(sorted(set(alet)))}), {(t.max()-t.min())/365.25:.1f} yil; "
          f"K = {np.hypot(p[na+1], p[na+2]):.1f} m/s")
    print(f"  RV egilimi  dv/dt = {gdot:.2f} +- {gdot_h:.2f} m/s/yil")
    print(f"  Romer'in ongordugu dP/dt = {pr:.2f} +- {prh:.2f} ms/yil;  O-C'den gozlenen {pdot_g} +- {pdot_gh}")
    print(f"  fark = {fark:.1f} sigma ->", "Romer TEK BASINA ACIKLAYABILIR" if abs(fark) < 2 else "Romer TEK BASINA ACIKLAYAMAZ")
    artik = v - X[:, :na] @ p[:na] - X[:, na+1:na+3] @ p[na+1:na+3]   # alet sifirlari ve gezegen sinyali cikarilmis
    fig, ax = plt.subplots(figsize=(7, 3.5))
    for x in sorted(set(alet)):
        m = alet == x
        ax.errorbar(t[m] - 2450000, artik[m], s[m], fmt="o", ms=3, label=x)
    tt = np.linspace(t.min(), t.max(), 100)
    ax.plot(tt - 2450000, gdot * (tt - tref) / 365.25, "r-", label=f"eğilim: {gdot:.1f} ± {gdot_h:.1f} m/s/yıl")
    ax.set_xlabel("BJD − 2450000"); ax.set_ylabel("RV − gezegen − sıfır nok. (m/s)"); ax.set_title(yildiz)
    ax.legend(fontsize=8); fig.tight_layout(); fig.savefig(f"RV_{yildiz}.png", dpi=200)
