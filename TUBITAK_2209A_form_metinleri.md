> TÜBİTAK 2209-A (2026) araştırma önerisi — son metin. TYBS'deki ilgili kutulara bölüm bölüm yapıştır; Tablo 1'i TYBS'nin "Tablo"
> düğmesiyle ekle. Kaynaklar TYBS'de ayrı "Kaynakça" adımına girilir. Word dosyası aynı metnin taslak halidir.

# A. Genel Bilgiler

| Alan | Değer |
|---|---|
| Başvuru Sahibinin Adı Soyadı | İdris Avlar |
| Araştırma Önerisinin Başlığı | Sıcak Jüpiterlerde Yörünge Dönemi Değişimlerinin O−C Analiziyle İncelenmesi ve Fiziksel Kökenlerinin Belirlenmesi |
| Danışmanın Adı Soyadı | Hüseyin Er |
| Araştırmanın Yürütüleceği Kurum | Atatürk Üniversitesi, Fen Fakültesi, Astronomi ve Uzay Bilimleri Bölümü |

# Özet

Yıldızlarına çok yakın yörüngelerde dolanan sıcak Jüpiterlerin yörünge dönemlerinin zamanla değişip değişmediği, yıldız–gezegen gelgit etkileşimini doğrudan sınayabilen az sayıdaki gözlemsel yoldan biridir. Wang vd. (2024), TESS verisiyle 326 sıcak Jüpiteri inceleyerek uzun dönemli dönem değişimi gösteren 26 aday bildirmiş; bunlardan 14'ü, tek bir ölçümün çıkarılmasına karşı sonucun dayanıklılığını sınayan “birini dışarıda bırak çapraz doğrulama” (LOOCV) testini geçmiştir. Ancak geçiş zamanlarında görülen parabolik bir değişim yalnızca gelgit kaynaklı yörünge bozulmasından değil; apsis hareketi, uzak bir üçüncü cismin ışık-yolu (Rømer) etkisi ya da kütle çekimsel etkisi, Applegate mekanizması, kütle kaybı ve veri hatalarından da kaynaklanabilir. Bu projede LOOCV testini geçen 14 aday, TESS veri yeterliliği ve fiziksel kökenin ayırt edilebilmesi için gerekli arşiv radyal hız verisinin yeterliliği ölçütleriyle elenmiş; WASP-12 b, WASP-4 b, HAT-P-7 b ve TrES-1 b hedef olarak seçilmiştir. Her hedef için literatür ve katalog geçiş zamanları derlenecek, tümü BJD_TDB zaman sistemine dönüştürülecek ve Wang vd. tarafından kullanılmamış yeni TESS sektörlerinden orta geçiş zamanları ölçülecektir. Gözlenen ve doğrusal efemerisle hesaplanan zamanların farkı olan O−C diyagramlarına doğrusal, kuadratik ve kübik modeller uydurulacak; dönem değişiminin varlığı, değişim hızının anlamlılığı ve Bayes Bilgi Ölçütü ile sınanacaktır. Anlamlı değişim bulunan hedeflerde, yalnızca zamanlamayla ayırt edilemeyen gelgit ve Rømer etkileri, yayımlanmış arşiv radyal hız ölçümlerinden öngörülen dönem değişimiyle karşılaştırılarak ayrılacak; diğer etkiler gelgit kalite faktörü, örtülme zamanları, dışmerkezlik, yıldız etkinliği, periyodogram ve Roche sınırı testleriyle değerlendirilecektir. Projede yeni gözlem yapılmayacak; tüm veriler açık arşivlerden sağlanacaktır. Ön çalışmada 14 adayın TESS ve radyal hız verilerinin yeterliliği incelenerek hedef seçimi yapılmıştır. Bütçe gerektirmeyen 12 aylık projenin çıktıları dört hedef için güncel efemerisler, fiziksel köken hükümleri ve açık erişimli veri seti ile analiz kodudur; sonuçların danışmanla birlikte kısa bir makale olarak paylaşılması hedeflenmektedir.

**Anahtar Kelimeler:** Sıcak Jüpiter, geçiş zamanlaması, O−C diyagramı, yörünge bozulması, TESS

# 1. Araştırma Önerisinin Bilimsel Niteliği

## 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Sıcak Jüpiterler, kütleleri Jüpiter mertebesinde olan ve yıldızlarının etrafında birkaç günde dolanan gezegenlerdir. Yıldızlarına çok yakın oldukları için yıldızda gelgit kabarıklıkları oluştururlar. Yıldızın kendi ekseni etrafındaki dönmesi yörünge hareketinden yavaş olduğunda bu kabarıklık gezegeni geriye doğru çeker; gezegen açısal momentum kaybederek içeri doğru sarmallanır ve yörünge dönemi kısalır. Bu sürecin hızı, yıldızın gelgit enerjisini ne kadar verimli soğurduğunu gösteren değiştirilmiş gelgit kalite faktörüne (Q′*) bağlıdır. Kuramsal ve görgül tahminler Q′* için birkaç mertebelik bir aralık verdiğinden (Penev vd., 2018), dönem değişiminin doğrudan ölçümü yıldız içi fiziği sınamanın ender yollarından biridir.

