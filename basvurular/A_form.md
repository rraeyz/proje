> BELGE A — Mevcut dört hedef (WASP-12 b, WASP-4 b, HAT-P-7 b, TrES-1 b), hocanın 8 Kasım notlarına göre yeniden yazıldı.

# A. Genel Bilgiler

| Alan | Değer |
|---|---|
| Başvuru Sahibinin Adı Soyadı | İdris Avlar |
| Araştırma Önerisinin Başlığı | Sıcak Jüpiterlerde Yörünge Dönemi Değişimlerinin O−C Analiziyle İncelenmesi ve Fiziksel Kökenlerinin Belirlenmesi |
| Danışmanın Adı Soyadı | Hüseyin Er |
| Araştırmanın Yürütüleceği Kurum | Atatürk Üniversitesi, Fen Fakültesi, Astronomi ve Uzay Bilimleri Bölümü |

# Özet

Sıcak Jüpiterlerin yörünge dönemlerindeki değişimler, yıldız ile gezegen arasındaki gelgit etkileşimini gözlemle sınamanın az sayıdaki yolundan biridir. Bu değişimler geçiş zamanlarından oluşturulan O−C diyagramlarıyla izlenir. Ancak O−C diyagramında görülen parabolik bir değişim yalnızca gelgit bozulmasından değil; apsis hareketinden, uzak bir eşlikçinin ışık-zaman (Rømer) etkisinden, yıldızın manyetik aktivitesinden (Applegate mekanizması), üçüncü bir cismin çekiminden ya da kütle kaybından da kaynaklanabilir. Bu projede dört sıcak Jüpiter sistemi incelenecektir: WASP-12 b, WASP-4 b, HAT-P-7 b ve TrES-1 b. Sistemler, Wang vd. (2024)'nin bildirdiği dönem değişimi adayları arasından, TESS verisinin yeterli olması ve ışık-zaman etkisinin dikine hız verisiyle sınanmış olması ölçütleriyle seçilmiştir. WASP-12 b'de gelgit bozulması, HAT-P-7 b'de ise üçüncü bir yıldızın ışık-zaman etkisi literatürde ortaya konmuştur; bu iki sistem kullanılan yöntemin bilinen sonuçları bulup bulmadığını sınamak için incelenecektir. WASP-4 b ve TrES-1 b'de ise dönem değişiminin nedeni hâlâ tartışmalıdır. Her sistem için yayımlanmış geçiş zamanları ve yer gözlemleri derlenecek, tüm zamanlar BJD_TDB sistemine dönüştürülecek ve henüz yayımlanmamış TESS sektörlerinden yeni orta geçiş zamanları ölçülecektir. O−C diyagramlarına doğrusal ve kuadratik modeller uyumlanacak, modeller χ² ve Bayes Bilgi Kriteri (BIC) istatistikleriyle karşılaştırılacak ve her sistem için güncel efemeris belirlenecektir. Dönem değişimi bulunan sistemlerde altı fiziksel mekanizma kendi bağıntılarıyla sınanacak; gelgit bozulması ile ışık-zaman etkisi, arşivdeki dikine hız ölçümlerinden hesaplanan ivme ile ayırt edilecektir. Projede yeni gözlem yapılmayacak ve bütçe gerekmemektedir. Proje sonunda dört sistem için güncel efemerisler, dönem değişiminin nedenine ilişkin bir sonuç tablosu ve açık erişimli bir veri seti elde edilecek; sonuçların danışmanla birlikte kısa bir makale olarak paylaşılması hedeflenmektedir.

**Anahtar Kelimeler:** Sıcak Jüpiter, geçiş zamanlaması, O−C diyagramı, gelgit bozulması, ışık-zaman etkisi

# 1. Araştırma Önerisinin Bilimsel Niteliği

## 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Sıcak Jüpiterler, Jüpiter kütlesinde olan ve yıldızlarının etrafında birkaç günde dolanan gezegenlerdir. Yıldıza çok yakın oldukları için yıldızda bir gelgit şişkinliği oluştururlar. Yıldız kendi ekseni etrafında gezegenin yörünge hareketinden daha yavaş dönüyorsa bu şişkinlik gezegeni yavaşlatır, gezegen yıldıza yaklaşır ve yörünge dönemi kısalır. Bu sürecin hızı yıldızın gelgit kalite faktörüne (Q′*) bağlıdır. Q′* için kuramsal ve gözlemsel tahminler birkaç mertebe farklılık gösterdiğinden (Penev vd., 2018), dönem değişiminin doğrudan ölçülmesi yıldızların iç yapısı hakkında da bilgi verir.

Dönem değişimi, gözlenen geçiş zamanları (O) ile sabit dönemle hesaplanan zamanlar (C) arasındaki farkın çizildiği O−C diyagramıyla incelenir. Dönem sabit bir hızla değişiyorsa O−C diyagramı bir parabol çizer. Bugüne kadar gelgit bozulması kesin olarak gösterilmiş tek sistem WASP-12 b'dir. Bu sistemde geçiş ve ikincil tutulma zamanları ile dikine hız ölçümleri birlikte kullanılarak apsis hareketi ve ışık-zaman etkisi dışlanmış, dönem değişim hızı yaklaşık −30 ms/yıl olarak bulunmuştur (Yee vd., 2020; Wong vd., 2022; Kutluay vd., 2023; Leonardi vd., 2024; Winn ve Stefánsson, 2025). Wang vd. (2024), TESS (Ricker vd., 2015) verilerini literatürdeki zamanlarla birleştirerek 326 sıcak Jüpiteri incelemiş ve 26 dönem değişimi adayı bildirmiştir. Bu adaylardan 14'ü, sonucun tek bir ölçüme bağlı olup olmadığını sınayan LOOCV (Leave-One-Out Cross-Validation) testini geçmiştir. Wang vd. bu adaylarda gelgit dışındaki mekanizmaların da etkili olabileceğini belirtmiş, ancak nedenleri sistem bazında incelememiştir.

