"""WASP-4 b alistirmasi: RV'den Romer ongorusu ve gecis zamanlarindan O-C, sonra karsilastirma.
Veri: Bouma vd. 2020 (VizieR J/ApJ/893/L29, table2 = RV, table1 = gecis zamanlari). P, T0: NASA Exoplanet Archive.
Google Colab'da hucre hucre ya da tek parca calistirilabilir (kilavuz Ek B).
"""
import pandas as pd, numpy as np, matplotlib.pyplot as plt

# --- Hucre 1: RV tablosunu indir
url = "https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=J/ApJ/893/L29/table2&-out.max=999&-out=BJD,RV,e_RV,Tel"
d = pd.read_csv(url, sep="\t", comment="#").iloc[2:]
d["BJD"] = d["BJD"].astype(float) + 2450000
d["RV"] = d["RV"].astype(float); d["e_RV"] = d["e_RV"].astype(float); d["Tel"] = d["Tel"].str.strip()
print(len(d), "olcum")                                             # 48

# --- Hucre 3: gecis sirasindaki olcumleri at
P, T0 = 1.338231, 2455804.515679
evre = ((d["BJD"] - T0) / P + 0.5) % 1 - 0.5
d = d[abs(evre) > 0.04]                                            # 45 olcum

# --- Hucre 4-5: alet sifirlari + egim + gezegen sinusu
t, v, s = d["BJD"].values, d["RV"].values, d["e_RV"].values
yil = (t - t.mean()) / 365.25; aci = 2 * np.pi * (t - T0) / P
X = np.column_stack([d["Tel"] == "CORALIE", d["Tel"] == "HARPS", d["Tel"] == "HIRES",
                     yil, np.sin(aci), np.cos(aci)]).astype(float)
A, b = X / s[:, None], v / s
p, *_ = np.linalg.lstsq(A, b, rcond=None)
kikare = np.sum((b - A @ p) ** 2) / (len(t) - 6)
hata = np.sqrt(np.diag(np.linalg.inv(A.T @ A)) * max(kikare, 1))
print("egim", p[3].round(2), "+-", hata[3].round(2), "m/s/yil")   # -15.20 +- 0.92

# --- Hucre 6: Romer ongorusu
c, sy = 299792458, 365.25 * 86400
romer = P * 86400 * (p[3] / sy) / c * sy * 1000
romer_h = P * 86400 * (hata[3] / sy) / c * sy * 1000
print("Romer", round(romer, 2), "+-", round(romer_h, 2), "ms/yil")  # -5.86 +- 0.36 (Bouma: -5.94 +- 0.39)

# --- Hucre 7-9: gecis zamanlari -> O-C -> dP/dt
url2 = "https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=J/ApJ/893/L29/table1&-out.max=999&-out=BJD,e_BJD,Epoch"
g = pd.read_csv(url2, sep="\t", comment="#").iloc[2:].astype(float)
E, T, h = g["Epoch"].values, g["BJD"].values, g["e_BJD"].values
lin = np.polyfit(E, T, 1, w=1/h)
k, kov = np.polyfit(E, T, 2, w=1/h, cov="unscaled")
chi_l = np.sum(((T - np.polyval(lin, E)) / h) ** 2); chi_q = np.sum(((T - np.polyval(k, E)) / h) ** 2)
olcek = np.sqrt(max(chi_q / (len(E) - 3), 1))
oc = 2 * k[0] / k[1] * sy * 1000; oc_h = 2 * np.sqrt(kov[0, 0]) * olcek / k[1] * sy * 1000
dbic = (chi_l + 2 * np.log(len(E))) - (chi_q + 3 * np.log(len(E)))
print("O-C dP/dt", round(oc, 2), "+-", round(oc_h, 2), "| dBIC", round(dbic, 1))  # -8.66 +- 1.27 | 89.2

# --- Hucre 10: karsilastirma
fark = abs(oc - romer) / np.hypot(oc_h, romer_h)
print("fark", round(fark, 1), "sigma | kalan", round(oc - romer, 2), "+-", round(np.hypot(oc_h, romer_h), 2))  # 2.1 sigma, -2.8 +- 1.3
assert abs(romer + 5.86) < 0.05 and abs(oc + 8.66) < 0.05      # beklenen sonuclar