Dönem değişimi, geçiş zamanlarının gözlenen (O) ve sabit dönemle hesaplanan (C) değerleri arasındaki farkın zamana karşı çizildiği O−C diyagramıyla incelenir. Dönem sabit bir hızla değişiyorsa O−C bir parabol çizer. Bugüne kadar ikna edici biçimde doğrulanmış tek örnek WASP-12 b'dir; geçiş, örtülme ve radyal hız verileri birlikte kullanılarak apsis hareketi ve ivme açıklamaları dışlanmış, dönem değişim hızı yaklaşık −29 ms/yıl ve Q′* ≈ 1,8×10⁵ bulunmuştur (Patra vd., 2017; Yee vd., 2020; Winn ve Stefánsson, 2025). Wang vd. (2024), 326 sıcak Jüpiterin TESS (Ricker vd., 2015) geçişlerini literatür zamanlarıyla birleştirerek 26 dönem değişimi adayı bildirmiş, bunlardan 12'sinin sonucunun tek bir ölçümün çıkarılmasıyla kaybolduğunu göstermiş ve gelgit dışında apsis hareketi, Rømer etkisi ve yıldızın manyetik etkinlik döngüsüne bağlı Applegate etkisinin (Applegate, 1992; Watson ve Marsh, 2010) de katkı verebileceğini belirtmiş; ancak adayların fiziksel kökenini sistem sistem sınamamıştır.

Literatürdeki temel sorun, O−C diyagramındaki parabolün tek başına kökenini göstermemesidir. Uzak bir eşlikçi nedeniyle bakış doğrultusunda sabit ivmelenen bir sistemde ışığın yol süresi değişir ve geçiş zamanları gelgit bozulmasıyla matematiksel olarak aynı kuadratik izi bırakır (Bouma vd., 2020). Nitekim WASP-4 b için aynı dönem değişimi bir çalışmada gelgit bozulmasıyla (Baştürk vd., 2025), başka bir çalışmada yaklaşık 7 Jüpiter kütleli uzak bir eşlikçinin ışık-yolu etkisiyle açıklanmıştır (Winn ve Stefánsson, 2025). HAT-P-7 b'de radyal hızlarda uzun dönemli bir eğilim bulunmuş (Winn vd., 2009) ve geçiş zamanlaması ile radyal hızların birlikte kullanılmasıyla yaklaşık 32 AB uzaklıkta eksantrik yörüngeli bir yıldız eşlikçi önerilmiştir (Yang vd., 2025). TrES-1 b için ise farklı çalışmalar birbiriyle uyumsuz dönem değişim hızları ve yorumlar ortaya koymuştur (Adams vd., 2024; Hagey vd., 2025; Kutluay vd., 2026). Ayrıca literatür zamanlarındaki hatalar, zaman sistemi karışıklıkları, gerçekçi olmayan küçük hata çubukları ve tek tek aykırı ölçümler sahte sinyaller üretebilmektedir (Adams vd., 2024; Rothmeier vd., 2025; Sodickson ve Grunblatt, 2025). Bu nedenle adayların güncel veriyle yeniden sınanması ve olası her fiziksel etkinin aynı yöntemle sistematik biçimde değerlendirilmesi gerekmektedir.

Bu proje, Wang vd. (2024)'nin LOOCV testini geçen 14 adayından önceden tanımlanmış ölçütlerle seçilen dört sıcak Jüpiterde (WASP-12 b, WASP-4 b, HAT-P-7 b, TrES-1 b) bu boşluğu doldurmayı amaçlamaktadır. Hedefler, TESS veri yeterliliği ve arşiv radyal hız verisinin yeterliliği ölçütleriyle seçilmiştir (bkz. Yöntem, Tablo 1). Seçilen hedefler birbirini tamamlayan dört durumu temsil etmektedir: WASP-12 b doğrulanmış gelgit bozulmasıyla yöntemin kalibrasyonunu, WASP-4 b gelgit ile ışık-yolu etkisinin tartışıldığı bir vakayı, HAT-P-7 b gelgitle açıklanamayan bir dönem artışını, TrES-1 b ise bildirilen dönem kısalmasının literatür zamanlarının güvenilirliğine bağlı olup olmadığının sınandığı bir vakayı. Projenin özgün yanları şunlardır: (i) Wang vd. sonrasında yayımlanan TESS sektörlerinden ölçülecek yeni geçiş zamanlarıyla zaman tabanı yaklaşık 2–6 yıl uzatılacaktır; (ii) gelgit etkileşimi, apsis hareketi, Rømer etkisi, üçüncü cismin dinamik etkisi, Applegate etkisi ve kütle kaybı her hedef için önceden yazılmış bir karar ağacıyla değerlendirilecektir; (iii) gelgit ile Rømer etkisi, farklı arşivlerde yayımlanmış radyal hız ölçümlerinden öngörülen dönem değişimiyle karşılaştırılarak ayrılacaktır.

**Araştırma sorusu:** Wang vd. (2024)'nin LOOCV testini geçen adaylardan seçilen dört sıcak Jüpiterin yörünge dönemleri güncel TESS verisiyle anlamlı biçimde değişmekte midir; değişiyorsa bu değişimden gelgit etkileşimi, apsis hareketi, Rømer etkisi, üçüncü cisim, Applegate etkisi ve kütle kaybından hangisi sorumludur?

**Hipotezler:**