Konunun temel sorunu, O−C diyagramındaki bir parabolün tek başına nedenini göstermemesidir. Uzak bir eşlikçi nedeniyle bakış doğrultusunda ivmelenen bir sistemde ışığın bize ulaşma süresi değişir ve geçiş zamanlarında gelgit bozulmasıyla aynı parabolik iz oluşur (Bouma vd., 2020). Bu ayrım ancak yıldızın dikine hızındaki uzun dönemli değişimle yapılabilir. WASP-4 b bu sorunun en iyi örneğidir. Bouma vd. (2020) dikine hızlarda bir ivme bularak dönem değişiminin büyük kısmını ışık-zaman etkisine bağlamış; Baluev vd. (2020) ve Turner vd. (2022) ise bu ivmeyi doğrulayamamıştır. Harre vd. (2023) ve Baştürk vd. (2025) değişimi gelgit bozulmasıyla açıklarken, Harre ve Smith (2023) sonucun ışık-zaman düzeltmesine bağlı olduğunu göstermiş, Winn ve Stefánsson (2025) ise yeni dikine hız verileriyle değişimi uzak bir eşlikçinin ışık-zaman etkisine bağlamıştır. TrES-1 b için bulunan değerler de birbirinden farklıdır: Adams vd. (2024) −16 ± 5 ms/yıl, Kutluay vd. (2026) −14,9 ± 0,6 ms/yıl bulmuş, Sodickson ve Grunblatt (2025) anlamlı bir değişim bulmamış, Hagey vd. (2025) ise ışık-zaman etkisini dışlayarak apsis hareketini ya da daha yavaş bir gelgit bozulmasını önermiştir. HAT-P-7 b'deki dönem artışı ise yakın zamanda yaklaşık 32 AB uzaklıktaki bir yıldızın ışık-zaman etkisiyle açıklanmıştır (Yang vd., 2025). Bunlara ek olarak, literatürdeki zamanlarda zaman sistemi karışıklıkları ve gerçekçi olmayan küçük ölçüm hataları da sahte dönem değişimleri üretebilmektedir (Adams vd., 2024).

Bu proje, Wang vd. (2024)'nin LOOCV testini geçen adaylarından seçilen dört sistemi aynı veri işleme yöntemi ve aynı karar ölçütleriyle incelemeyi amaçlamaktadır. Sistemler iki gruptan oluşmaktadır. WASP-12 b (gelgit bozulması) ve HAT-P-7 b (üçüncü bir yıldızın ışık-zaman etkisi) nedeni bilinen sistemlerdir ve yöntemin bu bilinen sonuçları bulup bulmadığını göstermek için kullanılacaktır. WASP-4 b ve TrES-1 b ise nedeni tartışmalı sistemlerdir. Bu iki sistem için incelediğimiz yayınlarda kullanılmamış TESS sektörleri bulunmaktadır: WASP-4 b için 2026 yılında gözlenen 103, 105 ve 106. sektörler, TrES-1 b için 2024 yılında gözlenen 81. sektör. TrES-1 b için ayrıca 2025–2026 yıllarında yapılmış yer gözlemleri vardır. Projenin sorusu, bu güncel verilerle WASP-4 b ve TrES-1 b'nin yörünge dönemlerinin anlamlı biçimde değişip değişmediği ve değişiyorsa bunun hangi mekanizmadan kaynaklandığıdır. Literatüre göre WASP-12 b'de değişimin gelgit bozulmasıyla, HAT-P-7 b'de ise ışık-zaman etkisiyle açıklanması beklenmektedir; yöntem bu iki sonucu bulamazsa diğer sistemler için verilecek sonuçlar da güvenilir sayılmayacaktır. WASP-4 b'de dönem değişiminin dikine hızlardaki ivmeyle açıklanıp açıklanamayacağı, TrES-1 b'de ise literatür zamanları gerçekçi hatalarla değerlendirildiğinde ve yeni zamanlar eklendiğinde değişimin anlamlı kalıp kalmadığı sınanacaktır.

Proje, On İkinci Kalkınma Planı'nın (2024–2028) temel bilimlere özel önem verilmesini ve uzay araştırmalarını kritik alanlar arasında sayan hedefiyle (madde 270) ve genç nesillerin uzay alanında çalışmaya teşvik edilmesini öngören hedefiyle (madde 271) ilişkilidir (T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı, 2023). 2030 Sanayi ve Teknoloji Stratejisi de TÜBİTAK araştırma desteklerinin astronomi dahil temel bilimlerde artırılmasını öngörmektedir (T.C. Sanayi ve Teknoloji Bakanlığı, 2025). Proje, bir uzay görevinin (TESS) verilerini işleyen ve yorumlayan lisans düzeyinde araştırmacılar yetiştirerek bu hedeflere katkı sağlayacaktır.

## 1.2. Amaç ve Hedefler

Projenin amacı, WASP-12 b, WASP-4 b, HAT-P-7 b ve TrES-1 b sistemlerinde yörünge dönemi değişiminin var olup olmadığını güncel verilerle sınamak ve değişim varsa nedenini belirlemektir.

**Hedef 1 (Veri seti):** Dört sistem için yayımlanmış geçiş zamanlarını ve yer gözlemlerini tek bir tabloda toplamak, tüm zamanları BJD_TDB sistemine dönüştürmek ve yayımlanmamış TESS sektörlerindeki (WASP-4 b: 103, 105, 106; TrES-1 b: 81) tam geçişlerin orta geçiş zamanlarını ölçmek.

