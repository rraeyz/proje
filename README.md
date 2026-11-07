# TÜBİTAK 2209-A — Sıcak Jüpiterlerde Yörünge Dönemi Değişimi (O−C)

| Dosya | Ne işe yarar |
|---|---|
| `kilavuz.pdf` / `kilavuz.tex` | Adım adım proje kılavuzu (50 sayfa). `.tex` tek dosyadır; Overleaf'e yapıştır, `sekiller/` klasörünü yükle. |
| `TUBITAK_2209A_form_metinleri.md` | Word formuna kopyala-yapıştır metinleri (Özet, Bilimsel Nitelik, Yöntem, Proje Yönetimi, Yaygın Etki, Kaynaklar). |
| `sekiller/sekil1_WASP-12b_OC.png`, `sekil2_dort_hedef_OC.png` | Forma konacak ön çalışma şekilleri. |
| `kod/` | `oc_diyagrami.py`, `tess_zaman.py`, `rv_analiz.py`, `fizik_testleri.py`, `zaman_donusum.py`, `secim_tablosu.py` |
| `veri/` | Bu projede ölçülen yeni TESS geçiş zamanları (`tess_*.csv`) ve O−C tabloları (`zamanlar_*.csv`). |
| `parcalar/` | `kilavuz.tex`'in kaynak parçaları; `python parcalar/birlestir.py` ile yeniden birleştirilir. |

Hızlı başlangıç (Google Colab):

```
!pip install -q astropy astroquery batman-package emcee
!python oc_diyagrami.py "WASP-12 b" WASP-012
```
