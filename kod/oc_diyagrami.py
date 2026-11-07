"""O-C diyagrami: Ivshina & Winn (2022) + Wang vd. (2024) gecis zamanlari.
Kullanim:  python oc_diyagrami.py "WASP-12 b" WASP-012 [tess_WASP-12.csv ...]
"""
import sys, io, urllib.parse, urllib.request
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

VIZIER = "https://vizier.cfa.harvard.edu/viz-bin/asu-tsv"   # Harvard aynasi; olmazsa vizier.cds.unistra.fr
YIL_S = 365.25 * 86400.0                                    # bir yil, saniye
EK_DOSYALAR = []
BELIRSIZ_BJD_DAHIL = True                                   # False yapip sonucun degisip degismedigine bak


def vizier(tablo, **filtre):
    """VizieR tablosunu indir; satir listesi (sozluk) dondur."""
    p = {"-source": tablo, "-out.max": "99999", "-out.all": ""}
    p.update(filtre)
    url = VIZIER + "?" + urllib.parse.urlencode(p)
    metin = urllib.request.urlopen(url, timeout=120).read().decode()
    satir = [s for s in metin.splitlines() if s and not s.startswith("#")]
    if not satir:                                               # eslesen kayit yok
        return []
    bas = [h.strip() for h in satir[0].split("\t")]
    return [dict(zip(bas, [x.strip() for x in s.split("\t")])) for s in satir[3:]]


def zamanlari_topla(gezegen, iw_adi):
    """O: gozlenen orta gecis zamanlari (BJD_TDB), hatalari ve kaynak etiketi."""
    t, s, k = [], [], []
    for r in vizier("J/ApJS/259/62/table4", Sys=iw_adi):        # literatur + I&W'nin TESS zamanlari
        sistem = r["n_TTmid"]
        if sistem not in ("BJD_TDB", "BJD_TT"):                  # TT ile TDB farki < 2 ms: ihmal edilir
            if sistem == "BJD" and BELIRSIZ_BJD_DAHIL:             # "BJD" = UTC mi TDB mi belli degil
                print("UYARI: zaman sistemi belirsiz (BJD), makaleden kontrol et:", r["TTmid"], r["Ref"])
            else:
                print("ATLANDI: zaman sistemi", sistem, r["TTmid"], r["Ref"])
                continue
        t.append(float(r["TTmid"])); s.append(float(r["e_TTmid"]))
        k.append("TESS" if r["Ref"] == "This work" else "Literatur")
    for r in vizier("J/ApJS/270/14/table1", Name=gezegen):      # Wang vd. TESS zamanlari
        tc = float(r["Tc"])
        if np.min(np.abs(np.array(t) - tc)) < 0.01:              # ayni gecis zaten var: tekrar sayma
            continue
        t.append(tc); s.append(float(r["e_Tc"])); k.append("TESS")
    for dosya in EK_DOSYALAR:                                     # kendi olctugun TESS zamanlari
        for _, tc, h in np.atleast_2d(np.loadtxt(dosya, delimiter=",")):
            if np.min(np.abs(np.array(t) - tc)) < 0.01:
                continue
            t.append(tc); s.append(h); k.append("TESS (bu proje)")
    i = np.argsort(t)
    return np.array(t)[i], np.array(s)[i], np.array(k)[i]


def uydur(E, t, s, derece):
    """Agirlikli en kucuk kareler. derece=1 dogrusal, 2 kuadratik. (katsayilar, kovaryans, chi2)."""
    X = np.vander(E, derece + 1, increasing=True)              # [1, E, E^2]
    A, b = X / s[:, None], t / s
    p, *_ = np.linalg.lstsq(A, b, rcond=None)
    kov = np.linalg.inv(A.T @ A)
    chi2 = float(np.sum((b - A @ p) ** 2))
    return p, kov, chi2


def analiz(E, t, s):
    """Dogrusal vs kuadratik: dP/dt (ms/yil), hatasi, Delta BIC."""
    n = len(t)
    p1, _, c1 = uydur(E, t, s, 1)
    p2, k2, c2 = uydur(E, t, s, 2)
    P = p2[1]
    pdot = 2 * p2[2] / P * YIL_S * 1e3                          # dP/dt = (1/P) dP/dN, dP/dN = 2c
    pdot_h = 2 * np.sqrt(k2[2, 2]) / P * YIL_S * 1e3
    dbic = (c1 + 2 * np.log(n)) - (c2 + 3 * np.log(n))
    return dict(p1=p1, p2=p2, pdot=pdot, pdot_h=pdot_h, dbic=dbic, chi2_1=c1, chi2_2=c2, n=n)