**Hedef 2 (O−C diyagramları):** Her sistem için O−C diyagramını oluşturmak; doğrusal ve kuadratik modelleri karşılaştırarak dönem değişim hızını (dP/dt) belirsizliğiyle birlikte vermek ve değişimin anlamlı olup olmadığına karar vermek. Yöntemin doğruluğu, WASP-12 b için literatürdeki değerle (Wong vd., 2022) 2σ içinde uyumla gösterilecektir.

**Hedef 3 (Güncel efemeris):** Dört sistem için güncel efemerisleri (T0, P ve anlamlı ise dP/dt) belirlemek.

**Hedef 4 (Fiziksel mekanizmalar):** Dönem değişimi bulunan her sistem için gelgit bozulması, apsis hareketi, ışık-zaman etkisi, Applegate mekanizması, üçüncü cisim ve kütle kaybı mekanizmalarını önceden belirlenmiş ölçütlerle değerlendirmek ve sonuçları bir tabloda toplamak.

# 2. Yöntem

Proje, açık arşivlerdeki verilere dayanan gözlemsel bir çalışmadır; yeni gözlem yapılmayacaktır. Bağımsız değişken çevrim sayısı (E), bağımlı değişken gözlenen orta geçiş zamanı ve ondan hesaplanan O−C değeridir. Hesaplanacak temel büyüklük yörünge dönemindeki değişim hızıdır (dP/dt). Zaman sistemi, ölçüm belirsizliği ve verinin kaynağı kontrol edilen değişkenlerdir.

**2.1. Veri**

Her sistem için geçiş zamanları dört kaynaktan derlenecektir: Ivshina ve Winn (2022) ile Wang vd. (2024)'nin TESS zamanları, sisteme özel yayınlarda verilen zamanlar (WASP-12 b için Wong vd., 2022 ve Kutluay vd., 2023; WASP-4 b için Baştürk vd., 2025; TrES-1 b için Hagey vd., 2025), yer gözlemi veritabanları olan ETD/VarAstro (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023), ve proje kapsamında ölçülecek yeni TESS zamanları. Katalog tabloları VizieR'den (Ochsenbein vd., 2000), sistem parametreleri NASA Exoplanet Archive'dan (Akeson vd., 2013), TESS ışık eğrileri MAST'tan alınacaktır. Dikine hız ölçümleri yayımlanmış makale tablolarından (Knutson vd., 2014; Bonomo vd., 2017; Bouma vd., 2020) ve DACE arşivinden alınacaktır.

Farklı çalışmalar zamanları farklı sistemlerde verdiğinden her zamanın sistemi kaynak makaleden kontrol edilecek ve HJD ya da BJD_UTC olarak verilen zamanlar Astropy (Astropy Collaboration vd., 2022) ile BJD_TDB sistemine dönüştürülecektir. Zaman sistemi belirlenemeyen zamanlar ayrıca işaretlenecek ve analiz bu zamanlarla ve onlar olmadan iki kez yapılacaktır. ETD verilerinden yalnızca veri kalitesi yüksek olarak işaretlenmiş tam geçişler kullanılacaktır.

**2.2. TESS Verilerinin Analizi ve Orta Geçiş Zamanlarının Belirlenmesi**

Daha önce yayımlanmış TESS zamanları yeniden ölçülmeyecek, yayımlandıkları tablolardan alınacaktır. Yalnızca incelenen yayınlarda kullanılmamış sektörler (WASP-4 b: 103, 105, 106; TrES-1 b: 81) analiz edilecektir. Bu sektörlerin 2 dakikalık ışık eğrileri MAST'tan indirilecek, kalitesi düşük olarak işaretlenmiş ölçümler çıkarılacak ve her geçişin çevresindeki geçiş dışı akı düzeyine göre normalize edilecektir. Geçiş modeli batman paketiyle (Kreidberg, 2015) oluşturulacaktır. Önce bir sektördeki tüm geçişler evreye göre birleştirilerek gezegen-yıldız yarıçap oranı, a/R* ve yörünge eğim açısı belirlenecek; ardından her geçiş için bu değerler sabit tutularak yalnızca orta geçiş zamanı uyumlanacaktır. Orta geçiş zamanının belirsizliği emcee paketiyle yapılan Markov Zinciri Monte Carlo (MCMC) örneklemesinden (Foreman-Mackey vd., 2013) elde edilecektir. Kenar kararması katsayıları literatürden alınıp sabit tutulacak, verisi eksik olan kısmi geçişler kullanılmayacaktır.

**2.3. O−C Diyagramlarının Oluşturulması**

Her geçiş için çevrim sayısı E ve hesaplanan zaman C = T0 + P·E bulunacak, gözlenen zamandan çıkarılarak O−C değeri elde edilecektir. Burada T0 referans geçiş zamanı, P yörünge dönemidir. Zamanlara iki model, ölçüm hatalarıyla ağırlıklandırılmış en küçük kareler yöntemiyle uyumlanacaktır:

Doğrusal model (sabit dönem): T(E) = T0 + P·E

Kuadratik model (sabit hızla değişen dönem): T(E) = T0 + P·E + ½·(dP/dE)·E²

