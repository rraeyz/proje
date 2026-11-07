"""on_calisma_colab.ipynb defterini kod/ klasorundeki GUNCEL dosyalardan uretir.
Kullanim (proje kokunden):  python kod/defter_olustur.py
Kodlar degisirse bu betigi yeniden calistir; defterdeki kod her zaman kod/ ile ayni olur.
"""
import json, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
oku = lambda ad: (KOK / "kod" / ad).read_text()
md = lambda t: {"cell_type": "markdown", "metadata": {}, "source": t}
code = lambda t: {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": t}

H = [
md("""# Ön Çalışma: Şekil 1, Şekil 2, Tablo 1 ve metindeki sayıları kendin üret

Bu defter başvurudaki ön çalışmanın **her şeklini, tablosunu ve sayısını** baştan üretir. Hücreleri **yukarıdan aşağı, sırayla**
çalıştır (hücreye tıkla → **Shift + Enter**). Her hücrenin üstünde ne yaptığı ve ekranda **ne görmen gerektiği** yazıyor.
Ölçümlerde rastgele sayı üreteci sabitlendiği için (seed = 42) sonuçlar her çalıştırmada aynıdır.

| Başvurudaki öğe | Bu defterdeki adım |
|---|---|
| Tablo 1 (hedef seçimi) | Adım 3 |
| WASP-12 b katalog sonucu | Adım 4 |
| Sektör 20 doğrulaması (−1,7 s; 0,40σ) | Adım 5 |
| Şekil 1 | Adım 6–7 |
| 174 yeni TESS zamanı ve Şekil 2 | Adım 8–9 |

Kullanılan her şey herkese açık: VizieR (Ivshina ve Winn 2022; Wang vd. 2024; Knutson vd. 2014; Bouma vd. 2020; Bonomo vd. 2017),
NASA MAST (TESS ışık eğrileri), NASA Exoplanet Archive, DACE. Süre: yaklaşık 30–40 dakika (çoğu bekleme)."""),
md("""## Adım 1 — Gerekli Python paketlerini kur
`astropy` (zaman/koordinat), `astroquery` (arşivden indirme), `batman` (geçiş modeli), `emcee` (MCMC), `dace-query` (DACE RV arşivi)."""),
code("!pip install -q astropy astroquery batman-package emcee dace-query"),
md("""## Adım 2 — Kod dosyalarını oluştur
Aşağıdaki hücreler kodları Colab klasörüne kaydeder; her biri için yalnızca "Writing ..." görmelisin. Her fonksiyonun ne yaptığı kodun içinde yazıyor.
- `oc_diyagrami.py`: geçiş zamanlarını indirir, epokları hesaplar, hata çubuklarını gerçekçi hale getirir, doğru/parabol uydurur, dP/dt ve ΔBIC'i yazar, O−C şeklini çizer.
- `tess_zaman.py`: TESS ışık eğrisini indirir ve her geçişin orta zamanını ölçer.
- `rv_analiz.py`: radyal hız (RV) verisine yıldız eğilimi uydurur ve Rømer etkisinin öngördüğü dönem değişimini hesaplar.
- `secim_tablosu.py`: Tablo 1'i (14 adaydan hedef seçimi) herkese açık kaynaklardan hesaplar."""),
code("%%writefile oc_diyagrami.py\n" + oku("oc_diyagrami.py")),
code("%%writefile tess_zaman.py\n" + oku("tess_zaman.py")),
code("%%writefile rv_analiz.py\n" + oku("rv_analiz.py")),
code("%%writefile secim_tablosu.py\n" + oku("secim_tablosu.py")),
md("""## Adım 3 — Tablo 1: 14 adaydan hedef seçimi
- **K1:** Wang vd. (2024) Tablo 3'te LOOCV sütunu "pass" olan 14 aday (bu sütun makalenin kendisinde; gösterirken makalenin Tablo 3'ünü aç).
- **K2:** Wang vd.'nin TESS geçiş zamanı sayısı ≥ 30 (VizieR'deki tablolarında satırlar sayılır).
- **K3:** Arşiv RV'sinden Rømer öngörüsünün belirsizliği < Wang vd.'nin |dP/dt| değerinin üçte biri (her aday için tüm arşivler denenir, en hassası alınır).

**Görmen gereken (≈3–5 dk):** `SECILDI` yalnızca **TrES-1 b** (σ 2,2 · Bonomo 2017), **WASP-4 b** (0,4 · Bouma 2020), **WASP-12 b** (1,6 · Knutson 2014),
**HAT-P-7 b** (1,2 · Knutson 2014) satırlarında. KELT-16, TrES-5 ve WASP-46 → `K3 saglanmiyor`; diğer yedisi → `K2 saglanmiyor`.
Sonuç `tablo1_secim.csv` dosyasına da yazılır."""),
code("!python secim_tablosu.py"),
md("""## Adım 4 — Sadece hazır katalog verisiyle WASP-12 b
**Görmen gereken:** `WASP-12 b: n=189 (TESS 82), dP/dt = -28.69 +- 1.03 ms/yil, DBIC = 770.5`
(Literatür değeri −29 ± 2 ms/yıl; Yee vd. 2020.)"""),
code('!python oc_diyagrami.py "WASP-12 b" WASP-012'),
md("""## Adım 5 — Ölçüm yöntemini doğrula: Wang vd.'nin ölçtüğü sektör 20
Wang vd.'nin **zaten ölçtüğü** TESS sektör 20'yi kendimiz ölçüp onların sonucuyla karşılaştırıyoruz (≈3–5 dk).

**Görmen gereken:** `Tur 2: Rp/R* = 0.1138, a/R* = 3.11` ve 21 satır `Tc = ...`"""),
code("!python tess_zaman.py WASP-12 97.6366450 29.6722662 1.091418901 2457607.519305 20\n!mv tess_WASP-12.csv dogrulama_sektor20.csv"),
md("""**Görmen gereken:** `olculen 21, ortak 20 | ortalama fark -1.7 s | ortanca |fark|/sigma 0.40 | ortanca hata 45 s`
Sistematik kayma yok, farklar hata payının içinde → ölçüm yöntemi doğrulandı."""),
code("""import numpy as np, oc_diyagrami as oc
ben = np.loadtxt("dogrulama_sektor20.csv", delimiter=",")
w = oc.vizier("J/ApJS/270/14/table1", Name="WASP-12 b")
wt = np.array([float(x["Tc"]) for x in w]); ws = np.array([float(x["e_Tc"]) for x in w])
fark, sig = [], []
for _, tc, h in ben:
    j = np.argmin(abs(wt - tc))
    if abs(wt[j] - tc) < 0.02:
        fark.append((tc - wt[j]) * 86400); sig.append((tc - wt[j]) / np.hypot(h, ws[j]))
fark, sig = np.array(fark), np.array(sig)
print(f"olculen {len(ben)}, ortak {len(fark)} | ortalama fark {fark.mean():+.1f} s | ortanca |fark|/sigma {np.median(abs(sig)):.2f} | ortanca hata {np.median(ben[:, 2]) * 86400:.0f} s")"""),
md("""## Adım 6 — Wang vd. sonrası yeni TESS sektörleri (71 ve 72)
**Görmen gereken (≈5–8 dk):** `Tur 2: Rp/R* = 0.1131, a/R* = 3.12` ve 38 satır `Tc = ...`"""),
code("!python tess_zaman.py WASP-12 97.6366450 29.6722662 1.091418901 2457607.519305 71 72"),
md("""## Adım 7 — Şekil 1
**Görmen gereken:** `WASP-12 b: n=227 (TESS 120), dP/dt = -30.90 +- 0.90 ms/yil, DBIC = 1177.1`
`OC_WASP-12b.png` dosyası **başvurudaki Şekil 1'dir**."""),
code('!python oc_diyagrami.py "WASP-12 b" WASP-012 tess_WASP-12.csv\nfrom IPython.display import Image\nImage("OC_WASP-12b.png")'),
md("""## Adım 8 — Diğer üç hedefin yeni TESS sektörleri (≈15 dk)
**Görmen gereken:**
- `WASP-4 b: n=197 (TESS 122), dP/dt = -4.79 +- 0.40 ms/yil, DBIC = 137.7`
- `HAT-P-7 b: n=117 (TESS 106), dP/dt = 30.00 +- 4.73 ms/yil, DBIC = 35.5`
- `TrES-1 b: n=94 (TESS 55), dP/dt = -4.26 +- 2.63 ms/yil, DBIC = -1.9` (anlamlı değişim yok)"""),
code("""!python tess_zaman.py WASP-4 353.5629149 -42.0617794 1.338231 2455804.515679 36 69 96 103 105 106
!python tess_zaman.py HAT-P-7 292.2471900 47.9695429 2.204737 2454954.358572 74 75 78 81 82 86
!python tess_zaman.py TrES-1 286.0408755 36.6325360 3.03007 2453186.806341 74 78 80 81 86
!python oc_diyagrami.py "WASP-4 b" WASP-004 tess_WASP-4.csv
!python oc_diyagrami.py "HAT-P-7 b" HAT-P-07 tess_HAT-P-7.csv
!python oc_diyagrami.py "TrES-1 b" TrES-1 tess_TrES-1.csv"""),
md("""**Görmen gereken:** `WASP-12 38 | WASP-4 75 | HAT-P-7 40 | TrES-1 21 | TOPLAM 174` (metindeki "174 yeni TESS geçiş zamanı")."""),
code("""import numpy as np
say = {h: len(np.loadtxt(f"tess_{h}.csv", delimiter=",")) for h in ["WASP-12", "WASP-4", "HAT-P-7", "TrES-1"]}
print(" | ".join(f"{h} {n}" for h, n in say.items()), "| TOPLAM", sum(say.values()))"""),
md("""## Adım 9 — Şekil 2: dört paneli birleştir
`sekil2_dort_hedef_OC.png` **başvurudaki Şekil 2'dir.** Sol menüdeki klasör simgesinden PNG ve CSV dosyalarını indir."""),
code("""import matplotlib.pyplot as plt, matplotlib.image as im
fig, ax = plt.subplots(2, 2, figsize=(14, 8.2))
for a, ad in zip(ax.flat, ["WASP-12b", "WASP-4b", "HAT-P-7b", "TrES-1b"]):
    a.imshow(im.imread(f"OC_{ad}.png")); a.axis("off")
plt.tight_layout(); plt.savefig("sekil2_dort_hedef_OC.png", dpi=150); plt.show()"""),
]
nb = {"cells": H, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}},
      "nbformat": 4, "nbformat_minor": 5}
for c in nb["cells"]:
    c["source"] = c["source"].splitlines(keepends=True)
(KOK / "on_calisma_colab.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1))
print("on_calisma_colab.ipynb yazildi:", len(H), "hucre")