H1: WASP-12 b'de güncel TESS verisiyle bulunan dönem değişim hızı literatür değeriyle (Yee vd., 2020) 2σ içinde uyumludur ve arşiv radyal hızlarından öngörülen Rømer katkısı bu değişimi açıklayamaz (gelgit kökenli bozulma).

H2: WASP-4 b ve HAT-P-7 b'deki dönem değişimlerinin önemli bir kısmı, arşiv radyal hız ölçümlerinin gösterdiği ivmeden kaynaklanan ışık-yolu (Rømer) etkisiyle açıklanır.

H3: TrES-1 b'de bildirilen dönem kısalması, literatür zamanlarının belirsizlikleri gerçekçi biçimde değerlendirildiğinde ve yeni TESS zamanları eklendiğinde istatistiksel olarak anlamlı değildir.

Proje, On İkinci Kalkınma Planı'nın (2024–2028) temel bilimlere özel önem verilmesini ve uzay araştırmalarını kritik alanlar arasında sayan hedefiyle (madde 270) ve genç nesillerin uzay alanında çalışmaya teşvik edilerek uzay araştırmalarının yaygınlaştırılmasını öngören hedefiyle (madde 271) doğrudan ilişkilidir (T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı, 2023). 2030 Sanayi ve Teknoloji Stratejisi de TÜBİTAK araştırma desteklerinin astronomi dahil temel bilimlerde bilgi üretimini artıracak şekilde yaygınlaştırılmasını öngörmektedir (T.C. Sanayi ve Teknoloji Bakanlığı, 2025). Proje, uzay görevi verilerinin (TESS) işlenmesi ve yorumlanması konusunda lisans düzeyinde araştırmacı yetiştirilmesine katkı sağlayarak bu hedeflere hizmet etmektedir.

## 1.2. Amaç ve Hedefler

Projenin amacı, Wang vd. (2024)'nin LOOCV testini geçen 14 sıcak Jüpiter adayından önceden tanımlanmış ölçütlerle seçilen dört hedefte yörünge dönemi değişiminin varlığını güncel TESS ve katalog verileriyle sınamak ve değişim varsa fiziksel kökenini belirlemektir.

**Hedef 1 (Veri seti):** Dört hedefin her biri için en az 70 geçiş zamanından oluşan, tümü BJD_TDB zaman sistemine dönüştürülmüş ve kaynakları etiketlenmiş bir zaman tablosu oluşturmak; Wang vd. sonrası TESS sektörlerinden toplam en az 150 yeni orta geçiş zamanını, ortanca belirsizliği 60 saniyeyi aşmayacak biçimde ölçmek.

**Hedef 2 (Dönem değişimi):** Her hedef için O−C diyagramını çizmek; doğrusal, kuadratik ve kübik modelleri karşılaştırarak dönem değişim hızını (dP/dt) belirsizliğiyle ve ΔBIC değeriyle raporlamak ve her hedef için “anlamlı değişim var/yok” kararını vermek. Yöntemin doğruluğu, WASP-12 b için literatür değeriyle 2σ içinde uyumla gösterilecektir.

**Hedef 3 (Fiziksel köken):** Anlamlı değişim bulunan her hedef için altı fiziksel etkinin her birine (gelgit, apsis hareketi, Rømer, üçüncü cisim, Applegate, kütle kaybı) önceden tanımlanmış ölçütlerle “dışlandı / olası değil / olası / en olası / ayrılamadı” hükmü veren gerekçeli bir karar tablosu oluşturmak.

**Hedef 4 (Efemeris):** Dört hedef için güncel efemerisleri (T0, P ve varsa dP/dt) yayımlamak.

# 2. Yöntem

**Araştırma tasarımı.** Proje, açık arşiv verisine dayanan, hipotez sınayan gözlemsel bir çalışmadır. Yeni teleskop ya da tayf gözlemi yapılmayacak; tüm veriler TESS ışık eğrileri için MAST, katalog tabloları için VizieR (Ochsenbein vd., 2000), sistem parametreleri için NASA Exoplanet Archive (Akeson vd., 2013), radyal hızlar için DACE ve yayımlanmış makale tabloları, yer gözlemi geçiş zamanları için ETD/VarAstro (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023) veritabanlarından sağlanacaktır. Bağımsız değişken geçiş epoku (E), bağımlı değişken orta geçiş zamanı ve ondan türetilen O−C değeridir; türetilen temel büyüklük dönem değişim hızıdır (dP/dt). Kontrol edilen değişkenler zaman sistemi, ölçüm belirsizliği ve veri kaynağıdır.

**Örneklem seçimi.** Hedefler, bu projenin kendi O−C sonuçlarından bağımsız üç ölçütle seçilmiştir (Tablo 1). (i) LOOCV ölçütü: Wang vd. (2024)'nin LOOCV testini geçmiş olmak (14 aday). (ii) TESS verisi ölçütü: Wang vd. tarafından raporlanan TESS geçiş zamanı sayısının en az 30 olması; adaylar arasındaki en kısa yörünge döneminde bile bu sayı en az iki TESS sektörüne yayılan veri anlamına gelir (7 aday). (iii) Radyal hız verisi ölçütü: Fiziksel kökenin belirlenebilmesi için, yayımlanmış arşiv radyal hız ölçümlerinden öngörülen Rømer katkısının belirsizliğinin Wang vd.'nin raporladığı |dP/dt| değerinin üçte birinden küçük olması (4 aday: WASP-12 b, WASP-4 b, HAT-P-7 b, TrES-1 b).