Dönem değişim hızı dP/dt = (1/P)·(dP/dE) bağıntısıyla hesaplanacaktır. Modelden 5σ'dan fazla sapan aykırı noktalar ayıklanacaktır. Literatür zamanları ile TESS zamanlarının ölçüm hataları ayrı ayrı ele alınacak; bir grubun artıklarının indirgenmiş χ² değeri 1'den büyükse o grubun hataları bu değer 1 olacak şekilde büyütülecektir. İki model χ² ve Bayes Bilgi Kriteri (BIC = χ² + k·ln n; Schwarz, 1978) istatistikleriyle karşılaştırılacaktır; burada k modeldeki parametre sayısı, n zaman sayısıdır. Wang vd. (2024) ile aynı ölçüt kullanılarak, kuadratik model doğrusal modelden ΔBIC > 10 farkla daha iyiyse ve dP/dt sıfırdan en az 3σ farklıysa dönem değişimi anlamlı kabul edilecektir. Anlamlı değişim yoksa doğrusal model, varsa kuadratik model güncel efemeris olarak verilecektir.

**2.4. Fiziksel Mekanizmalar**

Dönem değişimi anlamlı bulunan sistemlerde aşağıdaki altı mekanizma tek tek değerlendirilecektir. Gerekli sistem parametreleri (Mp, M*, R*, a, e) NASA Exoplanet Archive'dan alınacaktır.

**2.4.1. Gelgit Bozulması (Orbital Decay)**

Gelgit bozulmasında dönem değişim hızı yıldızın gelgit kalite faktörüne bağlıdır (Patra vd., 2017):

dP/dt = −(27π / 2Q′*)·(Mp/M*)·(R*/a)⁵

Burada Mp gezegenin kütlesi, M* yıldızın kütlesi, R* yıldızın yarıçapı, a yörüngenin yarı-büyük eksenidir. Bu bağıntıdan gözlenen değişimi açıklamak için gereken Q′* hesaplanacak ve literatürdeki değerlerle (Penev vd., 2018) karşılaştırılacaktır. Yıldız gezegenin yörünge hareketinden yavaş döndüğünde gelgit dönemi yalnızca kısaltabileceği için, dönemi uzayan bir sistemde gelgit bozulması dışlanacaktır (Wang vd., 2024).

**2.4.2. Apsis Hareketi (Eksen Dönmesi)**

Yörünge dışmerkez ise yörüngenin büyük ekseni zamanla döner ve geçiş zamanlarında çevrimsel bir değişim oluşur. Geçiş ve ikincil tutulma zamanları şu bağıntılarla verilir (Patra vd., 2017):

t_geçiş(E) = T0 + Ps·E − (e·Pa/π)·cos ω(E)

t_ikincil(E) = T0 + Pa/2 + Ps·E + (e·Pa/π)·cos ω(E)

ω(E) = ω0 + (dω/dE)·E ve Ps = Pa·[1 − (dω/dE)/2π]

Burada e dışmerkezlik, ω enberi boylamı, dω/dE enberi boylamının çevrim başına değişimi, Pa anomalistik dönem, Ps yıldızıl dönemdir. Dışmerkezlik ve enberi boylamı dikine hız modelinden (2.4.4) alınacak ve beklenen en büyük değişim genliği (e·Pa/π) gözlenen O−C değişimiyle karşılaştırılacaktır. İkincil tutulma zamanları bulunan WASP-12 b'de iki bağıntının farkından e·cos ω ayrıca hesaplanacaktır. Apsis hareketinde ikincil tutulmalar geçişlerle zıt yönde, gelgit bozulmasında ise aynı yönde kayar; bu fark iki mekanizmayı ayırt etmek için kullanılacaktır.

**2.4.3. Işık-Zaman Etkisi (Rømer Etkisi)**

Sistem uzak bir eşlikçi nedeniyle bakış doğrultusunda sabit bir ivmeyle hareket ediyorsa, ışığın bize ulaşma süresi değişir ve dönem değişiyormuş gibi görünür (Bouma vd., 2020):

(dP/dt)_ışık-zaman = P·γ̇ / c

Burada γ̇ dikine hızdaki ivme (2.4.4), c ışık hızıdır. Bu değer O−C'den bulunan dP/dt ile karşılaştırılacaktır. İki değerin farkı, birleşik belirsizliğe (√(σ²_O−C + σ²_ışık-zaman)) oranla 2σ'dan küçükse değişim ışık-zaman etkisiyle açıklanabilir; 3σ'dan büyükse açıklanamaz ve ışık-zaman katkısı çıkarıldıktan sonra kalan değişim diğer mekanizmalarla değerlendirilir; arada kalan durumlar "kısmen açıklanabilir" olarak verilecektir.

**2.4.4. Dikine Hız Verilerinin Modellenmesi**

Işık-zaman etkisi ve apsis hareketi için gereken ivme, dışmerkezlik ve enberi boylamı, yayımlanmış dikine hız ölçümlerinden elde edilecektir. Dikine hız modeli şudur:

v(t) = γ_j + K·[cos(ν + ω) + e·cos ω] + γ̇·(t − t0)

Burada K gezegenin oluşturduğu hız genliği, ν gerçek anomali, γ_j j. tayfçekerin sistemik hızı, γ̇ ivme, t0 referans zamandır. Farklı tayfçekerlerin ölçümleri aynı yıldız için farklı sistemik hız değerleri verdiğinden her tayfçekere ayrı bir γ_j tanımlanacaktır. Gezegen yıldızın önünden geçerken alınan ölçümler (Rossiter-McLaughlin etkisi) çıkarılacak; yıldız etkinliğinden kaynaklanan ek hız gürültüsü (jitter) ölçüm hatalarına eklenecektir. Model en küçük kareler yöntemiyle uyumlanacak, parametrelerin belirsizlikleri emcee ile MCMC örneklemesinden alınacaktır. Doğrusal ivme yeterli olmazsa modele ikinci dereceden bir terim eklenecektir.

**2.4.5. Applegate Mekanizması**

Yıldızın manyetik aktivite döngüsü kütle dağılımını değiştirir ve yörünge döneminde çevrimsel bir değişim yaratır (Applegate, 1992; Watson ve Marsh, 2010):

