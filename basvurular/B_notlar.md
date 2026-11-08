# Belge B — Yeni gerekçe (yayımlanmamış TESS verisi + literatür çelişkisi), yeni adaylar, RV dahil

Ortak kurallar ve hocanın tüm uyarıları: ORTAK_KURALLAR.md (bu belgeye de aynen uygulanır).

## Araştırma notları

### B1. Yeni gerekçe
Wang vd. (2024)'nin LOOCV'yi geçen 14 adayından, (i) son yayımlanmış zamanlama analizinden sonra TESS'in yeniden
gözlediği ve bu verisi incelediğimiz yayınlarda kullanılmamış, (ii) literatürde dönem değişiminin varlığı ya da nedeni
konusunda çelişkili sonuçlar bulunan sistemler. Hocanın "değişim var mı yok mu onun üzerinde dur" ve "biri değişim var
diyor diğeri yok diyor" yönlendirmesiyle uyumlu. RV ile ışık-zaman/gelgit ayrımı, RV'nin yeterli olduğu sistemde yapılır.

### B2. 14 adayın taraması (8 Kasım 2026)
| Aday | Yayımlanmamış TESS? | Literatür çelişkisi? | Sonuç |
|---|---|---|---|
| WASP-4 b | Evet: 103, 105, 106 (2026) | Evet: gelgit (Baştürk 2025, Harre 2023) / ışık-zaman (Bouma 2020, Winn ve Stefánsson 2025); RV ivmesi tartışmalı (Baluev 2020, Turner 2022) | **Seçildi** |
| WASP-45 b | Evet: 69 (2023), 96 (2025), 106, 107 (2026) | Evet: Wang −169 ± 21 (8σ) / Sodickson 2025 −55 ± 13, "veri seyrek, hatalar küçük verilmiş, sistemde ek yıldız var" | **Seçildi** |
| WASP-46 b | Evet: 94, 95 (2025), 102–105 (2026) | Evet: Petrucci 2018 değişim yok; Davoudi 2021 artış; Adams 2024 +21,6 ± 8,2 ama ΔBIC 2; Wang +51,7 ± 2,9; Kutluay 2026 +10,4 ± 1,1 ama ΔBIC 1,36 | **Seçildi** |
| WASP-22 b | 105–107 (2026) **Stinga 2026 RNAAS 10, 297 tarafından analiz edildi** | Wang'ın −72'si 2026 verisiyle dışlandı | Elendi (soru cevaplanmış) |
| TrES-1 b | Yalnız 81 | Evet | Elendi (yeni veri çok az; A'da var) |
| WASP-12, HAT-P-7, CoRoT-2, KELT-16, TrES-5 | Hayır (tüm sektörler kullanılmış) | — | Elendi |
| HAT-P-37 b | 74, 75, 80, 82 var ama Wang 2024: 'TESS yedi sektörde gözledi, ilk altısı ciddi arka plan kirliliği nedeniyle kullanılamıyor' (kullanılan tek sektör 59) → yeni sektörlerin kullanılabilirliği şüpheli | Aslında var: Baluev 2019 −27,2 ± 8,8 (gelgite hafif tercih); AJ 163, 77 (2022) apsis tercih; Wang −34,3 | Elendi (veri kullanılabilirliği) |
| XO-4 b, WASP-10 b, WASP-1 b | Birer sektör (2024) | Hayır (dönem değişimi için tek çalışma ya da uyumlu sonuçlar) | Elendi |

### B3. Yeni sektörlerin envanteri (ışık eğrileri indirilip sayıldı; 120 s SPOC, kalite bayrağı 0)
- WASP-4 b: S103 15, S105 15, S106 11 → ~41 tam geçiş.
- WASP-45 b: S69 7, S96 6, S106 4, S107 7 → ~24 tam geçiş.
- WASP-46 b: S94 15, S95 14, S102 16, S103 15, S104 15, S105 15 → ~90 tam geçiş.
(Tam geçiş: geçiş içi noktaların ≥%80'i ve geçiş dışı noktaların ≥%60'ı var. Formda sayı verilmeyecek, yalnızca
sektörler ve verinin mevcut olduğu yazılacak.)

### B4. Literatür ayrıntıları
**WASP-45 b** (K2V yıldız, P = 3,126 g): Anderson 2012 (keşif); Ciceri 2016 (fiziksel parametreler, çok bantlı);
Ivshina ve Winn 2022; Wang 2024 (10 literatür + 14 TESS [S2, S29]; −169,21 ± 21,09; 8σ; LOOCV geçti);
Sodickson ve Grunblatt 2025 ApJ 993, 78 (24 zaman, IW22'den sonra yeni gözlem yok; −55,11 ± 13,12; ΔBIC 14;
Q′ ~ 3×10²; "büyük olasılıkla veri seyrekliğinden"; ek yıldız). Dikine hız: DACE 12 ölçüm, 0,3 yıl (yetersiz).
**WASP-46 b** (G6 yıldız, kromosferik aktif, P = 1,430 g): Anderson 2012; Ciceri 2016; Petrucci 2018 MNRAS 473, 5126
(12 yeni + 37 literatür; anlamlı azalma yok; σ = 1,66 dk saçılma, yıldız aktivitesine bağlanmış);
Davoudi 2021 Astron. Lett. (dönem artıyor); Ivshina ve Winn 2022; Adams 2024 (+21,6 ± 8,2; düzeltmeden sonra
ΔBIC 2); Wang 2024 (+51,68 ± 2,86; 18σ); Kutluay 2026 (TESS 1, 27, 67; +10,4 ± 1,1; ΔBIC 1,36; anlamlı değil).
Dikine hız: DACE 21 ölçüm, 8,5 yıl ama hassasiyet düşük.
**WASP-4 b**: A_notlar.md A3'teki liste. Yeni TESS: 103, 105, 106.
- OpenReview'da "Transit Timing Variations of Exoplanet WASP-4b: Decrease in the Orbital Period" başlıklı bir
  çalışma görüldü; tarayıcı doğrulaması nedeniyle içeriğine erişilemedi; hakemli dergi kaydı bulunamadı.

## Kararlar
- Hedefler: WASP-4 b, WASP-45 b, WASP-46 b (3 sistem; 4 zorunlu değil).
- WASP-22 b çıkarıldı: 2026 sektörleri Stinga 2026 (RNAAS 10, 297) tarafından analiz edilmiş, Wang'ın −72'si dışlanmış.
- Ölçüt 1: en az iki kullanılmamış VE kullanılabilir TESS sektörü (HAT-P-37 nedeniyle eklendi).
- Ölçüt 2: dönem değişiminin varlığı ya da nedeni konusunda çelişkili yayımlanmış sonuçlar.
- RV: WASP-4 için güçlü; WASP-45 ve WASP-46 için zayıf → "ayırt edilemedi" olasılığı açıkça yazıldı.
- Özgünlük: incelediğimiz yayınlarda kullanılmamış 13 TESS sektörü (2023–2026). "Hiçbir yayında" denmedi.
- TrES-5 ve WASP-22, 1.1'de "bildirilen değişimin yeni veriyle doğrulanamadığı" örnekleri olarak kullanıldı (hocanın TrES-5 önerisi).
- Yeni kaynaklar (Crossref doğrulandı): Anderson 2012, Ciceri 2016 (formda kullanılmadı), Petrucci 2018, Davoudi 2021, Stinga 2026.

## Kontrol kayıtları
- 8 Kasım, kontrol.py: özet 229 kelime; 1.1 = 5228, 1.2 = 1143, 2 = 10444 karakter; 39 kaynak, hepsi atıflı,
  alfabetik; yasak terim yok (Research Notes yalnızca kaynakçadaki dergi adı); takvim 100; Yöntem'de İP yok.
- DOI: 37 DOI'nin 34'ü birebir; 3 uyarı A'dakiyle aynı ve açıklamalı (Foreman-Mackey, Kreidberg, Ricker).
- Yazım sonrası olgusal düzeltmeler: Petrucci 2018 cümlesi "olabileceği" diye yumuşatıldı (makale "could be");
  HAT-P-37 satırı Wang'ın "yedi sektörden altısı arka plan kirliliği nedeniyle kullanılamıyor" ifadesine göre
  düzeltildi; ölçüt 1'e "kullanılabilir" eklendi.
- Word: 10 sayfa, doğrulama geçti; 249 parça birebir; Tablo 1 sayfası gözle kontrol edildi.
- 2. tur okuma: 1.1 ve Yöntem yeniden okundu; ek hata bulunmadı.