**İP1 – Zaman tablosunun oluşturulması (Ay 1–2).** Geçiş zamanları Ivshina ve Winn (2022) veritabanından, Wang vd. (2024)'nin TESS ölçümlerinden, ETD/VarAstro (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023) veritabanlarından ve hedefe özel makalelerden (Yee vd., 2020; Bouma vd., 2020; Baştürk vd., 2025; Hagey vd., 2025) derlenecektir. Her zamanın sistemi makalesinden kontrol edilecek, HJD ve BJD_UTC zamanları Astropy (Astropy Collaboration vd., 2022) ile BJD_TDB'ye dönüştürülecektir. Zaman sistemi makalesinden belirlenemeyen zamanlar işaretlenecek; analiz bu zamanlar dahil ve hariç olmak üzere iki kez yapılarak sonucun bu zamanlara duyarlılığı raporlanacaktır. ETD verilerinde yalnızca yüksek kalite notlu tam geçişler kullanılacaktır. Epok numarasının kesirli kısmı 0,02'yi aşan zamanlar ayrıca kontrol edilecektir.

**İP2 – Yeni TESS zamanlarının ölçülmesi (Ay 3–4).** Wang vd. sonrası SPOC 2 dakikalık ışık eğrileri MAST'tan indirilecek, kalite bayraklı noktalar atılarak normalize edilecektir. Tüm geçişler katlanarak geçiş şekli (Rp/R*, a/R*, eğiklik) batman modeliyle (Kreidberg, 2015) belirlenecek; ardından her geçiş, yalnızca orta zaman ve yerel taban çizgisi serbest bırakılarak uydurulacak ve orta zamanın belirsizliği emcee ile MCMC örneklemesinden (Foreman-Mackey vd., 2013) elde edilecektir. Kenar kararması katsayıları sabit tutulacaktır; geçiş biçimi simetrik olduğundan orta zaman ölçümüne etkisi ihmal edilebilir. Kısmi geçişler kullanılmayacaktır. Yöntem, Wang vd.'nin ölçtüğü sektörlerden biri yeniden ölçülerek ortak geçişlerde karşılaştırılacak ve doğrulanacaktır.

**İP3 – O−C analizi ve model seçimi (Ay 5–6).** Doğrusal (T = T0 + P·E), kuadratik (T = T0 + P·E + ½·(dP/dE)·E²) ve kübik efemerisler ağırlıklı en küçük karelerle uydurulacak, dP/dt = (1/P)(dP/dE) hesaplanacaktır. Aykırı noktalar 5σ yinelemeli kırpmayla belirlenecektir. Literatür ve TESS zamanlarının hata çubukları, her grubun kuadratik model artıklarından hesaplanan indirgenmiş χ² değeri 1 olacak şekilde (yalnızca büyütülerek) ölçeklenecektir. Model seçimi Bayes Bilgi Ölçütü (BIC = χ² + k·ln n; Schwarz, 1978) ile yapılacak; Wang vd. (2024) ile aynı ölçütler (|dP/dt|/σ ≥ 3 ve ΔBIC > 10) uygulanacaktır. Kübik model, dönem değişim hızının zamanla sabit olup olmadığını sınamak için kullanılacaktır.

**İP4 – Fiziksel kökenin belirlenmesi (Ay 7–11).** (a) Rømer etkisi: Yayımlanmış arşiv radyal hızlarına (Knutson vd., 2014; Bonomo vd., 2017; Bouma vd., 2020; Yee vd., 2020; DACE) her alet için ayrı sıfır noktası, gezegenin dairesel yörünge sinyali ve doğrusal eğilim uydurulacaktır. Geçiş sırasında alınan ölçümler (Rossiter–McLaughlin etkisi) çıkarılacak, hatalar yıldız kaynaklı saçılmayı içerecek şekilde ölçeklenecek, doğrusal eğilim yetersiz kalırsa ikinci dereceden terim eklenecektir. Rømer etkisinin öngördüğü dönem değişimi dP/dt = P·(dv/dt)/c ile hesaplanıp O−C sonucuyla karşılaştırılacaktır (fark < 2σ: Rømer açıklayabilir; 2–3σ: kısmen; > 3σ: Rømer tek başına açıklayamaz). Sonucun kullanılan radyal hız veri setine duyarlılığı ayrıca raporlanacaktır. (b) Gelgit: NASA Exoplanet Archive parametreleriyle dP/dt = −(27π/2Q′*)(Mp/M*)(R*/a)⁵ bağıntısından (Patra vd., 2017) gereken Q′* hesaplanacak ve kuramsal aralıkla karşılaştırılacaktır; yıldızın yörüngeden yavaş döndüğü sistemlerde gelgit dönemi yalnızca kısaltabileceğinden, dönemi uzayan hedefte gelgit dışlanır (Wang vd., 2024). (c) Apsis hareketi: dışmerkezlik üst sınırından beklenen genlik (≈ eP/π) hesaplanacak; örtülme zamanlarının bulunduğu WASP-12 b'de (Yee vd., 2020) örtülmelerin geçişlere göre kayma yönü sınanacaktır. (d) Applegate etkisi ve üçüncü cismin dinamik etkisi: kuadratik model artıklarında Lomb–Scargle periyodogramıyla (Lomb, 1976; Scargle, 1982; Astropy Collaboration vd., 2022) periyodik sinyal aranacak (yanlış alarm olasılığı < 0,01; gözlem mevsiminden kaynaklanan yaklaşık bir yıllık tepeler sinyal sayılmayacak), kübik modelle eğriliğin sabitliği sınanacak, yıldız etkinliği literatürden değerlendirilecektir. (e) Kütle kaybı: a/a_Roche oranı hesaplanacaktır. Her etki için hüküm önceden yazılmış karar ağacıyla verilecektir.

