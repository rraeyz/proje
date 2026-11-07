# TÜBİTAK 2209-A — Sıcak Jüpiterlerde Yörünge Dönemi Değişimi (O−C)

| Dosya | Ne işe yarar |
|---|---|
| `2209-A_Arastirma_Onerisi_Formu_Idris_Avlar.docx` | Hocaya gidecek doldurulmuş Word formu. |
| `TUBITAK_2209A_form_metinleri.md` | Aynı form metninin düz hali (TYBS'ye kopyalamak için). |
| `kilavuz.pdf` / `kilavuz.tex` | Başvuru kılavuzu: aday seçimi, TYBS adımları, olası sorular, yapılan her şey, form metni (Ek A). |
| `kod/secim_tablosu.py` | Tablo 1'i (hedef seçimi) açık arşivlerden üretir. |
| `kod/oc_diyagrami.py`, `tess_zaman.py`, `rv_analiz.py`, `fizik_testleri.py`, `zaman_donusum.py` | Analiz kodları (O−C, TESS zaman ölçümü, RV/Rømer, fiziksel testler, zaman dönüşümü). |
| `kod/kilavuz_ek_uret.py` | Kılavuzun Ek A'sını form metninden üretir. |
| `veri/` | Tablo 1 (`tablo1_secim.csv`), RV verileri (`rv_*`), denemede ölçülen TESS zamanları (`tess_*.csv`). |
| `sekiller/`, `on_calisma_colab.ipynb` | Eski denemeler; formda kullanılmıyor. |

Kılavuzu derlemek (proje kökünden):

```
python kod/kilavuz_ek_uret.py
pdflatex kilavuz.tex && pdflatex kilavuz.tex
```