def sigma_kirp(E, t, s, n_sigma=5):
    """Wang vd. gibi: kuadratik artiklarda n-sigma disindakileri yinelemeli at."""
    tut = np.ones(len(t), bool)
    while True:
        p, _, _ = uydur(E[tut], t[tut], s[tut], 2)
        r = t - np.polyval(p[::-1], E)
        m, sd = r[tut].mean(), r[tut].std()
        yeni = np.abs(r - m) < n_sigma * sd
        if (yeni == tut).all():
            return tut
        tut = yeni


def hata_olcekle(E, t, s, k, tur=5):
    """Hata cubuklarini veri grubu (literatur / TESS) basina, kuadratik model artiklarinin
    indirgenmis ki-karesi 1 olacak sekilde buyutur (hicbir zaman kucultmez)."""
    s = s.copy()
    gruplar = [k == "Literatur", k != "Literatur"]
    for _ in range(tur):
        p, _, _ = uydur(E, t, s, 2)
        r = (t - np.polyval(p[::-1], E)) / s
        for g in gruplar:
            if g.sum() > 3:
                s[g] *= np.sqrt(max(np.sum(r[g] ** 2) / (g.sum() - 1), 1.0))
    return s


def loocv(E, t, s):
    """Her noktayi tek tek cikar, yeniden uydur; 3-sigma ve DBIC>10 kosulu hep saglaniyor mu?"""
    sonuc = []
    for i in range(len(t)):
        m = np.arange(len(t)) != i
        a = analiz(E[m], t[m], s[m])
        sonuc.append(abs(a["pdot"]) / a["pdot_h"] >= 3 and a["dbic"] > 10)
    return np.array(sonuc)


if __name__ == "__main__":
    gezegen, iw_adi, EK_DOSYALAR = sys.argv[1], sys.argv[2], sys.argv[3:]
    t, s, k = zamanlari_topla(gezegen, iw_adi)
    # C icin baslangic efemerisi: Wang Tablo 2 (yoksa NASA Exoplanet Archive'dan T0, P)
    ef = [r for r in vizier("J/ApJS/270/14/table2", Name=gezegen)][0]
    T0, P = float(ef["T0"]), float(ef["P0"])
    E = np.round((t - T0) / P)
    E = E - np.round(np.median(E))                              # epoklari ortala: sayisal kararlilik
    tut = sigma_kirp(E, t, s, 5)
    E, t, s, k = E[tut], t[tut], s[tut], k[tut]
    s = hata_olcekle(E, t, s, k)                               # gercekci hata cubuklari
    a = analiz(E, t, s)
    gecti = loocv(E, t, s)
    print(f"{gezegen}: n={a['n']} (TESS {np.sum(k!='Literatur')}), dP/dt = {a['pdot']:.2f} +- {a['pdot_h']:.2f} ms/yil, "
          f"DBIC = {a['dbic']:.1f}, LOOCV: {np.sum(~gecti)} noktada kosul bozuluyor -> {'GECTI' if gecti.all() else 'KALDI'}")

    # O-C: dogrusal efemerise gore (C = T0 + P*E)
    C = a["p1"][0] + a["p1"][1] * E
    oc_dk = (t - C) * 1440
    ee = np.linspace(E.min(), E.max(), 400)
    kuad = (np.polyval(a["p2"][::-1], ee) - (a["p1"][0] + a["p1"][1] * ee)) * 1440
    fig, ax = plt.subplots(figsize=(7, 4))
    for etiket, renk in [("Literatur", "tab:orange"), ("TESS", "tab:green"), ("TESS (bu proje)", "tab:red")]:
        m = k == etiket
        if not m.any():
            continue
        ax.errorbar(E[m], oc_dk[m], s[m] * 1440, fmt="o", ms=3, color=renk, label=etiket, alpha=.8)
    ax.plot(ee, kuad, "b-", label=f"kuadratik: dP/dt = {a['pdot']:.1f} ± {a['pdot_h']:.1f} ms/yıl")
    ax.axhline(0, color="k", lw=.8, ls="--", label="doğrusal (sabit dönem)")
    ax.set_xlabel("Epok (E)"); ax.set_ylabel("O − C (dakika)")
    ax.set_title(f"{gezegen}  (ΔBIC = {a['dbic']:.1f}, n = {a['n']})")
    ax.legend(fontsize=8); fig.tight_layout()
    ad = gezegen.replace(" ", "")
    fig.savefig(f"OC_{ad}.png", dpi=200)
    np.savetxt(f"zamanlar_{ad}.csv", np.column_stack([E, t, s, oc_dk]), delimiter=",",
               header="E,T_gozlenen_BJD_TDB,hata_gun,OC_dakika", fmt=["%d", "%.6f", "%.6f", "%.3f"])
