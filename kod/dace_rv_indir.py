"""DACE arsivinden (Cenevre) bir yildizin yayimlanmis RV olcumlerini indirir, rv_analiz.py'nin okudugu CSV'ye yazar.
Kullanim:  python dace_rv_indir.py WASP-12 1.091418901 2457607.519305
           (yildiz adi, P [gun], T0 [BJD_TDB]; P ve T0 gecis icindeki RV'leri atmak icin)
Kurulum:   pip install dace-query      (hesap gerekmez; herkese acik veriler)
"""
import sys
import numpy as np
from dace_query.spectroscopy import Spectroscopy

yildiz, P, T0 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
d = Spectroscopy.get_timeseries(yildiz, sorted_by_instrument=False, output_format="dict")
t = np.array(d["rjd"], float) + 2400000                      # DACE zamani: BJD - 2400000
v, s = np.array(d["rv"], float), np.array(d["rv_err"], float)  # m/s
alet = np.array([str(x) for x in d["instrument_name"]])
faz = ((t - T0) / P + 0.5) % 1 - 0.5
tut = np.isfinite(v) & np.isfinite(s) & (s > 0) & (np.abs(faz) > 0.04)   # gecis sirasindaki (Rossiter) RV'leri at
u, n = np.unique(alet[tut], return_counts=True)
tut &= np.isin(alet, u[n >= 3])                               # 1-2 olcumlu alet yalniz kendi sifir noktasini belirler
np.savetxt(f"rv_{yildiz}.csv", np.column_stack([t[tut], v[tut], s[tut], alet[tut]]), fmt="%s",
           delimiter=",", header="BJD,RV_ms,hata_ms,alet", comments="")
print(f"{yildiz}: {tut.sum()} RV, {np.ptp(t[tut]) / 365.25:.1f} yil, aletler: {dict(zip(*np.unique(alet[tut], return_counts=True)))}")