ΔP/P = −9·(R*/a)²·ΔQ/(M*·R*²) ve A = (P_mod/2π)·(ΔP/P)

Burada ΔQ yıldızın kuadrupol momentindeki değişim, P_mod aktivite döngüsünün süresi, A O−C diyagramındaki değişimin genliğidir. Gözlenen değişimi üretmek için gereken ΔQ ve buna karşılık gelen enerji, yıldızın ışınım gücüyle karşılaştırılacaktır.

**2.4.6. Üçüncü Cisim**

Üçüncü bir cisim, sistemin ortak kütle merkezi etrafında dolanması nedeniyle O−C diyagramında çevrimsel bir değişim oluşturur. Kuadratik modelin artıklarında Lomb-Scargle periyodogramıyla (Lomb, 1976; Scargle, 1982) periyodik sinyal aranacak; yanlış alarm olasılığı 0,01'den küçük olan sinyaller dikkate alınacak, gözlem mevsiminden kaynaklanan yaklaşık bir yıllık sinyaller dışarıda bırakılacaktır. Sinyal bulunursa yarı genliği A ve dönemi P₃ kullanılarak üçüncü cismin kütle fonksiyonu hesaplanacaktır (Irwin, 1952):

f(M₃) = 4π²·(A·c)³ / (G·P₃²) = (M₃·sin i₃)³ / (M* + Mp + M₃)²

Burada M₃ üçüncü cismin kütlesi, i₃ yörüngesinin eğim açısı, G kütle çekim sabitidir.

**2.4.7. Kütle Kaybı**

Gezegen yıldızına Roche sınırı kadar yaklaşırsa kütle kaybedebilir ve bu durum yörüngeyi değiştirebilir. Roche sınırı a_Roche ≈ 2,16·Rp·(M*/Mp)^(1/3) bağıntısıyla (Ford ve Rasio, 2006) hesaplanacaktır; burada Rp gezegenin yarıçapıdır. a/a_Roche oranı 1'e yakın olan sistemlerde kütle kaybının katkısı tartışılacak, bu oranın belirgin biçimde büyük olduğu sistemlerde ihmal edilecektir.

Her mekanizma için sonuç "dışlandı", "olası değil", "olası" ya da "ayırt edilemedi" olarak verilecek ve dört sistemin sonuçları bir tabloda toplanacaktır.

**2.5. Hedeflerin Seçimi (Ön Çalışma)**

Ön çalışma olarak yalnızca hedef seçimi yapılmıştır. Wang vd. (2024)'nin LOOCV testini geçen 14 adayı iki ölçüte göre incelenmiştir. Birinci ölçüt, Wang vd.'nin bildirdiği TESS geçiş zamanı sayısının en az 30 olmasıdır; adaylar arasındaki en kısa yörünge döneminde bile bu sayı en az iki TESS sektörüne karşılık gelir. İkinci ölçüt, gelgit bozulmasının ışık-zaman etkisinden ayırt edilebilmesi için, ışık-zaman katkısının dikine hız verisiyle sınandığı yayımlanmış bir analizin bulunmasıdır (Bouma vd., 2020; Hagey vd., 2025). İki ölçütü birlikte sağlayan dört aday seçilmiştir (Tablo 1). Ayrıca bu sistemlerin TESS sektörleri MAST arşivinde tek tek kontrol edilmiş ve hangi sektörlerin yayımlanmış çalışmalarda kullanıldığı belirlenmiştir. Yöntemin adımları, çalışma takvimindeki iş paketleriyle aynı sırayla yürütülecektir.

# 3. Proje Yönetimi

## 3.1. Çalışma Takvimi

| Tarih Aralığı | Faaliyetler | Kim(ler) | Başarı Ölçütü ve Katkısı |
|---|---|---|---|
| 1.–3. ay | İP1: Yayımlanmış geçiş zamanlarının ve yer gözlemlerinin derlenmesi; zamanların BJD_TDB sistemine dönüştürülmesi | İdris Avlar (proje yürütücüsü; zaman sistemi dönüşümleri); Bahar Cayib (proje ortağı; zamanların ve kaynaklarının tabloya girilmesi); Hüseyin Er (akademik danışman) | Dört sistem için kaynakları belirtilmiş, tümü BJD_TDB sisteminde bir zaman tablosu; zaman sistemi belirsiz kaynaklar işaretli (%20) |
| 4.–5. ay | İP2: Yayımlanmamış TESS sektörlerinden (WASP-4 b: 103, 105, 106; TrES-1 b: 81) orta geçiş zamanlarının ölçülmesi | İdris Avlar (proje yürütücüsü; ışık eğrisi modellemesi ve zaman ölçümü); Bahar Cayib (proje ortağı; ışık eğrilerinin indirilmesi ve geçişlerin gözle kontrolü) | Bu sektörlerdeki tüm tam geçişler için belirsizliğiyle birlikte orta geçiş zamanı (%20) |
| 6.–7. ay | İP3: O−C diyagramlarının oluşturulması; doğrusal ve kuadratik modellerin karşılaştırılması; güncel efemerislerin belirlenmesi | İdris Avlar (proje yürütücüsü; model uyumlama ve istatistiksel karşılaştırma); Bahar Cayib (proje ortağı; O−C diyagramlarının çizilmesi); Hüseyin Er (akademik danışman) | Dört sistem için dP/dt ± σ, ΔBIC, "anlamlı değişim var/yok" kararı ve güncel efemeris; WASP-12 b'de literatürle 2σ içinde uyum (%25) |
| 8.–11. ay | İP4: Dikine hız verilerinin modellenmesi; gelgit bozulması, apsis hareketi, ışık-zaman etkisi, Applegate mekanizması, üçüncü cisim ve kütle kaybının değerlendirilmesi | İdris Avlar (proje yürütücüsü; dikine hız modeli ve mekanizma testleri); Bahar Cayib (proje ortağı; dikine hız ölçümlerinin ve sistem parametrelerinin derlenmesi); Hüseyin Er (akademik danışman) | Dönem değişimi bulunan her sistem için altı mekanizmanın sonucunu gerekçesiyle veren tablo; nedeni bilinen iki sistemde (WASP-12 b, HAT-P-7 b) sonuçların literatürle karşılaştırılması (%35) |

