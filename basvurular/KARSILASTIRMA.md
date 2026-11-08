# Üç başvuru metninin karşılaştırması ve puanlaması (8 Kasım 2026, ikinci kontrol turundan sonra)

| | A | B | C |
|---|---|---|---|
| Hedefler | WASP-12 b, WASP-4 b, HAT-P-7 b, TrES-1 b | WASP-4 b, WASP-45 b, WASP-46 b | WASP-45 b, WASP-46 b |
| Seçim gerekçesi | TESS ≥ 30 geçiş + ışık-zaman etkisi RV ile sınanmış | ≥ 2 kullanılmamış TESS sektörü + literatürde çelişki | ≥ 2 kullanılmamış TESS sektörü + değişimin varlığı üzerine çelişki |
| Kullanılmamış TESS verisi | 4 sektör (WASP-4: 3, TrES-1: 1) | 12 sektör (~148 tam geçiş) | 9 sektör (~107 tam geçiş) |
| Dikine hız | Var (4 sistemde de yeterli) | Var (WASP-4 güçlü; WASP-45/46 zayıf) | Yok (ışık-zaman/Rømer kapsam dışı) |
| Mekanizma sayısı | 6 | 6 | 5 |
| Kaynak sayısı | 43 | 41 | 36 |
| Özet (kelime) | 247 | 229 | 239 |

## Hocanın notlarına uyum
Üçü de 14 notun ve WhatsApp uyarılarının hepsini karşılıyor (otomatik kontrol + okuma). Tek fark not 3–4 (özgünlük):
A'da özgünlük yalnızca iki sistemde yeni veriye dayanıyor; B ve C'de tüm hedeflerde kullanılmamış TESS verisi var.

## Puanlama (100 üzerinden; TÜBİTAK ağırlıklarıyla + hocanın uyarıları)
| Ölçüt (ağırlık) | A | B | C |
|---|---|---|---|
| Bilimsel nitelik ve özgünlük (35) | 22 | 31 | 28 |
| Yöntem (25) | 22 | 22 | 20 |
| Proje yönetimi ve yapılabilirlik (20) | 16 | 16 | 18 |
| Yaygın etki (20) | 14 | 16 | 14 |
| **Toplam** | **74** | **85** | **80** |

Gerekçeler:
- A: Yöntem en eksiksiz (dört sistemde RV var, iki bilinen sonuçla kalibrasyon), ama hocanın en büyük itirazı
  (3. not) yarım cevaplanıyor: WASP-12 ve HAT-P-7'nin tüm TESS verisi yayımlanmış; hakem "yapılmış işi tekrar"
  diyebilir.
- B: Özgünlük açık (13 sektörlük kullanılmamış veri, üç tartışmalı sistem), hocanın 6 mekanizmalı ilk talimatı
  korunuyor, "değişim var mı yok mu" vurgusu da var. Zayıf yanı: WASP-45/46'da RV yetersiz, bu iki sistemde
  ışık-zaman etkisi için "ayırt edilemedi" çıkabilir (metinde açıkça yazıldı).
- C: En sade ve hocanın "değişim var mı yok mu onun üzerinde dur" sözüne en yakın. Ama yalnız iki sistem var ve
  hocanın ilk talimatındaki Rømer kapsam dışı; gelgit için en fazla "olası" denebiliyor.

Öneri: Hoca onaylarsa B. Hoca "RV'ye girme, basit tut" derse C. A, yalnızca hedeflerin değişmemesi istenirse.

## Lisans öğrencisi için zorluk (ikinci tur)
| İş | A | B | C |
|---|---|---|---|
| Zaman derleme ve BJD_TDB dönüşümü (Astropy) | Orta (4 sistem, çok kaynak) | Orta | Kolay–orta |
| TESS ışık eğrisi, batman, emcee | Kolay (4 sektör) | Orta (12 sektör) | Orta (9 sektör) |
| O−C, en küçük kareler, BIC | Kolay | Kolay | Kolay |
| Gelgit Q′*, Roche, Applegate enerjisi, Irwin kütle fonksiyonu | Kolay (formüle sayı koyma) | Kolay | Kolay |
| Apsis | Kolay (RV'den e ile genlik karşılaştırma) | Kolay | Orta (5 parametreli modeli zamanlara uyumlama) |
| Dikine hız Kepler modeli (çok tayfçeker, jitter, MCMC) | Zor (4 sistem) | Orta–zor (asıl iş WASP-4) | Yok |
Sonuç: C en kolay, B orta, A en yüklü. Hiçbiri lisans düzeyini aşmıyor; en zor kısım (RV modeli) danışman desteğiyle yapılabilir.
Yapılabilirlik ölçümü: tek geçiş zamanlama hassasiyeti WASP-45/46 ~75 s, WASP-4 ~37 s; tartışılan değişimler 2026'da
7–10 dakikalık farklar üretiyor, yani yeni sektörler soruyu cevaplamaya yetiyor.

## İkinci turda değişen
- B ve C: WASP-45'in 69. sektörü ExoClock IV (Kokori vd., 2026) tarafından kullanılmış → çıkarıldı; Yeh vd. (2024) eklendi.
- Üçü: Applegate'e enerji bağıntısı (Watson ve Marsh, 2010) eklendi.
- A: "yayımlanmamış" ifadeleri düzeltildi.
- Puanlar değişmedi (B'nin özgünlüğü bir sektör azaldı ama hâlâ tüm hedeflerde yeni veri var).