**Ön çalışma.** Ön çalışmada Wang vd. (2024)'nin LOOCV testini geçen 14 adayın, projenin yürütülebilmesi için gereken verilerinin yeterliliği incelenmiştir. Her aday için Wang vd.'nin TESS geçiş zamanı sayısı belirlenmiş; yayımlanmış radyal hız ölçümleri (Knutson vd., 2014; Bonomo vd., 2017; Oberst vd., 2017; Bouma vd., 2020; DACE) derlenerek Rømer katkısının hangi duyarlılıkla öngörülebileceği hesaplanmıştır. Bu inceleme sonucunda seçim ölçütlerini sağlayan dört hedef belirlenmiş (Tablo 1) ve dört hedefin geçiş zamanlarının ve Wang vd. sonrası TESS ışık eğrilerinin açık arşivlerde erişilebilir olduğu doğrulanmıştır. Yöntem adımları çalışma takvimindeki İP1–İP4 ile birebir ilişkilidir.

# 3. Proje Yönetimi

## 3.1. Çalışma Takvimi

| Tarih Aralığı | Faaliyetler | Kim(ler) | Başarı Ölçütü ve Katkısı |
|---|---|---|---|
| 1.–2. ay | İP1: Arşiv ve literatür geçiş zamanı veri setinin oluşturulması; tüm zamanların BJD_TDB'ye dönüştürülmesi ve kaynak etiketlemesi | İdris Avlar (proje yürütücüsü; zaman sistemi dönüşümleri); Bahar Cayib (proje ortağı; literatür ve arşiv zamanlarının derlenmesi); Hüseyin Er (akademik danışman) | Her hedef için en az 70 zaman; tüm zamanlar BJD_TDB'de; zaman sistemi belirsiz kaynaklar ayrıca işaretli (%20) |
| 3.–4. ay | İP2: Wang vd. sonrası TESS sektörlerinden orta geçiş zamanlarının ölçülmesi ve Wang vd.'nin ölçtüğü bir sektörün yeniden ölçülerek yöntemin doğrulanması | İdris Avlar (proje yürütücüsü; ışık eğrisi modellemesi ve zaman ölçümü); Bahar Cayib (proje ortağı; TESS verilerinin indirilmesi ve geçişlerin görsel kontrolü) | Dört hedef için en az 150 yeni zaman; ortanca belirsizlik en fazla 60 s; Wang vd. ile ortak geçişlerde ortanca fark en fazla 1σ (%20) |
| 5.–6. ay | İP3: O−C diyagramları; hata çubuklarının ölçeklenmesi; doğrusal, kuadratik ve kübik modeller; BIC ile model seçimi | İdris Avlar (proje yürütücüsü; model uydurma ve istatistiksel karşılaştırma); Bahar Cayib (proje ortağı; O−C diyagramlarının hazırlanması ve veri kontrolü); Hüseyin Er (akademik danışman) | Dört hedef için dP/dt ± σ, ΔBIC ve “anlamlı değişim var/yok” kararı; WASP-12 b'de literatürle 2σ uyum (%25) |
| 7.–11. ay | İP4: Arşiv radyal hızlarıyla Rømer testi; gelgit (Q′*), apsis, Applegate, üçüncü cisim ve kütle kaybı testleri; karar tablosu | İdris Avlar (proje yürütücüsü; fiziksel testler ve karar tablosu); Bahar Cayib (proje ortağı; radyal hız verilerinin ve yıldız/gezegen parametrelerinin derlenmesi); Hüseyin Er (akademik danışman) | Anlamlı değişim bulunan her hedef için altı etkinin her birine gerekçeli hüküm verilmiş karar tablosu (%35) |

[Tarih sütunu: TYBS ay numarası yerine tarih isterse, sonuçların ilan tarihine göre gg/aa/yyyy olarak yaz. 12. ay sonuç raporu için boş bırakılmıştır.]

## 3.2. Risk Yönetimi