## 3.2. Risk Yönetimi

| En Önemli Riskler | Alınacak Tedbirler (B Planı) |
|---|---|
| Literatürdeki zamanlarda zaman sistemi belirsizliği ya da gerçekçi olmayan küçük ölçüm hataları sahte bir dönem değişimi üretebilir. | Her zamanın sistemi kaynak makaleden kontrol edilecek; belirsiz zamanlarla ve onlar olmadan iki ayrı analiz yapılacak; ölçüm hataları her veri grubu için indirgenmiş χ² ile ölçeklenecektir. |
| Bazı yayınlardaki geçiş zamanları tablo olarak verilmemiş olabilir. | Bu zamanların ait olduğu TESS sektörleri aynı yöntemle (2.2) ölçülecektir; yöntemin geri kalanı değişmez. |
| Yayımlanmamış TESS sektörlerinde bazı geçişler veri boşlukları ya da düşük sinyal-gürültü oranı nedeniyle ölçülemeyebilir. | Tek tek ölçülemeyen geçişler için sektördeki tüm geçişler birlikte uyumlanarak sektör başına bir orta geçiş zamanı elde edilecektir. |
| Güncel verilerle bir sistemde anlamlı dönem değişimi bulunmayabilir. | Bu durum araştırma sorusunun bir cevabı olarak raporlanacak ve doğrusal efemeris verilecektir; mekanizma analizi diğer sistemlerle sürdürülecektir. |
| Gelgit bozulması ile ışık-zaman etkisi mevcut dikine hız verisiyle ayırt edilemeyebilir. | İki mekanizmanın da öngördüğü değerler verilecek ve sonuç "ayırt edilemedi" olarak gerekçesiyle raporlanacaktır. |
| Yöntem, nedeni bilinen sistemlerde (WASP-12 b, HAT-P-7 b) literatürdeki sonucu bulamayabilir. | Fark veri seçimi, zaman sistemi ve hata ölçeklemesi açısından incelenecek; sorun giderilmeden diğer sistemler için sonuç verilmeyecektir. |
| İş paketlerinde gecikme yaşanabilir. | İş paketleri ardışık planlanmış ve 12. ay tampon olarak bırakılmıştır; ilerleme danışmanla düzenli görüşmelerle izlenecektir. |
| Yazılım ya da bilgisayar arızası yaşanabilir. | Kod ve veriler düzenli olarak yedeklenecek; analizler ücretsiz çevrim içi Python ortamlarında da çalışabilecek şekilde hazırlanacaktır. |

## 3.3. Araştırma Olanakları

| Kuruluşta Bulunan Altyapı/Ekipman Türü, Modeli | Projede Kullanım Amacı |
|---|---|
| Proje yürütücüsünün kişisel dizüstü bilgisayarı ile üniversite kütüphanesindeki bilgisayarlar ve internet erişimi | Veri indirme, ışık eğrisi analizi, O−C ve dikine hız analizleri |
| Açık erişimli veri arşivleri: MAST (TESS), VizieR, NASA Exoplanet Archive, DACE, ETD/VarAstro, ExoClock | Geçiş zamanları, ışık eğrileri, sistem parametreleri ve dikine hız ölçümleri |
| Açık kaynak yazılımlar: Python, NumPy, Astropy, astroquery, batman, emcee | Tüm analizlerin ücretsiz ve tekrarlanabilir biçimde yapılması |

# 4. Araştırma Önerisinin Yaygın Etkisi

| Çıktı, Etki ve Kazanımlar | Öngörülen Çıktı(lar), Etki(ler) ve Kazanım(lar) |
|---|---|
| Bilimsel/Akademik Çıktılar | Dört sistemin O−C analizini ve dönem değişiminin nedenine ilişkin sonuç tablosunu içeren proje sonuç raporu. Sonuçların, yeterli görülmesi halinde danışmanla birlikte kısa bir makale olarak sunulması hedeflenmektedir. |
| Ekonomik/Ticari/Sosyal Çıktılar | Dört sistemin tüm geçiş zamanlarını (yeni TESS zamanları dahil) BJD_TDB sisteminde içeren açık erişimli veri seti, analiz kodu ve güncel efemerisler. Bu çıktılar gelecekteki geçiş gözlemlerinin planlanmasında kullanılabilecektir. Danışmanın uygun görmesi halinde bölüm öğrencilerine yönelik kısa bir O−C analizi tanıtım sunumu yapılması hedeflenmektedir. |
| Yeni Proje(ler) Oluşturmasına Yönelik Çıktılar | Aynı yöntemin Wang vd. (2024)'nin diğer adaylarına uygulanmasıyla olası bir lisansüstü tez çalışmasına temel oluşturulması. |

# 5. Belirtmek İstediğiniz Diğer Konular

Aşağıdaki tablo, yöntem bölümünde (2.5) anlatılan hedef seçiminin sonucudur.

