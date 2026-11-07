"""TESS isik egrisinden orta gecis zamanlari (O) olcer.
Kullanim:  python tess_zaman.py WASP-12 97.6366450 29.6722662 1.09141890 2457607.51930 71 72
           (hedef, RA, Dec, P [gun], T0 [BJD_TDB], sektor listesi)
"""
import sys
import numpy as np
import batman, emcee
from scipy.optimize import least_squares
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations

BTJD0 = 2457000.0                         # TESS zamani: BTJD = BJD_TDB - 2457000


def indir(ra, dec, sektorler):
    """MAST'tan SPOC 120 s isik egrisi (*_lc.fits) dosyalarini indirir."""
    obs = Observations.query_criteria(coordinates=SkyCoord(ra, dec, unit="deg"), radius="0.003 deg",
                                      obs_collection="TESS", dataproduct_type="timeseries",
                                      provenance_name="SPOC")
    obs = obs[np.isin(obs["sequence_number"], sektorler)]
    urun = Observations.get_product_list(obs)
    urun = urun[[str(f).endswith("_lc.fits") for f in urun["productFilename"]]]
    liste = Observations.download_products(urun, download_dir="veri_ham")
    return sorted(str(p) for p in liste["Local Path"])        # yalnizca BU hedefin dosyalari


def oku(dosya):
    """TIME (BTJD), PDCSAP_FLUX; kalite bayragi 0 olmayan ve NaN noktalari atar, 1'e normalize eder."""
    d = fits.getdata(dosya, 1)
    m = (d["QUALITY"] == 0) & np.isfinite(d["TIME"]) & np.isfinite(d["PDCSAP_FLUX"])
    t, f, e = d["TIME"][m], d["PDCSAP_FLUX"][m], d["PDCSAP_FLUX_ERR"][m]
    return t + BTJD0, f / np.nanmedian(f), e / np.nanmedian(f)


def model(t, tc, P, rp, a, inc, u1=0.4, u2=0.2):
    p = batman.TransitParams()
    p.t0, p.per, p.rp, p.a, p.inc, p.ecc, p.w = tc, P, rp, a, inc, 0.0, 90.0
    p.u, p.limb_dark = [u1, u2], "quadratic"
    return batman.TransitModel(p, t).light_curve(p)


def efemeris_merkezle(t, f, T0, P):
    """Eski bir T0 TESS'e kadar dakikalarca kaymis olabilir: katlanmis isik egrisinde
    en derin noktayi kutu taramasiyla bul ve T0'i oraya tasi (BLS benzeri basit tarama)."""
    n_ort = np.round((np.median(t) - T0) / P)
    T0 = T0 + n_ort * P                                       # T0'i TESS verisinin ortasina tasi
    kaymalar = np.arange(-0.15, 0.15, 0.001)
    derinlik = []
    for dt in kaymalar:
        x = ((t - T0 - dt) / P + 0.5) % 1 - 0.5
        derinlik.append(np.mean(f[np.abs(x * P) < 0.03]))     # +-43 dk kutu
    return T0 + kaymalar[int(np.argmin(derinlik))]


def sekil_uydur(t, f, e, T0, P):
    """Tum gecisleri katlayip (phase-fold) gecis seklini (rp, a, inc) bir kez belirler."""
    faz = ((t - T0) / P + 0.5) % 1 - 0.5                     # -0.5..0.5, gecis 0'da
    m = np.abs(faz) < 0.1
    x = faz[m] * P
    r = least_squares(lambda q: (f[m] - q[3] * model(x, 0.0, P, *q[:3])) / e[m],
                      [0.1, 4.0, 85.0, 1.0], bounds=([0.01, 1.5, 70, 0.9], [0.3, 20, 90, 1.1]))
    return r.x[:3]


def tek_gecis(t, f, e, tc0, P, sekil, mcmc=True):
    """Bir gecis: serbest parametreler tc + dogrusal taban (c0, c1). Sonuc: tc, hata (gun)."""
    def m(q):
        return model(t, q[0], P, *sekil) * (q[1] + q[2] * (t - tc0))
    ls = least_squares(lambda q: (f - m(q)) / e, [tc0, 1.0, 0.0])
    if not mcmc:
        J = ls.jac; kov = np.linalg.inv(J.T @ J)
        return ls.x[0], np.sqrt(kov[0, 0]), f - m(ls.x)
    def lnp(q):
        if abs(q[0] - tc0) > 0.05:
            return -np.inf
        return -0.5 * np.sum(((f - m(q)) / e) ** 2)
    np.random.seed(42)                                        # sabit tohum: her calistirmada ayni sonuc (yeniden uretilebilirlik)
    sm = emcee.EnsembleSampler(12, 3, lnp)
    sm.run_mcmc(ls.x + 1e-5 * np.random.randn(12, 3), 2000, progress=False)
    z = sm.get_chain(discard=500, flat=True)[:, 0]
    q16, q50, q84 = np.percentile(z, [16, 50, 84])
    return q50, 0.5 * (q84 - q16), f - m(ls.x)


if __name__ == "__main__":
    hedef, ra, dec, P, T0 = sys.argv[1], *map(float, sys.argv[2:6])
    sektorler = [int(x) for x in sys.argv[6:]]
    t_hep, f_hep, e_hep = [], [], []
    for d in indir(ra, dec, sektorler):
        t, f, e = oku(d); t_hep.append(t); f_hep.append(f); e_hep.append(e)
    t, f, e = map(np.concatenate, (t_hep, f_hep, e_hep))
    T0_eski = T0
    T0 = efemeris_merkezle(t, f, T0, P)
    for tur in (1, 2):                                        # 1. tur: hizli (en kucuk kareler); 2. tur: MCMC
        sekil = sekil_uydur(t, f, e, T0, P)
        print(f"Tur {tur}: Rp/R* = {sekil[0]:.4f}, a/R* = {sekil[1]:.2f}, i = {sekil[2]:.2f}")
        sure = P / np.pi / sekil[1]                          # kabaca gecis suresi (gun)
        satir = []
        for n in range(int(np.ceil((t.min() - T0) / P)), int(np.floor((t.max() - T0) / P)) + 1):
            tc0 = T0 + n * P
            w = np.abs(t - tc0) < 1.5 * sure                   # gecisin iki yani + taban
            giris = np.any((t > tc0 - 0.6 * sure) & (t < tc0 - 0.4 * sure))
            cikis = np.any((t > tc0 + 0.4 * sure) & (t < tc0 + 0.6 * sure))
            if w.sum() < 50 or not (giris and cikis):           # kismi gecis: kullanma
                continue
            tc, h, art = tek_gecis(t[w], f[w], e[w], tc0, P, sekil, mcmc=(tur == 2))
            satir.append((n, tc, h))
        n_, tc_, h_ = np.array(satir).T
        q = np.polyfit(n_, tc_, 1, w=1 / h_)                  # TESS zamanlarindan yerel efemeris
        P, T0 = q[0], q[1]
    for n, tc, h in satir:
        print(f"Tc = {tc:.6f} BJD_TDB  +- {h * 86400:5.1f} s")
    satir = [(np.round((tc - T0_eski) / P), tc, h) for _, tc, h in satir]   # epok: girilen T0'a gore
    np.savetxt(f"tess_{hedef}.csv", satir, delimiter=",", fmt=["%d", "%.6f", "%.6f"],
               header="epok,Tc_BJD_TDB,hata_gun")