| En Önemli Riskler | Alınacak Tedbirler (B Planı) |
|---|---|
| Literatür zamanlarında zaman sistemi belirsizliği veya gerçekçi olmayan küçük hata çubukları sahte sinyal üretebilir. | Her kaynağın zaman sistemi makalesinden kontrol edilecek; belirlenemeyen zamanlarla ve onlarsız iki ayrı analiz yapılacak; hata çubukları her veri grubu için indirgenmiş χ² ile ölçeklenecektir. |
| Yeni TESS sektörlerinden bazı geçişlerin zamanı ölçülemeyebilir ve nitelikli zaman sayısı hedefin altında kalabilir (veri boşluğu, düşük sinyal-gürültü oranı). | Tek tek ölçülemeyen geçişler için sektördeki tüm geçişler birlikte uydurularak sektör başına tek bir orta geçiş zamanı elde edilecektir; yöntem değişikliği yalnızca bu adımla sınırlıdır, sonraki analizler aynı kalır. En kötü durumda Wang vd. ve Ivshina ve Winn TESS zamanlarıyla devam edilecektir. |
| Bir hedefte güncel veriyle anlamlı dönem değişimi bulunmayabilir. | Bu durum araştırma sorusunun (“değişim var mı?”) bir cevabı olarak raporlanacak ve güncel sabit dönemli efemeris verilecektir; fiziksel köken analizi anlamlı değişim bulunan hedeflerle sürdürülecektir. |
| Farklı arşivlerdeki radyal hız veri setleri, alet sıfır noktası farkları nedeniyle farklı eğimler verebilir. | Tüm yayımlanmış ölçümler alet başına ayrı sıfır noktasıyla birlikte uydurulacak ve sonucun veri setine duyarlılığı raporlanacaktır; yeterli duyarlılık sağlanamazsa literatürde yayımlanmış eğimler ve radyal hız gerektirmeyen testler (Q′*, eğrilik, periyodogram, Roche) kullanılacaktır. |
| Gelgit ve Rømer etkileri mevcut veriyle ayrılamayabilir. | İki senaryonun da büyüklüğü verilecek ve “ayrılamadı” hükmü gerekçesiyle raporlanacaktır. |
| Veri arşivlerine erişim geçici olarak kesilebilir. | Aynı katalogların ayna sunucuları kullanılacak; indirilen tüm veriler yerel olarak saklanacaktır. |
| İş paketlerinde gecikme yaşanabilir. | İş paketleri ardışık planlanmış ve 12. ay tampon olarak bırakılmıştır; ilerleme akademik danışmanla düzenli görüşmelerle izlenecektir. |
| Yazılım veya bilgisayar arızası. | Tüm kod ve veriler sürüm kontrolüyle çevrim içi bir depoda yedeklenecek; analizler ücretsiz bulut tabanlı bir Python ortamında da çalışabilecek şekilde hazırlanacaktır. |

## 3.3. Araştırma Olanakları

| Kuruluşta Bulunan Altyapı/Ekipman Türü, Modeli | Projede Kullanım Amacı |
|---|---|
| Proje yürütücüsünün kişisel dizüstü bilgisayarı ile üniversite kütüphanesindeki bilgisayarlar ve internet erişimi | Veri indirme, ışık eğrisi analizi, O−C ve radyal hız analizleri |
| Açık erişimli veri arşivleri: MAST (TESS), VizieR, NASA Exoplanet Archive, DACE, ETD/VarAstro, ExoClock | Geçiş zamanları, ışık eğrileri, sistem parametreleri ve radyal hız verileri |
| Açık kaynak yazılımlar: Python, NumPy, Astropy, astroquery, batman, emcee | Tüm analizlerin ücretsiz ve yeniden üretilebilir biçimde yapılması |

# 4. Araştırma Önerisinin Yaygın Etkisi

| Çıktı, Etki ve Kazanımlar | Öngörülen Çıktı(lar), Etki(ler) ve Kazanım(lar) |
|---|---|
| Bilimsel/Akademik Çıktılar | Dört hedefin güncel O−C analizini ve fiziksel köken karar tablosunu içeren proje sonuç raporu. Sonuçların, yeterli görülmesi halinde danışmanla birlikte kısa bir makale olarak sunulması hedeflenmektedir. |
| Ekonomik/Ticari/Sosyal Çıktılar | Dört hedefin tüm geçiş zamanlarını (yeni TESS zamanları dahil) BJD_TDB sisteminde içeren açık erişimli veri seti, analiz kodu ve dört hedef için güncel efemerisler; bu çıktılar gelecekteki geçiş gözlemlerinin planlanmasında kullanılabilecektir. Danışmanın uygun görmesi halinde bölüm öğrencilerine yönelik kısa bir O−C analizi tanıtım sunumu yapılması hedeflenmektedir. |
| Yeni Proje(ler) Oluşturmasına Yönelik Çıktılar | Aynı yöntemin Wang vd. (2024)'nin diğer adaylarına genişletilmesiyle olası bir lisansüstü tez çalışmasına temel oluşturulması. |

# 5. Belirtmek İstediğiniz Diğer Konular

Aşağıdaki tablo, yöntem bölümünde özetlenen ön çalışmanın sonucudur.