**Tablo 1.** Hedef seçim tablosu. Satırlar, Wang vd. (2024)'nin dönem değişimi bildirdiği 26 adaydan LOOCV testini geçen 14 adaydır (Wang vd., 2024, Tablo 3). |dP/dt|/σ (dönem değişim hızının belirsizliğine oranı) ve TESS geçiş sayısı Wang vd. (2024)'nin VizieR'deki tablolarından (J/ApJS/270/14) alınmıştır. Eşik, Wang vd.'nin |dP/dt| değerinin üçte biridir. "Işık-zaman analizi" sütunu, uzak bir eşlikçinin ivmesinden kaynaklanabilecek görünür dönem değişimini dikine hız verisiyle sınayan yayımlanmış çalışmaların sonucunu verir; sayısal değerler Bouma vd. (2020) Tablo 5'tendir. Seçim ölçütleri: (1) TESS geçiş sayısı en az 30; (2) ışık-zaman katkısı yayımlanmış bir dikine hız analiziyle Eşik'ten küçük bir belirsizlikle hesaplanmış ya da açıkça dışlanmış. "–": aday birinci ölçütte elendiği için ışık-zaman analizi taranmadı.

| Aday | \|dP/dt\|/σ | TESS geçiş sayısı | Eşik (ms/yıl) | Işık-zaman analizi (ms/yıl) | Sonuç |
|---|---|---|---|---|---|
| CoRoT-2 b | 7,3 | 5 | 7,2 | – | Elendi: TESS sayısı 30'dan az |
| HAT-P-37 b | 5,1 | 8 | 11,4 | – | Elendi: TESS sayısı 30'dan az |
| KELT-16 b | 5,8 | 65 | 9,3 | Yetersiz: dikine hızlar yalnızca yaklaşık 6 aya yayılıyor (Oberst vd., 2017) | Elendi: ışık-zaman etkisi sınanmamış |
| TrES-1 b | 6,3 | 34 | 4,9 | Dışlandı: 12 yıllık dikine hızlarda eğilim yok (Hagey vd., 2025) | **Seçildi** |
| TrES-5 b | 4,6 | 66 | 3,2 | Yetersiz: 217 güne yayılan 8 dikine hız ölçümü (Rothmeier vd., 2025) | Elendi: ışık-zaman etkisi sınanmamış |
| WASP-4 b | 11,5 | 47 | 2,1 | −5,9 ± 0,4 | **Seçildi** |
| WASP-10 b | 7,9 | 8 | 9,2 | −15,6 ± 4,1 | Elendi: TESS sayısı 30'dan az |
| WASP-12 b | 32,8 | 81 | 10,1 | −0,1 ± 1,1 | **Seçildi** |
| WASP-22 b | 4,2 | 5 | 23,9 | +21,7 ± 2,8 | Elendi: TESS sayısı 30'dan az |
| WASP-45 b | 8,0 | 14 | 56,4 | – | Elendi: TESS sayısı 30'dan az |
| XO-4 b | 3,6 | 16 | 20,9 | +4,3 ± 4,3 | Elendi: TESS sayısı 30'dan az |
| HAT-P-7 b | 4,5 | 66 | 6,1 | +15,0 ± 0,9 | **Seçildi** |
| WASP-1 b | 4,3 | 9 | 7,5 | +0,8 ± 1,5 | Elendi: TESS sayısı 30'dan az |
| WASP-46 b | 18,1 | 32 | 17,2 | İncelenen literatürde bulunamadı | Elendi: ışık-zaman etkisi sınanmamış |

# 6. Ekler — EK-1: Kaynaklar

