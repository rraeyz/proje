"""Donem degisiminin fiziksel kokeni icin basit testler (RV gerektirmeyenler).
Kullanim:  python fizik_testleri.py "WASP-12 b" WASP-012 [tess_WASP-12.csv]
Gerekli: oc_diyagrami.py ayni klasorde; parametreler NASA Exoplanet Archive'dan cekilir.
"""
import sys, urllib.parse, urllib.request, csv, io
import numpy as np
from astropy.timeseries import LombScargle
import oc_diyagrami as oc

MJ, MS, RJ, RS, AU = 1.898e27, 1.989e30, 7.1492e7, 6.957e8, 1.496e11
YIL_S = 365.25 * 86400.0


def parametreler(gezegen):
    """NASA Exoplanet Archive pscomppars: kutle, yaricap, a, e, yildiz kutlesi/yaricapi."""
    q = ("select pl_name,pl_orbper,pl_bmassj,pl_radj,pl_orbsmax,pl_orbeccen,pl_orbeccenerr1,st_mass,st_rad,st_teff "
         f"from pscomppars where pl_name='{gezegen}'")
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?" + urllib.parse.urlencode({"query": q, "format": "csv"})
    r = list(csv.DictReader(io.StringIO(urllib.request.urlopen(url, timeout=60).read().decode())))[0]
    return {k: (float(v) if v not in ("", None) and k != "pl_name" else v) for k, v in r.items()}


def gerekli_Q(p, pdot_msyil):
    """Gelgit: dP/dt = -(27 pi / 2Q') (Mp/M*) (R*/a)^5  ->  bu dP/dt icin gereken Q'."""
    if pdot_msyil >= 0:
        return np.nan                                          # gelgit (yavas donen yildiz) donemi uzatamaz
    q = p["pl_bmassj"] * MJ / (p["st_mass"] * MS)
    x = p["st_rad"] * RS / (p["pl_orbsmax"] * AU)
    return -(27 * np.pi / 2) * q * x**5 / (pdot_msyil * 1e-3 / YIL_S)


def roche_orani(p):
    """a / a_Roche ;  a_Roche ~ 2.16 Rp (M*/Mp)^(1/3).  ~1 ise kutle kaybi onemli, >2 ise ihmal edilebilir."""
    aR = 2.16 * p["pl_radj"] * RJ * (p["st_mass"] * MS / (p["pl_bmassj"] * MJ)) ** (1 / 3)
    return p["pl_orbsmax"] * AU / aR


def apsis_genligi_s(p, e):
    """Apsis hareketinin O-C'de yaratabilecegi en buyuk genlik ~ e*P/pi (saniye)."""
    return e * p["pl_orbper"] * 86400 / np.pi


if __name__ == "__main__":
    gezegen, iw_adi = sys.argv[1], sys.argv[2]
    oc.EK_DOSYALAR = sys.argv[3:]
    t, s, k = oc.zamanlari_topla(gezegen, iw_adi)
    ef = oc.vizier("J/ApJS/270/14/table2", Name=gezegen)[0]
    E = np.round((t - float(ef["T0"])) / float(ef["P0"])); E -= np.round(np.median(E))
    tut = oc.sigma_kirp(E, t, s, 5); E, t, s, k = E[tut], t[tut], s[tut], k[tut]
    s = oc.hata_olcekle(E, t, s, k)
    a = oc.analiz(E, t, s)
    p = parametreler(gezegen)
    print(f"== {gezegen}:  dP/dt = {a['pdot']:.2f} +- {a['pdot_h']:.2f} ms/yil (n={a['n']})")

    # 1) Gelgit: gereken Q'
    Q = gerekli_Q(p, a["pdot"])
    print(f"  [Gelgit]    gereken Q'* = {Q:.2e}  (kuramsal beklenti ~1e5-1e7; <1e4 ise gelgit fiziksel olarak zor)"
          if np.isfinite(Q) else "  [Gelgit]    donem UZUYOR: yavas donen yildizda gelgit bunu yapamaz")

    # 2) Kutle kaybi: Roche
    print(f"  [Kutle k.]  a/a_Roche = {roche_orani(p):.2f}  (~1: onemli olabilir; >2: ihmal edilebilir)")

    # 3) Apsis: dismerkezlik ust siniri ile en buyuk genlik
    e_ust = (p["pl_orbeccen"] or 0) + 2 * (p["pl_orbeccenerr1"] or 0.01)   # e bilinmiyorsa 0.02 varsay
    if e_ust == 0:
        e_ust = 0.02
    print(f"  [Apsis]     e <~ {e_ust:.3f} icin en buyuk O-C genligi ~ {apsis_genligi_s(p, e_ust):.0f} s; "
          f"gozlenen parabolun tepe-cukur genligi ~ {np.ptp(np.polyval(a['p2'][::-1], E) - (a['p1'][0] + a['p1'][1]*E))*86400:.0f} s")

    # 4) Egrilik sabit mi? kubik model (sabit dP/dt'den sapma) - Romer/LTTE ve apsis icin ipucu
    p3, _, c3 = oc.uydur(E, t, s, 3)
    bic2 = a["chi2_2"] + 3 * np.log(a["n"]); bic3 = c3 + 4 * np.log(a["n"])
    print(f"  [Egrilik]   DBIC(kuadratik - kubik) = {bic2 - bic3:.1f}  (>10: dP/dt zamanla degisiyor -> LTTE/apsis/Applegate lehine)")

    # 5) Periyodiklik: kuadratik artiklarinda Lomb-Scargle
    art = t - np.polyval(a["p2"][::-1], E)
    zaman_yil = (t - t.min()) / 365.25
    ls = LombScargle(zaman_yil, art, s)
    f, g = ls.autopower(minimum_frequency=1 / (2 * np.ptp(zaman_yil)), maximum_frequency=2.0, samples_per_peak=20)
    i = int(np.argmax(g))
    print(f"  [Periyot]   en guclu tepe: {1/f[i]:.1f} yil, yanlis alarm olasiligi = {ls.false_alarm_probability(g[i]):.3f}"
          "  (<0.01 ise periyodik sinyal var: Applegate / 3. cisim / apsis aday)")