**Tablo 1.** Bu çalışmada oluşturulan hedef seçim tablosu. Satırlar, Wang vd. (2024)'nin dönem değişimi bildirdiği 26 adaydan, aynı çalışmanın LOOCV testini geçen 14'üdür (Wang vd., 2024, Tablo 3). Sütunların kaynakları: |dP/dt|/σ (Wang vd.'nin bildirdiği dönem değişim hızının belirsizliğine oranı) ve TESS geçiş sayısı Wang vd. (2024)'nin VizieR'de yayımlanan tablolarından (J/ApJS/270/14) alınmıştır. σ_Rømer (uzak bir eşlikçinin ivmesinden kaynaklanabilecek dönem değişiminin arşiv radyal hız verisiyle öngörülebildiği belirsizlik, ms/yıl) bu çalışmada, yayımlanmış radyal hız ölçümlerinden (Knutson vd., 2014; Bonomo vd., 2017; Oberst vd., 2017; Bouma vd., 2020; DACE) hesaplanmış ve her aday için en hassas veri seti kullanılmıştır. Seçim ölçütleri: (1) TESS geçiş sayısı en az 30; (2) σ_Rømer, Wang vd.'nin bildirdiği |dP/dt| değerinin üçte birinden (“Eşik” sütunu) küçük. “–”: ilk ölçütte elendiği için hesaplanmadı.

| Aday | \|dP/dt\|/σ | TESS geçiş sayısı | σ_Rømer (ms/yıl) | Eşik (ms/yıl) | Sonuç |
|---|---|---|---|---|---|
| CoRoT-2 b | 7,3 | 5 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| HAT-P-37 b | 5,1 | 8 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| KELT-16 b | 5,8 | 65 | 39,3 | 9,3 | Elendi: arşiv radyal hız verisi yetersiz |
| TrES-1 b | 6,3 | 34 | 2,2 | 4,9 | **Seçildi** |
| TrES-5 b | 4,6 | 66 | 29,2 | 3,2 | Elendi: arşiv radyal hız verisi yetersiz |
| WASP-4 b | 11,5 | 47 | 0,4 | 2,1 | **Seçildi** |
| WASP-10 b | 7,9 | 8 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| WASP-12 b | 32,8 | 81 | 1,6 | 10,1 | **Seçildi** |
| WASP-22 b | 4,2 | 5 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| WASP-45 b | 8,0 | 14 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| XO-4 b | 3,6 | 16 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| HAT-P-7 b | 4,5 | 66 | 1,2 | 6,1 | **Seçildi** |
| WASP-1 b | 4,3 | 9 | – | – | Elendi: TESS geçiş sayısı 30'dan az |
| WASP-46 b | 18,1 | 32 | 56,3 | 17,2 | Elendi: arşiv radyal hız verisi yetersiz |

# 6. Ekler — EK-1: Kaynaklar

- Adams, E. R. vd. 2024. "Doomed Worlds. I. No New Evidence for Orbital Decay in a Long-term Survey of 43 Ultrahot Jupiters", The Planetary Science Journal, 5, 163. https://doi.org/10.3847/PSJ/ad3e80
- Akeson, R. L. vd. 2013. "The NASA Exoplanet Archive: Data and Tools for Exoplanet Research", Publications of the Astronomical Society of the Pacific, 125, 989-999. https://doi.org/10.1086/672273
- Applegate, J. H. 1992. "A Mechanism for Orbital Period Modulation in Close Binaries", The Astrophysical Journal, 385, 621. https://doi.org/10.1086/170967
- Astropy Collaboration vd. 2022. "The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package", The Astrophysical Journal, 935, 167. https://doi.org/10.3847/1538-4357/ac7c74
- Baştürk, Ö. vd. 2025. "The Orbit of WASP-4 b is in Decay", Monthly Notices of the Royal Astronomical Society, 541, 714-730. https://doi.org/10.1093/mnras/staf1009
- Bonomo, A. S. vd. 2017. "The GAPS Programme with HARPS-N at TNG. XIV. Investigating Giant Planet Migration History via Improved Eccentricity and Mass Determination for 231 Transiting Planets", Astronomy & Astrophysics, 602, A107. https://doi.org/10.1051/0004-6361/201629882
- Bouma, L. G. vd. 2020. "WASP-4 Is Accelerating toward the Earth", The Astrophysical Journal Letters, 893, L29. https://doi.org/10.3847/2041-8213/ab8563
- DACE (Data & Analysis Center for Exoplanets), Cenevre Üniversitesi. https://dace.unige.ch, Son erişim tarihi: 7 Kasım 2026.
- Foreman-Mackey, D. vd. 2013. "emcee: The MCMC Hammer", Publications of the Astronomical Society of the Pacific, 125, 306-312. https://doi.org/10.1086/670067
- Hagey, S. R. vd. 2025. "TrES-1 b: A Case Study in Detecting Secular Evolution of Exoplanet Orbits", The Astronomical Journal, 170, 197. https://doi.org/10.3847/1538-3881/aded15
- Ivshina, E. S. ve Winn, J. N. 2022. "TESS Transit Timing of Hundreds of Hot Jupiters", The Astrophysical Journal Supplement Series, 259, 62. https://doi.org/10.3847/1538-4365/ac545b
- Knutson, H. A. vd. 2014. "Friends of Hot Jupiters. I. A Radial Velocity Search for Massive, Long-period Companions to Close-in Gas Giant Planets", The Astrophysical Journal, 785, 126. https://doi.org/10.1088/0004-637X/785/2/126
- Kokori, A. vd. 2023. "ExoClock Project. III. 450 New Exoplanet Ephemerides from Ground and Space Observations", The Astrophysical Journal Supplement Series, 265, 4. https://doi.org/10.3847/1538-4365/ac9da4
- Kreidberg, L. 2015. "batman: BAsic Transit Model cAlculatioN in Python", Publications of the Astronomical Society of the Pacific, 127, 1161-1165. https://doi.org/10.1086/683602
- Kutluay, A. C. vd. 2026. "Chasing the Tides: Searching for Orbital Decay Signatures in Transit Timing Data and Tidal Models for 20 Hot Jupiters", Publications of the Astronomical Society of the Pacific, 138, 024405. https://doi.org/10.1088/1538-3873/ae406a
- Lomb, N. R. 1976. "Least-squares Frequency Analysis of Unequally Spaced Data", Astrophysics and Space Science, 39, 447-462. https://doi.org/10.1007/BF00648343
- MAST (Mikulski Archive for Space Telescopes), Space Telescope Science Institute. https://archive.stsci.edu, Son erişim tarihi: 7 Kasım 2026.
- Oberst, T. E. vd. 2017. "KELT-16b: A Highly Irradiated, Ultra-short Period Hot Jupiter Nearing Tidal Disruption", The Astronomical Journal, 153, 97. https://doi.org/10.3847/1538-3881/153/3/97
- Ochsenbein, F., Bauer, P. ve Marcout, J. 2000. "The VizieR Database of Astronomical Catalogues", Astronomy and Astrophysics Supplement Series, 143, 23-32. https://doi.org/10.1051/aas:2000169
- Patra, K. C. vd. 2017. "The Apparently Decaying Orbit of WASP-12b", The Astronomical Journal, 154, 4. https://doi.org/10.3847/1538-3881/aa6d75
- Penev, K. vd. 2018. "Empirical Tidal Dissipation in Exoplanet Hosts from Tidal Spin-up", The Astronomical Journal, 155, 165. https://doi.org/10.3847/1538-3881/aaaf71
- Poddaný, S., Brát, L. ve Pejcha, O. 2010. "Exoplanet Transit Database. Reduction and Processing of the Photometric Data of Exoplanet Transits", New Astronomy, 15, 297-301. https://doi.org/10.1016/j.newast.2009.09.001
- Ricker, G. R. vd. 2015. "Transiting Exoplanet Survey Satellite", Journal of Astronomical Telescopes, Instruments, and Systems, 1, 014003. https://doi.org/10.1117/1.JATIS.1.1.014003
- Rothmeier, M. vd. 2025. "Doomed Worlds. II. Reassessing Suggestions of Orbital Decay for TrES-5 b", The Planetary Science Journal, 6, 292. https://doi.org/10.3847/PSJ/ae1b9c
- Scargle, J. D. 1982. "Studies in Astronomical Time Series Analysis. II. Statistical Aspects of Spectral Analysis of Unevenly Spaced Data", The Astrophysical Journal, 263, 835. https://doi.org/10.1086/160554
- Schwarz, G. 1978. "Estimating the Dimension of a Model", The Annals of Statistics, 6, 461-464. https://doi.org/10.1214/aos/1176344136
- Sodickson, N. ve Grunblatt, S. 2025. "In Search of Decay: An Analysis of Transit Times of Hot Jupiters in Main-sequence and Post-main-sequence Systems", The Astrophysical Journal, 993, 78. https://doi.org/10.3847/1538-4357/adfd60
- T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. 2023. "On İkinci Kalkınma Planı (2024-2028)". https://www.sbb.gov.tr/wp-content/uploads/2023/12/On-Ikinci-Kalkinma-Plani_2024-2028_11122023.pdf, Son erişim tarihi: 7 Kasım 2026.
- T.C. Sanayi ve Teknoloji Bakanlığı. 2025. "2030 Sanayi ve Teknoloji Stratejisi". https://www.sanayi.gov.tr/assets/img/popup-image/pdf/SanayiTeknolojiStratejisi2030.pdf, Son erişim tarihi: 7 Kasım 2026.
- Wang, W. vd. 2024. "Long-term Variations in the Orbital Period of Hot Jupiters from Transit-timing Analysis Using TESS Survey Data", The Astrophysical Journal Supplement Series, 270, 14. https://doi.org/10.3847/1538-4365/ad0847
- Watson, C. A. ve Marsh, T. R. 2010. "Orbital Period Variations of Hot Jupiters Caused by the Applegate Effect", Monthly Notices of the Royal Astronomical Society, 405, 2037. https://doi.org/10.1111/j.1365-2966.2010.16602.x
- Winn, J. N. vd. 2009. "HAT-P-7: A Retrograde or Polar Orbit, and a Third Body", The Astrophysical Journal, 703, L99-L103. https://doi.org/10.1088/0004-637X/703/2/L99
- Winn, J. N. ve Stefánsson, G. 2025. "Orbital Decay Candidates Reconsidered: WASP-4 b Is Not Decaying and Kepler-1658 b Is Not a Planet", The Planetary Science Journal, 6, 300. https://doi.org/10.3847/PSJ/ae21db
- Yang, E., Su, Y. ve Winn, J. N. 2025. "A Third Star in the HAT-P-7 System and a New Dynamical Pathway to Misaligned Hot Jupiters", The Astrophysical Journal, 986, 117. https://doi.org/10.3847/1538-4357/add5f7
- Yee, S. W. vd. 2020. "The Orbit of WASP-12b Is Decaying", The Astrophysical Journal Letters, 888, L5. https://doi.org/10.3847/2041-8213/ab5c16