- Adams, E. R. vd. 2024. "Doomed Worlds. I. No New Evidence for Orbital Decay in a Long-term Survey of 43 Ultrahot Jupiters", The Planetary Science Journal, 5, 163. https://doi.org/10.3847/PSJ/ad3e80
- Akeson, R. L. vd. 2013. "The NASA Exoplanet Archive: Data and Tools for Exoplanet Research", Publications of the Astronomical Society of the Pacific, 125, 989-999. https://doi.org/10.1086/672273
- Applegate, J. H. 1992. "A Mechanism for Orbital Period Modulation in Close Binaries", The Astrophysical Journal, 385, 621. https://doi.org/10.1086/170967
- Astropy Collaboration vd. 2022. "The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package", The Astrophysical Journal, 935, 167. https://doi.org/10.3847/1538-4357/ac7c74
- Baluev, R. V. vd. 2020. "WASP-4 Transit Timing Variation from a Comprehensive Set of 129 Transits", Monthly Notices of the Royal Astronomical Society: Letters, 496, L11-L15. https://doi.org/10.1093/mnrasl/slaa069
- Baştürk, Ö. vd. 2025. "The Orbit of WASP-4 b is in Decay", Monthly Notices of the Royal Astronomical Society, 541, 714-730. https://doi.org/10.1093/mnras/staf1009
- Bonomo, A. S. vd. 2017. "The GAPS Programme with HARPS-N at TNG. XIV. Investigating Giant Planet Migration History via Improved Eccentricity and Mass Determination for 231 Transiting Planets", Astronomy & Astrophysics, 602, A107. https://doi.org/10.1051/0004-6361/201629882
- Bouma, L. G. vd. 2020. "WASP-4 Is Accelerating toward the Earth", The Astrophysical Journal Letters, 893, L29. https://doi.org/10.3847/2041-8213/ab8563
- DACE (Data & Analysis Center for Exoplanets), Cenevre Üniversitesi. https://dace.unige.ch, Son erişim tarihi: 8 Kasım 2026.
- Ford, E. B. ve Rasio, F. A. 2006. "On the Relation between Hot Jupiters and the Roche Limit", The Astrophysical Journal, 638, L45-L48. https://doi.org/10.1086/500734
- Foreman-Mackey, D. vd. 2013. "emcee: The MCMC Hammer", Publications of the Astronomical Society of the Pacific, 125, 306-312. https://doi.org/10.1086/670067
- Hagey, S. R. vd. 2025. "TrES-1 b: A Case Study in Detecting Secular Evolution of Exoplanet Orbits", The Astronomical Journal, 170, 197. https://doi.org/10.3847/1538-3881/aded15
- Harre, J.-V. vd. 2023. "Examining the Orbital Decay Targets KELT-9 b, KELT-16 b, and WASP-4 b, and the Transit-timing Variations of HD 97658 b", Astronomy & Astrophysics, 669, A124. https://doi.org/10.1051/0004-6361/202244529
- Harre, J.-V. ve Smith, A. M. S. 2023. "The Apparent Tidal Decay of WASP-4 b Can Be Explained by the Rømer Effect", Universe, 9, 506. https://doi.org/10.3390/universe9120506
- Irwin, J. B. 1952. "The Determination of a Light-Time Orbit", The Astrophysical Journal, 116, 211. https://doi.org/10.1086/145604
- Ivshina, E. S. ve Winn, J. N. 2022. "TESS Transit Timing of Hundreds of Hot Jupiters", The Astrophysical Journal Supplement Series, 259, 62. https://doi.org/10.3847/1538-4365/ac545b
- Knutson, H. A. vd. 2014. "Friends of Hot Jupiters. I. A Radial Velocity Search for Massive, Long-period Companions to Close-in Gas Giant Planets", The Astrophysical Journal, 785, 126. https://doi.org/10.1088/0004-637X/785/2/126
- Kokori, A. vd. 2023. "ExoClock Project. III. 450 New Exoplanet Ephemerides from Ground and Space Observations", The Astrophysical Journal Supplement Series, 265, 4. https://doi.org/10.3847/1538-4365/ac9da4
- Kreidberg, L. 2015. "batman: BAsic Transit Model cAlculatioN in Python", Publications of the Astronomical Society of the Pacific, 127, 1161-1165. https://doi.org/10.1086/683602
- Kutluay, A. C. vd. 2023. "Updated Orbital Decay Rate of WASP-12 with New Data from TESS and Ground-based Observations", Turkish Journal of Astronomy and Astrophysics, 4, 10-22. https://doi.org/10.55064/tjaa.1307803
- Kutluay, A. C. vd. 2026. "Chasing the Tides: Searching for Orbital Decay Signatures in Transit Timing Data and Tidal Models for 20 Hot Jupiters", Publications of the Astronomical Society of the Pacific, 138, 024405. https://doi.org/10.1088/1538-3873/ae406a
- Leonardi, P. vd. 2024. "TASTE V. A New Ground-based Investigation of Orbital Decay in the Ultra-hot Jupiter WASP-12b", Astronomy & Astrophysics, 686, A84. https://doi.org/10.1051/0004-6361/202348363
- Lomb, N. R. 1976. "Least-squares Frequency Analysis of Unequally Spaced Data", Astrophysics and Space Science, 39, 447-462. https://doi.org/10.1007/BF00648343
- MAST (Mikulski Archive for Space Telescopes), Space Telescope Science Institute. https://archive.stsci.edu, Son erişim tarihi: 8 Kasım 2026.
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
- T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. 2023. "On İkinci Kalkınma Planı (2024-2028)". https://www.sbb.gov.tr/wp-content/uploads/2023/12/On-Ikinci-Kalkinma-Plani_2024-2028_11122023.pdf, Son erişim tarihi: 8 Kasım 2026.
- T.C. Sanayi ve Teknoloji Bakanlığı. 2025. "2030 Sanayi ve Teknoloji Stratejisi". https://www.sanayi.gov.tr/assets/img/popup-image/pdf/SanayiTeknolojiStratejisi2030.pdf, Son erişim tarihi: 8 Kasım 2026.
- Turner, J. D. vd. 2022. "Characterizing the WASP-4 System with TESS and Radial Velocity Data: Constraints on the Cause of the Hot Jupiter's Changing Orbit and Evidence of an Outer Planet", The Astronomical Journal, 163, 281. https://doi.org/10.3847/1538-3881/ac686f
- Wang, W. vd. 2024. "Long-term Variations in the Orbital Period of Hot Jupiters from Transit-timing Analysis Using TESS Survey Data", The Astrophysical Journal Supplement Series, 270, 14. https://doi.org/10.3847/1538-4365/ad0847
- Watson, C. A. ve Marsh, T. R. 2010. "Orbital Period Variations of Hot Jupiters Caused by the Applegate Effect", Monthly Notices of the Royal Astronomical Society, 405, 2037. https://doi.org/10.1111/j.1365-2966.2010.16602.x
- Winn, J. N. ve Stefánsson, G. 2025. "Orbital Decay Candidates Reconsidered: WASP-4 b Is Not Decaying and Kepler-1658 b Is Not a Planet", The Planetary Science Journal, 6, 300. https://doi.org/10.3847/PSJ/ae21db
- Wong, I. vd. 2022. "TESS Revisits WASP-12: Updated Orbital Decay Rate and Constraints on Atmospheric Variability", The Astronomical Journal, 163, 175. https://doi.org/10.3847/1538-3881/ac5680
- Yang, E., Su, Y. ve Winn, J. N. 2025. "A Third Star in the HAT-P-7 System and a New Dynamical Pathway to Misaligned Hot Jupiters", The Astrophysical Journal, 986, 117. https://doi.org/10.3847/1538-4357/add5f7
- Yee, S. W. vd. 2020. "The Orbit of WASP-12b Is Decaying", The Astrophysical Journal Letters, 888, L5. https://doi.org/10.3847/2041-8213/ab5c16
