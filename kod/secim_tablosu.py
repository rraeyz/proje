"""Tablo 1 (hedef secimi) - tum sutunlar herkese acik kaynaklardan hesaplanir.
Kullanim:  python secim_tablosu.py        (DACE icin: pip install dace-query)
K1: Wang vd. (2024) Tablo 3, LOOCV sutunu "pass" olan 14 aday (makalenin kendisinden; VizieR'de bu sutun yok).
K2: Wang vd. TESS gecis zamani sayisi >= 30   (VizieR J/ApJS/270/14/table1'de satir sayilir)
K3: arsiv RV'sinden Romer ongorusunun belirsizligi < Wang vd. |dP/dt| / 3   (K2'yi gecenler icin)
"""
import csv, io, urllib.parse, urllib.request, collections
import numpy as np
from oc_diyagrami import vizier
from rv_analiz import rv_uydur, romer_pdot

K1 = ["CoRoT-2 b", "HAT-P-37 b", "KELT-16 b", "TrES-1 b", "TrES-5 b", "WASP-4 b", "WASP-10 b", "WASP-12 b",
      "WASP-22 b", "WASP-45 b", "XO-4 b", "HAT-P-7 b", "WASP-1 b", "WASP-46 b"]


def nasa(gezegen):
    q = f"select pl_orbper,pl_tranmid from pscomppars where pl_name='{gezegen}'"
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?" + urllib.parse.urlencode({"query": q, "format": "csv"})
    r = list(csv.DictReader(io.StringIO(urllib.request.urlopen(url, timeout=60).read().decode())))[0]
    return float(r["pl_orbper"]), float(r["pl_tranmid"])


def rv_setleri(yildiz, P, T0):
    """Her arsivden (t, v, s, alet) dondurur. Gecis sirasindaki RV'ler ve <3 olcumlu aletler atilir."""
    setler = {}
    r = vizier("J/ApJ/785/126/table3", Name=yildiz)                                  # Knutson vd. 2014
    if r:
        setler["Knutson 2014"] = ([float(x["BJD"]) for x in r], [float(x["RV"]) for x in r],
                                  [float(x["e_RV"]) for x in r], ["HIRES"] * len(r))
    if yildiz == "WASP-4":                                                           # Bouma vd. 2020
        r = vizier("J/ApJ/893/L29/table2")
        setler["Bouma 2020"] = ([float(x["BJD"]) + 2450000 for x in r], [float(x["RV"]) for x in r],
                                [float(x["e_RV"]) for x in r], [x["Tel"] for x in r])
    r = [x for x in vizier("J/A+A/602/A107/table1") if x["Star"].strip() == yildiz]  # Bonomo vd. 2017 (km/s)
    if r:
        setler["Bonomo 2017"] = ([float(x["BJD"]) + 2450000 for x in r], [float(x["RV"]) * 1e3 for x in r],
                                 [float(x["e_RV"]) * 1e3 for x in r], ["HARPS-N"] * len(r))
    try:                                                                             # DACE
        from dace_query.spectroscopy import Spectroscopy
        d = Spectroscopy.get_timeseries(yildiz, sorted_by_instrument=False, output_format="dict")
        if d and "rjd" in d:
            setler["DACE"] = (list(np.array(d["rjd"], float) + 2400000), list(d["rv"]), list(d["rv_err"]),
                              [str(x) for x in d["instrument_name"]])
    except Exception as e:
        print("  DACE okunamadi:", yildiz, type(e).__name__)
    temiz = {}
    for ad, (t, v, s, a) in setler.items():
        t, v, s, a = np.array(t, float), np.array(v, float), np.array(s, float), np.array(a, str)
        faz = ((t - T0) / P + 0.5) % 1 - 0.5
        m = np.isfinite(v) & np.isfinite(s) & (s > 0) & (np.abs(faz) > 0.04)
        u, n = np.unique(a[m], return_counts=True); m &= np.isin(a, u[n >= 3])
        if m.sum() >= 6:
            temiz[ad] = (t[m], v[m], s[m], a[m])
    return temiz


if __name__ == "__main__":
    tess = collections.Counter(r["Name"].strip() for r in vizier("J/ApJS/270/14/table1"))
    t2 = {r["Name"].strip(): r for r in vizier("J/ApJS/270/14/table2") if r["sigma"].strip() == "5"}
    satirlar = []
    for g in K1:
        pd, pe = abs(float(t2[g]["dP/dt"])), float(t2[g]["e_dP/dt"])
        n = tess[g]; sr, kaynak, sonuc = None, "", ""
        if n < 30:
            sonuc = "K2 saglanmiyor"
        else:
            P, T0 = nasa(g)
            enk = {}
            for ad, (t, v, s, a) in rv_setleri(g[:-2], P, T0).items():
                p, h, _, _, na = rv_uydur(t, v, s, a, P, T0)
                enk[ad] = abs(romer_pdot(P, h[na]))
            if enk:
                kaynak = min(enk, key=enk.get); sr = enk[kaynak]
            sonuc = "SECILDI" if (sr is not None and sr < pd / 3) else "K3 saglanmiyor"
        satirlar.append((g, pd / pe, n, sr, kaynak, pd / 3, sonuc))
        print(f"{g:11s} |dP/dt|/sigma={pd/pe:5.1f}  TESS={n:3d}  sigma_Romer={'-' if sr is None else f'{sr:.1f}':>5} {kaynak:12s}"
              f" |dP/dt|/3={pd/3:5.1f}  -> {sonuc}")
    with open("tablo1_secim.csv", "w") as f:
        f.write("aday,dPdt_anlamlilik,TESS_sayisi,sigma_Romer_msyil,RV_kaynagi,Wang_dPdt_bolu_3,sonuc\n")
        for g, sn, n, sr, k, e, s in satirlar:
            f.write(f"{g},{sn:.1f},{n},{'' if sr is None else f'{sr:.2f}'},{k},{e:.1f},{s}\n")
