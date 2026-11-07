# Bekleyen değişiklikler (son halde uygulanacak)

Son halde hepsi birlikte işlenecek: TYBS'ye alan alan kopyalanacak metin (`TUBITAK_2209A_form_metinleri.md`),
Word taslağı, `kilavuz.pdf`/`.tex` (Kısım I + Kısım II'deki ilgili yerler), şekiller.

**GENEL KURAL: UAK, kongre, bildiri hiçbir yerde geçmeyecek** (form metni, özet, yaygın etki, Word taslağı, kılavuz). Akademik çıktı
yalnızca: proje sonuç raporu (kesin) + kısa makale (yalnız "hedeflenmektedir").

## A. Yöntemde yapılan düzeltme ve YENİ SAYILAR (7 Kasım; kod güncellendi)

Hata çubukları artık veri grubu (literatür / TESS) başına, kuadratik model artıklarının indirgenmiş χ²'si 1 olacak şekilde
büyütülüyor (`oc_diyagrami.hata_olcekle`). Sebep: TrES-1 literatür zamanlarında χ²ν = 7,3 (2006–2007 yer gözlemlerine
9–18 s hata verilmiş, 4–8σ sapıyorlar); TESS grubunda χ²ν = 0,9. Ölçeklemesiz sonuçlar fazla iyimserdi.

**KANONİK SAYILAR** (sabit MCMC tohumu seed=42; her çalıştırmada aynı; `on_calisma_colab.ipynb` ile birebir üretilir):

| Hedef | dP/dt (ms/yıl) | anlamlılık | ΔBIC | Rømer öngörüsü | fark | kübik ΔBIC |
|---|---|---|---|---|---|---|
| WASP-12 b (n=227) | −30,90 ± 0,90 | 34σ | 1177 | −0,8 ± 1,7 (DACE) | 15,7σ → dışlandı | ~5,7 (gereksiz) |
| WASP-4 b (n=197) | −4,79 ± 0,40 | 12σ | 138 | −5,95 ± 0,32 (Bouma) | 2,3σ → Rømer kısalmanın tamamını karşılıyor | ~5,5 (gereksiz) |
| HAT-P-7 b (n=117) | +30,00 ± 4,73 | 6,3σ | 35,5 | +13,1 ± 1,2 (Knutson) | 3,5σ → kısmen (~%44) | ~−2,7 |
| TrES-1 b (n=94) | −4,26 ± 2,63 | 1,6σ | −1,9 | −2,5 ± 2,2 (Bonomo) | 0,5σ | ~5,1 |

- Yeni TESS zamanları: WASP-12 38 (ortanca hata 43 s), WASP-4 75 (33 s), HAT-P-7 40 (56 s), TrES-1 21 (31 s); TOPLAM 174.
- İP2 doğrulaması (sektör 20): ölçülen 21, ortak 20, ortalama fark −1,7 s, ortanca |fark| 0,40σ, ortanca hata 45 s.
- Katalog-yalnız WASP-12: −28,69 ± 1,03, ΔBIC 770,5.
- Tablo 1 (`veri/tablo1_secim.csv`, `kod/secim_tablosu.py`): σ_Rømer en hassas arşivle — WASP-12 1,6 (Knutson), WASP-4 0,4 (Bouma),
  HAT-P-7 1,2 (Knutson), TrES-1 2,2 (Bonomo), TrES-5 29,2 (DACE), WASP-46 56,3 (DACE), KELT-16 arşivde yok. K2'de elenenlerde "–".
  TESS sayıları VizieR tablosundan sayılır (WASP-12: 81; makale metni 82 — eşiği etkilemez).
- Form metnindeki tüm sayılar bu kanonik değerlere göre yazılacak (ör. ön çalışma: "ortalama −1,7 s fark ve ortanca 0,4σ uyum";
  Şekil 1 açıklaması "dP/dt = −30,9 ± 0,9 ms/yıl").

- **TrES-1 b'de gerçekçi hatalarla anlamlı dönem değişimi YOK.** Bu hocanın "değişim var mı yok mu" sorusuna geçerli bir cevap.
- **WASP-4'te kübik terim artık gerekmiyor** (ΔBIC 5,5). "dP/dt zamanla değişiyor, kübik ΔBIC = 13" iddiası her yerden çıkacak.
  Yalnız gözlem olarak: yayımlanan değerler veri uzadıkça küçülüyor (−8,6 Bouma 2020; −6,4 Wang 2024; −4,8 bu çalışma).
- Periyodogramda hiçbir hedefte FAP < 0,01 tepe yok (WASP-12: 0,6 yıl, FAP 0,012 — yıllık örnekleme izi).
- Yalnız katalog verisiyle (14 aday, yeni yöntem) sağlam kalanlar: WASP-12 (−28,69±1,03; ΔBIC 770) ve WASP-4 (−7,24±0,97; ΔBIC 51).
  HAT-P-7 ancak yeni TESS verisiyle sağlamlaşıyor (katalog: ΔBIC 11,4, LOOCV kalır). Kısım II Bölüm 3 tablosu buna göre yenilenecek.
- **İP2 doğrulaması yapıldı:** WASP-12 sektör 20 yeniden ölçüldü; Wang vd. ile 20 ortak geçişte ortalama fark −2,2 s,
  ortanca |fark| 21 s = 0,42σ (ölçüt ≤ 1σ sağlandı). Benim ortanca hatam 45 s (Wang: 22 s).
- Şekil 1, Şekil 2 ve `veri/zamanlar_*.csv` yeni yöntemle üretildi (`sekiller/OC_*.png`); birleşik Şekil 2 paneli son halde yeniden yapılacak.

## B. Form metni (Kısım I) değişiklikleri

1. **Yang, Su ve Winn (2025)** (arXiv:2505.07927) eklenecek: HAT-P-7'de geçiş zamanlaması + RV ile ~32 AB'de eksantrik yıldız
   eşlikçi → 1.1'e bir cümle, kaynakçaya; HAT-P-7'deki "kısmen" sonucunun açıklaması (değişen ivme) buna bağlanacak.
2. **Özet son cümlesi:** "Bütçe gerektirmeyen 12 aylık projenin çıktıları dört hedef için güncel efemerisler, fiziksel köken hükümleri
   ve açık erişimli veri seti ile analiz kodudur; sonuçların danışmanla birlikte kısa bir makale olarak paylaşılması
   hedeflenmektedir."
   Özetteki ön çalışma cümlesi: "...174 yeni TESS geçiş zamanı ölçülmüş; WASP-12 b, WASP-4 b ve HAT-P-7 b'de anlamlı dönem değişimi
   bulunmuş, TrES-1 b'de bildirilen kısalma ise literatür zamanlarının belirsizlikleri gerçekçi biçimde değerlendirildiğinde
   anlamlılığını yitirmiştir; WASP-12 b için elde edilen −30,9 ± 0,9 ms/yıl değeri literatürle uyumludur."
3. **Yaygın Etki → Bilimsel/Akademik:** madde 25'e bakın (UAK/kongre/bildiri YOK).
4. **Kübik model kalıyor** (İP3'te model, İP4(d)'de eğrilik testi olarak); ön çalışmada "gerekmiyor" diye raporlanacak.
5. **1.1 son paragrafı (Kalkınma Planı / 2030 Stratejisi):** "Proje, On İkinci Kalkınma Planı'nın (2024–2028) temel bilimlere özel
   önem verilmesini ve uzay araştırmalarını kritik alanlar arasında sayan hedefiyle (madde 270) ve genç nesillerin uzay alanında
   çalışmaya teşvik edilerek uzay araştırmalarının yaygınlaştırılmasını öngören hedefiyle (madde 271) doğrudan ilişkilidir. 2030 Sanayi
   ve Teknoloji Stratejisi de TÜBİTAK araştırma desteklerinin astronomi dahil temel bilimlerde bilgi üretimini artıracak şekilde
   yaygınlaştırılmasını öngörmektedir (Temel Bilim Araştırmaları Liderlik Programı). Proje, uzay görevi verilerinin (TESS) işlenmesi
   ve yorumlanması konusunda lisans düzeyinde araştırmacı yetiştirilmesine katkı sağlayarak bu hedeflere hizmet etmektedir."
   (Öncelikli Alanlar 2025 listesinde astronomi yok → öncelikli alan iddia edilmeyecek.)
6. **1.1'e seçim gerekçesi:** "Hedefler, Wang vd. (2024)'nin LOOCV testini geçen 14 aday arasından TESS veri yeterliliği ve arşiv
   radyal hız verisinin yeterliliği ölçütleriyle seçilmiştir (bkz. Yöntem). Seçilen hedefler birbirini tamamlayan dört durumu temsil
   etmektedir: WASP-12 b doğrulanmış gelgit bozulmasıyla yöntemin kalibrasyonunu, WASP-4 b gelgit ile ışık-yolu etkisinin tartışıldığı
   bir vakayı, HAT-P-7 b gelgitle açıklanamayan bir dönem artışını, TrES-1 b ise bildirilen dönem kısalmasının literatür zamanlarının
   güvenilirliğine bağlı olup olmadığının sınandığı bir vakayı."
7. **RV öngörüsü formdan çıkacak:** Hedef 4 → "Dört hedef için güncel efemerisleri (T0, P ve varsa dP/dt) yayımlamak."; İP4'teki
   "Rømer açıklamasının gerektirdiği radyal hız eğimi ... raporlanacaktır" cümlesi silinecek; takvim İP4 başarı ölçütü →
   "24 hücrelik karar tablosunun tamamı gerekçeli (%35)"; Yaygın Etki/Yeni Proje → yalnız lisansüstü tez önerisi.
8. **Hipotezler (ön çalışmaya uygun):**
   - H1 aynı kalır.
   - H2: "WASP-4 b ve HAT-P-7 b'deki dönem değişimlerinin önemli bir kısmı, arşiv radyal hız ölçümlerinin gösterdiği ivmeden kaynaklanan
     ışık-yolu (Rømer) etkisiyle açıklanır."
   - H3: "TrES-1 b'de bildirilen dönem kısalması, literatür zamanlarının belirsizlikleri gerçekçi biçimde değerlendirildiğinde ve yeni
     TESS zamanları eklendiğinde istatistiksel olarak anlamlı değildir."
9. **Yöntem – Örneklem seçimi:**
   - "sonuçlara bakılmadan önce tanımlanan" → "bu projenin kendi O−C sonuçlarından bağımsız" (doğru olan bu).
   - K2: "en az birkaç TESS sektörüne" → "en az iki TESS sektörüne" (en kısa dönemli aday P≈0,97 gün → sektör başına ≤~28 geçiş).
   - K3: "gözlenen |dP/dt|" → "Wang vd.'nin raporladığı |dP/dt|".
   - Son cümle TrES-1 rolü: "...ve bildirilen dönem kısalmasının veri kalitesine duyarlılığının sınandığı bir vakayı temsil etmektedir."
10. **İP1:** İlk cümle: "Geçiş zamanları Ivshina ve Winn (2022) veritabanından, Wang vd. (2024)'nin TESS ölçümlerinden, ETD/VarAstro
    (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023) veritabanlarından ve hedefe özel makalelerden (...) derlenecektir."
    Belirsiz zaman sistemi cümlesi: "Zaman sistemi makalesinden belirlenemeyen zamanlar işaretlenecek; analiz bu zamanlar dahil ve hariç
    olmak üzere iki kez yapılarak sonucun bu zamanlara duyarlılığı raporlanacaktır."
11. **İP2:**
    - "Kenar kararması katsayıları sabit tutulacaktır; geçiş biçimi simetrik olduğundan orta zaman ölçümüne etkisi ihmal edilebilir."
    - Doğrulama cümlesi → "Yöntem, Wang vd.'nin ölçtüğü sektörlerden biri yeniden ölçülerek ortak geçişlerde karşılaştırılacak ve
      doğrulanacaktır." (Ön çalışma: WASP-12 sektör 20, 20 ortak geçiş, ortalama fark −2,2 s, ortanca fark 0,4σ.)
12. **İP3:** eklenecek: "Literatür ve TESS zamanlarının hata çubukları, her grubun kuadratik model artıklarından hesaplanan indirgenmiş
    χ² değeri 1 olacak şekilde (yalnızca büyütülerek) ölçeklenecektir." Kübik model eğrilik testi olarak kalır.
13. **İP4:**
    - (a) eklenecek: geçiş sırasında alınan RV'ler (Rossiter–McLaughlin etkisi) çıkarılacak; RV hataları yıldız titreşimi için ölçeklenecek;
      doğrusal eğilim yetersizse ikinci dereceden terim eklenecek; 2–3σ arası fark "kısmen/ayrılamadı" olarak raporlanacak.
    - (b) eklenecek: parametreler NASA Exoplanet Archive'dan; dönemi uzayan hedefte (yıldız yörüngeden yavaş döndüğü için) gelgit dışlanır
      (Wang vd., 2024).
    - (c) örtülme zamanları yalnız WASP-12 için mevcut (Yee vd., 2020).
    - (d) eklenecek: yanlış alarm olasılığı < 0,01 eşiği; ~1 yıllık (gözlem mevsimi) tepeler gerçek sinyal sayılmayacak.
    - Son cümlenin RV öngörüsü kısmı silinecek (madde 7).
14. **Ön çalışma paragrafı yalnız uygulanabilirliği gösterecek biçimde yeniden yazılacak; Tablo 2 (Rømer testi) formdan çıkacak.**
    Sebep: eski metin abartılı ("tüm adımlar") ve güncel değil ("dördünde de anlamlı", TrES-1 −12,7 / 3,5σ / Q′*≈8×10², 16σ, 1,9σ);
    ayrıca projenin cevaplayacağı fiziksel köken sonuçlarını önceden ilan ediyordu. Yeni metin:
    "Ön çalışma. Projenin uygulanabilirliği açık verilerle sınanmıştır. (i) Veri erişimi: Dört hedefin literatür ve TESS geçiş
    zamanlarına (Ivshina ve Winn, 2022; Wang vd., 2024), Wang vd. sonrası TESS sektörlerine ve yayımlanmış radyal hız ölçümlerine
    (Knutson vd., 2014; Bonomo vd., 2017; Bouma vd., 2020; DACE) erişilebildiği doğrulanmıştır (Tablo 1). (ii) Geçiş zamanı ölçümü:
    Wang vd.'nin ölçtüğü WASP-12 b TESS sektör 20'deki 20 geçiş yeniden ölçülmüş; elde edilen zamanlar Wang vd. ile ortalama −2 s fark
    ve ortanca 0,4σ uyum göstermiştir. Aynı yöntemle dört hedefte Wang vd. sonrası sektörlerden 174 yeni geçiş zamanı (tipik belirsizlik
    44 s) ölçülmüştür. (iii) Yöntem kalibrasyonu: WASP-12 b için katalog ve yeni TESS zamanlarıyla dP/dt = −30,9 ± 0,9 ms/yıl elde
    edilmiş ve literatür değeriyle (−29 ± 2 ms/yıl; Yee vd., 2020) uyumlu bulunmuştur (Şekil 1). Dört hedefin ilk O−C diyagramları
    Şekil 2'de verilmiştir. Bu sonuçlar verinin ve yöntemin proje hedeflerine ulaşmaya elverişli olduğunu göstermektedir; fiziksel köken
    analizleri (İP4) proje kapsamında yürütülecektir."
    - Şekil 1 açıklaması: −30,9 ± 0,9 ms/yıl, ΔBIC = 1180 (yeni yöntem). Şekil 2 açıklaması: yalnız "dört hedefin O−C diyagramları";
      "dördünde de" / ΔBIC listesi yeni sayılarla ya da hiç verilmeden.
    - Özetteki ön çalışma cümlesi de buna uyacak (madde 2'deki fiziksel sonuç iddiası çıkarılacak): "Ön çalışmada geçiş zamanı ölçüm
      yöntemi Wang vd. ile doğrulanmış, dört hedefte 174 yeni TESS geçiş zamanı ölçülmüş ve WASP-12 b için elde edilen −30,9 ± 0,9 ms/yıl
      değeri literatürle uyumlu bulunmuştur."
    - Hipotezler (madde 8) ön çalışma sonucuna değil literatüre dayandırılacak: H2 → Bouma vd. (2020), Winn ve Stefánsson (2025),
      Winn vd. (2009), Yang vd. (2025); H3 → Hagey vd. (2025), Kutluay vd. (2026), Adams vd. (2024). (Winn vd. 2009 kaynakçaya eklenecek.)
    - Kısım II (kılavuz) ön sonuçları ayrıntılı haliyle (yeni sayılarla) korur; orası forma girmiyor.

## C. 2026 çağrı belgelerinden (çağrı duyurusu, Başvuru İçeriği Bilgi Notu, kaynakça kuralları)

15. **Kaynakça ayrı TYBS adımı + DOI zorunlu.** "6. Ekler" bölümü boş kalır. Biçim: Soyad, A. Yıl. "Başlık", Dergi, Cilt, Sayfa. DOI —
    soyadına göre alfabetik. Tüm DOI'ler arXiv/Crossref'ten tek tek doğrulanacak.
16. **Metin içi atıf biçimi:** (Yee vd., 2020; Winn ve Stefánsson, 2025); anlatımda Wang vd. (2024).
17. **Her kaynak metinde atıf almalı:** Patra vd. (2017) gelgit formülüne; (Applegate, 1992; Watson ve Marsh, 2010) Applegate etkisinin ilk
    geçtiği yere; (Hagey vd., 2025; Kutluay vd., 2026) TrES-1 tartışmasına; Poddaný vd. (2010), Kokori vd. (2023), Yang vd. (2025) eklenecek.
18. **Kurum/marka öne çıkarılmayacak (çağrı 4.1.8):** "Google Colab" → "ücretsiz bulut tabanlı Python ortamı"; "GitHub/Zenodo" → "açık
    erişimli kod ve veri deposu"; Olanaklar'da "Atatürk Üniversitesi ..." → "Bölüm bilgisayar olanakları ...".
19. **Çevrim içi başvuru:** TYBS metin kutuları; tablolar "Tablo" düğmesiyle, şekiller "Resim Yükle" (.png) ile; "Proje Önerisini
    Önizle" ile kontrol. Word yalnız taslak. Son teslim: alan alan metin + PNG şekiller + tablo içerikleri.
20. **Bütçe:** en fazla 12.000 TL, başvurudan sonra değişmez; proje 0 TL — TYBS 0'a izin veriyor mu kontrol edilecek.
21. **Etik kurul:** gerekmez (arşiv verisi).
22. **Çalışma takvimi yeniden yazılacak** (bilgi notu: "iş paketlerinin toplam süresi proje süresinden uzun olamaz"; eski plan
    örtüşüyordu, toplam 17 ay). Art arda, toplam 11 ay; 12. ay sonuç raporu için boş. "Bursiyer" → "Proje yürütücüsü" (2209-A terimi).
    | 1.–2. ay | İP1: Arşiv ve literatür geçiş zamanı veri setinin oluşturulması; tüm zamanların BJD_TDB'ye dönüştürülmesi ve kaynak
      etiketlemesi | Proje yürütücüsü; akademik danışman | Her hedef için en az 70 zaman; tüm zamanlar BJD_TDB'de; zaman sistemi
      belirsiz kaynaklar ayrıca işaretli (%20) |
    | 3.–4. ay | İP2: TESS geçiş zamanlarının nihai ölçümü ve doğrulanması (kalite kontrolü, Wang vd. sektörüyle karşılaştırma, varsa
      yeni sektörlerin eklenmesi) | Proje yürütücüsü | Dört hedef için en az 150 nitelikli yeni zaman; ortanca belirsizlik en fazla 60 s;
      Wang vd. ile ortak geçişlerde ortanca fark en fazla 1σ (%20) |
    | 5.–6. ay | İP3: O−C diyagramları; hata çubuklarının ölçeklenmesi; doğrusal, kuadratik ve kübik modeller; BIC ile model seçimi |
      Proje yürütücüsü; akademik danışman | Dört hedef için dP/dt ± σ, ΔBIC ve "anlamlı değişim var/yok" kararı; WASP-12 b'de
      literatürle 2σ uyum (%25) |
    | 7.–11. ay | İP4: Arşiv radyal hızlarıyla Rømer testi; gelgit (Q′*), apsis, Applegate, üçüncü cisim ve kütle kaybı testleri; karar
      tablosu | Proje yürütücüsü; akademik danışman | Anlamlı değişim bulunan her hedef için altı etkinin her birine gerekçeli hüküm
      verilmiş karar tablosu (%35) |
    - Yöntem bölümündeki İP başlıklarındaki aylar da buna uyacak: İP1 (Ay 1–2), İP2 (Ay 3–4), İP3 (Ay 5–6), İP4 (Ay 7–11).
    - İP2 yöntem metni: ölçüm ön çalışmada yapıldığı için "nihai ölçüm ve doğrulama" olarak yazılacak.
    - 1.2 Hedef 3: "24 hücrelik" kalkacak → "Anlamlı değişim bulunan her hedef için altı fiziksel etkinin her birine önceden tanımlanmış
      ölçütlerle 'dışlandı / olası değil / olası / en olası / ayrılamadı' hükmü veren gerekçeli bir karar tablosu oluşturmak."
    - Madde 7'deki "24 hücrelik karar tablosunun tamamı gerekçeli (%35)" ifadesi bu maddeyle geçersiz.
    - Tarih sütunu: TYBS ay numarası mı tarih mi istiyor, başvuruda görülecek (süre sonuç ilanından başlar).
23. **Risk tablosu yeniden yazılacak** (8 satır). Değişenler: R1 "gerekirse" → "her veri grubu için" ölçekleme; R2 ön çalışmadan sonra
    "nitelikli zaman sayısı hedefin altında kalabilir" + B planı yöntem değişikliği ayrıntılı (sektör başına birleşik orta zaman; sonraki
    analizler aynı); R3'ten **WASP-10 yedek aday çıkarıldı** (8 TESS geçişi, K2'yi sağlamıyor; "değişim yok" zaten geçerli sonuç);
    R5'ten "ayrım için gereken RV duyarlılığı" çıkarıldı (madde 7 ile tutarlı); R6 marka adları genelleştirildi.
    Yeni riskler: "Veri arşivlerine erişim geçici olarak kesilebilir" → ayna sunucular, verilerin yerel saklanması;
    "İş paketlerinde gecikme" → ardışık İP'ler, 12. ay tampon, danışmanla düzenli görüşme.
    (Tam metin: sohbetteki tablo, 7 Kasım.)
24. **Araştırma Olanakları yeniden yazılacak:** "Atatürk Üniversitesi" ve "Google Colab" çıkacak; kütüphane satırı çıkacak (kaynaklar açık
    erişimli). Satırlar: (1) "Proje yürütücüsünün kişisel dizüstü bilgisayarı ile üniversite kütüphanesindeki bilgisayarlar ve internet
    erişimi" (kullanıcı teyit etti: kütüphanede bilgisayar var, bölümde yok — bölüm bilgisayarı YAZILMAYACAK); (2) açık erişimli veri arşivleri
    (MAST/TESS, VizieR, NASA Exoplanet Archive, DACE, ETD/VarAstro, ExoClock); (3) açık kaynak yazılımlar (Python, NumPy, Astropy,
    astroquery, batman, emcee). Madde 18'in olanaklar kısmı bununla değişti.
25. **Yaygın Etki tablosu yeniden yazılacak** (madde 3 ve madde 7'nin yaygın etki kısımları bununla değişti):
    - Bilimsel/Akademik: "Dört hedefin güncel O−C analizini ve fiziksel köken karar tablosunu içeren proje sonuç raporu. Sonuçların,
      yeterli görülmesi halinde danışmanla birlikte kısa bir makale (ör. Research Notes of the AAS) olarak sunulması hedeflenmektedir."
      (UAK, kongre, bildiri ve Turkish Journal örneği çıktı.)
    - Ekonomik/Ticari/Sosyal: "Dört hedefin yaklaşık 635 geçiş zamanını (174 yeni TESS zamanı dahil) BJD_TDB sisteminde içeren açık erişimli
      veri seti, analiz kodu ve dört hedef için güncel efemerisler; bu çıktılar gelecekteki geçiş gözlemlerinin planlanmasında
      kullanılabilecektir. Danışmanın uygun görmesi halinde bölüm öğrencilerine yönelik kısa bir O−C analizi tanıtım sunumu yapılması
      hedeflenmektedir."  (GitHub/Zenodo çıktı; "ETD/ExoClock ile efemeris paylaşımı" gerçekçi olmadığı için çıktı — bu veritabanları
      gözlemci zamanlarını kabul eder, dışarıdan efemeris almaz.)
    - Yeni Proje(ler): "Aynı yöntemin Wang vd. (2024)'nin diğer adaylarına genişletilmesiyle olası bir lisansüstü tez çalışmasına temel
      oluşturulması."

26. **5. Belirtmek İstediğiniz Diğer Konular yeniden yazılacak (yeni ön çalışma tanımına uygun):**
    - Giriş: "Aşağıdaki şekiller ve tablo, yöntem bölümünde özetlenen ön çalışmanın bulgularıdır. Ön çalışmada kullanılan kod ve veriler
      talep halinde sunulabilir." ("danışmanla paylaşılmıştır" ifadesi gerçek olmadığı sürece YAZILMAYACAK.)
    - Şekil 1 KALIR (yöntem kalibrasyonu); yeni yöntemle üretilmiş şekil kullanılacak (`sekiller/OC_WASP-12b.png`). Açıklama:
      "Şekil 1. WASP-12 b O−C diyagramı. Turuncu: literatür zamanları (Ivshina ve Winn, 2022); yeşil: Wang vd. (2024) ve Ivshina ve Winn
      (2022) TESS zamanları; kırmızı: bu çalışmada TESS sektör 71–72'den ölçülen 38 yeni geçiş zamanı. Mavi eğri en iyi kuadratik model
      (dP/dt = −30,9 ± 0,9 ms/yıl), kesikli çizgi sabit dönemli doğrusal modeldir. Sonuç literatür değeriyle (−29 ± 2 ms/yıl; Yee vd.,
      2020) uyumludur."
    - Şekil 2 KALIR (dört hedefte veri kapsamını ve ölçülen yeni zamanları gösterir) ama yorumsuz; birleşik panel yeni şekillerden yeniden
      yapılacak. Açıklama: "Şekil 2. Seçilen dört hedefin ön O−C diyagramları (renkler Şekil 1'deki gibidir). Ayrıntılı model seçimi ve
      fiziksel yorum proje kapsamında yapılacaktır." (Eski "dört hedefte de güçlü biçimde tercih" ve ΔBIC listesi ÇIKTI.)
    - Tablo 1 KALIR (örneklem seçimi). Düzeltmeler: WASP-10 satırındaki "(yedek aday)" kalkacak; açıklamaya "Tüm adaylar Wang vd. (2024)'nin
      LOOCV testini geçmiştir (K1)." eklenecek; K3 eşiği "σ_Rømer < Wang vd.'nin |dP/dt| değerinin üçte biri" diye açıkça yazılacak.
    - Tablo 2 (Rømer testi) ÇIKTI (madde 14).
    - Şekiller TYBS'ye "Resim Yükle" ile .png olarak, Tablo 1 "Tablo" düğmesiyle eklenecek.
27. **KAYNAKÇA — doğrulanmış son liste** (TÜBİTAK biçimi, soyadına göre alfabetik; DOI'ler Crossref/DataCite'tan tek tek doğrulandı, 7 Kasım).
    Metinde atıf alması gereken yeni kaynaklar: Ricker vd. (2015) → TESS'in ilk geçtiği yer; Akeson vd. (2013) ve Ochsenbein vd. (2000) →
    araştırma tasarımında NASA Exoplanet Archive ve VizieR; Astropy Collaboration (2022) → İP1 zaman dönüşümü ve İP4(d); Schwarz (1978) → İP3 BIC;
    Lomb (1976) ve Scargle (1982) → İP4(d) periyodogram; Kalkınma Planı ve 2030 Stratejisi → 1.1 son paragraf; DACE ve MAST → tasarım.
    Eski listeden "PSJ, 5, 163 (arXiv...)" gibi DOI'siz kısaltmalar tamamen kalkıyor.

    Adams, E. R. vd. 2024. "Doomed Worlds. I. No New Evidence for Orbital Decay in a Long-term Survey of 43 Ultrahot Jupiters", The Planetary Science Journal, 5, 163. https://doi.org/10.3847/psj/ad3e80
    Akeson, R. L. vd. 2013. "The NASA Exoplanet Archive: Data and Tools for Exoplanet Research", Publications of the Astronomical Society of the Pacific, 125, 989-999. https://doi.org/10.1086/672273
    Applegate, J. H. 1992. "A Mechanism for Orbital Period Modulation in Close Binaries", The Astrophysical Journal, 385, 621. https://doi.org/10.1086/170967
    Astropy Collaboration vd. 2022. "The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package", The Astrophysical Journal, 935, 167. https://doi.org/10.3847/1538-4357/ac7c74
    Baştürk, Ö. vd. 2025. "The Orbit of WASP-4 b is in Decay", arXiv ön baskı, 2506.15022. https://doi.org/10.48550/arXiv.2506.15022
    Bonomo, A. S. vd. 2017. "The GAPS Programme with HARPS-N at TNG. XIV. Investigating Giant Planet Migration History via Improved Eccentricity and Mass Determination for 231 Transiting Planets", Astronomy & Astrophysics, 602, A107. https://doi.org/10.1051/0004-6361/201629882
    Bouma, L. G. vd. 2020. "WASP-4 Is Accelerating toward the Earth", The Astrophysical Journal Letters, 893, L29. https://doi.org/10.3847/2041-8213/ab8563
    Cenevre Üniversitesi. "DACE – Data & Analysis Center for Exoplanets". https://dace.unige.ch, Son erişim tarihi: 7 Kasım 2026.
    Foreman-Mackey, D. vd. 2013. "emcee: The MCMC Hammer", Publications of the Astronomical Society of the Pacific, 125, 306-312. https://doi.org/10.1086/670067
    Hagey, S. R. vd. 2025. "TrES-1 b: A Case Study in Detecting Secular Evolution of Exoplanet Orbits", The Astronomical Journal, 170, 197. https://doi.org/10.3847/1538-3881/aded15
    Ivshina, E. S. ve Winn, J. N. 2022. "TESS Transit Timing of Hundreds of Hot Jupiters", The Astrophysical Journal Supplement Series, 259, 62. https://doi.org/10.3847/1538-4365/ac545b
    Knutson, H. A. vd. 2014. "Friends of Hot Jupiters. I. A Radial Velocity Search for Massive, Long-period Companions to Close-in Gas Giant Planets", The Astrophysical Journal, 785, 126. https://doi.org/10.1088/0004-637X/785/2/126
    Kokori, A. vd. 2023. "ExoClock Project. III. 450 New Exoplanet Ephemerides from Ground and Space Observations", The Astrophysical Journal Supplement Series, 265, 4. https://doi.org/10.3847/1538-4365/ac9da4
    Kreidberg, L. 2015. "batman: BAsic Transit Model cAlculatioN in Python", Publications of the Astronomical Society of the Pacific, 127, 1161-1165. https://doi.org/10.1086/683602
    Kutluay, A. C. vd. 2026. "Chasing the Tides: Searching for Orbital Decay Signatures in Transit Timing Data and Tidal Models for 20 Hot Jupiters", Publications of the Astronomical Society of the Pacific, 138, 024405. https://doi.org/10.1088/1538-3873/ae406a
    Lomb, N. R. 1976. "Least-squares Frequency Analysis of Unequally Spaced Data", Astrophysics and Space Science, 39, 447-462. https://doi.org/10.1007/BF00648343
    Ochsenbein, F., Bauer, P. ve Marcout, J. 2000. "The VizieR Database of Astronomical Catalogues", Astronomy and Astrophysics Supplement Series, 143, 23-32. https://doi.org/10.1051/aas:2000169
    Patra, K. C. vd. 2017. "The Apparently Decaying Orbit of WASP-12b", The Astronomical Journal, 154, 4. https://doi.org/10.3847/1538-3881/aa6d75
    Penev, K. vd. 2018. "Empirical Tidal Dissipation in Exoplanet Hosts from Tidal Spin-up", The Astronomical Journal, 155, 165. https://doi.org/10.3847/1538-3881/aaaf71
    Poddaný, S., Brát, L. ve Pejcha, O. 2010. "Exoplanet Transit Database. Reduction and Processing of the Photometric Data of Exoplanet Transits", New Astronomy, 15, 297-301. https://doi.org/10.1016/j.newast.2009.09.001
    Ricker, G. R. vd. 2015. "Transiting Exoplanet Survey Satellite", Journal of Astronomical Telescopes, Instruments, and Systems, 1, 014003. https://doi.org/10.1117/1.JATIS.1.1.014003
    Rothmeier, M. vd. 2025. "Doomed Worlds. II. Reassessing Suggestions of Orbital Decay for TrES-5 b", The Planetary Science Journal, 6, 292. https://doi.org/10.3847/PSJ/ae1b9c
    Scargle, J. D. 1982. "Studies in Astronomical Time Series Analysis. II. Statistical Aspects of Spectral Analysis of Unevenly Spaced Data", The Astrophysical Journal, 263, 835. https://doi.org/10.1086/160554
    Schwarz, G. 1978. "Estimating the Dimension of a Model", The Annals of Statistics, 6, 461-464. https://doi.org/10.1214/aos/1176344136
    Sodickson, N. ve Grunblatt, S. 2025. "In Search of Decay: An Analysis of Transit Times of Hot Jupiters in Main-sequence and Post-main-sequence Systems", The Astrophysical Journal, 993, 78. https://doi.org/10.3847/1538-4357/adfd60
    Space Telescope Science Institute. "Mikulski Archive for Space Telescopes (MAST)". https://archive.stsci.edu, Son erişim tarihi: 7 Kasım 2026.
    T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. "On İkinci Kalkınma Planı (2024-2028)". https://www.sbb.gov.tr/wp-content/uploads/2023/12/On-Ikinci-Kalkinma-Plani_2024-2028_11122023.pdf, Son erişim tarihi: 7 Kasım 2026.
    T.C. Sanayi ve Teknoloji Bakanlığı. "2030 Sanayi ve Teknoloji Stratejisi". https://www.sanayi.gov.tr/assets/img/popup-image/pdf/SanayiTeknolojiStratejisi2030.pdf, Son erişim tarihi: 7 Kasım 2026.
    Wang, W. vd. 2024. "Long-term Variations in the Orbital Period of Hot Jupiters from Transit-timing Analysis Using TESS Survey Data", The Astrophysical Journal Supplement Series, 270, 14. https://doi.org/10.3847/1538-4365/ad0847
    Watson, C. A. ve Marsh, T. R. 2010. "Orbital Period Variations of Hot Jupiters Caused by the Applegate Effect", Monthly Notices of the Royal Astronomical Society, 405, 2037. https://doi.org/10.1111/j.1365-2966.2010.16602.x
    Winn, J. N. vd. 2009. "HAT-P-7: A Retrograde or Polar Orbit, and a Third Body", The Astrophysical Journal Letters, 703, L99-L103. https://doi.org/10.1088/0004-637X/703/2/L99
    Winn, J. N. ve Stefánsson, G. 2025. "Orbital Decay Candidates Reconsidered: WASP-4 b Is Not Decaying and Kepler-1658 b Is Not a Planet", The Planetary Science Journal, 6, 300. https://doi.org/10.3847/PSJ/ae21db
    Yang, E., Su, Y. ve Winn, J. N. 2025. "A Third Star in the HAT-P-7 System and a New Dynamical Pathway to Misaligned Hot Jupiters", The Astrophysical Journal, 986, 117. https://doi.org/10.3847/1538-4357/add5f7
    Yee, S. W. vd. 2020. "The Orbit of WASP-12b Is Decaying", The Astrophysical Journal Letters, 888, L5. https://doi.org/10.3847/2041-8213/ab5c16

28. **"K1/K2/K3" kısaltmaları kalkacak** (hakem Tablo 1'de ne demek olduğunu anlayamaz; tanımları sayfalarca önce Yöntem'de).
    - Tablo 1 "Sonuç" sütunu: "K2 sağlanmıyor" → "Elendi: TESS geçiş sayısı 30'dan az"; KELT-16 → "Elendi: arşivde RV verisi yok";
      TrES-5, WASP-46 → "Elendi: arşiv RV verisi yetersiz (σ_Rømer > |dP/dt|/3)"; "Seçildi" aynen.
    - Tablo 1 açıklaması (tablonun ne olduğu ve her sütunun kaynağı açıkça):
      "Tablo 1. Bu çalışmada oluşturulan hedef seçim tablosu. Satırlar, Wang vd. (2024)'nin dönem değişimi bildirdiği 26 adaydan, aynı
      çalışmanın LOOCV testini geçen 14'üdür (Wang vd., 2024, Tablo 3). Sütunların kaynakları: |dP/dt|/σ (Wang vd.'nin bildirdiği dönem
      değişim hızının belirsizliğine oranı) ve TESS geçiş sayısı Wang vd. (2024)'nin VizieR'de yayımlanan tablolarından (J/ApJS/270/14)
      alınmıştır. σ_Rømer (uzak bir eşlikçinin ivmesinden kaynaklanabilecek dönem değişiminin arşiv radyal hız verisiyle öngörülebildiği
      belirsizlik, ms/yıl) bu çalışmada, yayımlanmış radyal hız ölçümlerinden (Knutson vd., 2014; Bonomo vd., 2017; Bouma vd., 2020;
      DACE arşivi) hesaplanmış ve her aday için en hassas veri seti kullanılmıştır. Seçim ölçütleri: (1) TESS geçiş sayısı en az 30;
      (2) σ_Rømer, Wang vd.'nin bildirdiği |dP/dt| değerinin üçte birinden küçük. '–': ilk ölçütte elendiği için hesaplanmadı ya da
      arşivde radyal hız verisi yok."
    - Yöntem/Örneklem seçimi: "(K1)", "(K2)", "(K3)" → "(i) LOOCV ölçütü", "(ii) TESS verisi ölçütü", "(iii) radyal hız verisi ölçütü".
    - `kod/secim_tablosu.py` çıktısındaki etiketler de aynı açık ifadelere çevrilecek (tablo ile kod tutarlı olsun).

(Yapay zekâ kullanım beyanı kullanıcıya ait; bu listede yer almıyor.)
