> BELGE C — Dikine hız (RV) analizi yok; sabit ivmeli ışık-zaman (Rømer) etkisi kapsam dışı. Hedefler: WASP-45 b, WASP-46 b.

# A. Genel Bilgiler

| Alan | Değer |
|---|---|
| Başvuru Sahibinin Adı Soyadı | İdris Avlar |
| Araştırma Önerisinin Başlığı | WASP-45 b ve WASP-46 b Sıcak Jüpiterlerinde Yörünge Dönemi Değişiminin Yeni TESS Verileri ve O−C Analiziyle Sınanması |
| Danışmanın Adı Soyadı | Hüseyin Er |
| Araştırmanın Yürütüleceği Kurum | Atatürk Üniversitesi, Fen Fakültesi, Astronomi ve Uzay Bilimleri Bölümü |

# Özet

Sıcak Jüpiterlerin yörünge dönemlerindeki değişimler, yıldız ile gezegen arasındaki gelgit etkileşimini gözlemle sınamanın az sayıdaki yolundan biridir. Bu değişimler geçiş zamanlarından oluşturulan O−C diyagramlarıyla izlenir. Son yıllarda TESS verileriyle birçok sistemde dönem değişimi bildirilmiş, ancak bu sonuçların bir kısmı yeni verilerle doğrulanamamıştır. Bu projede iki sıcak Jüpiter sistemi incelenecektir: WASP-45 b ve WASP-46 b. Bu sistemler, Wang vd. (2024)'nin bildirdiği dönem değişimi adayları arasından iki ölçütle seçilmiştir: TESS uydusunun bu sistemleri son yayımlanmış zamanlama çalışmalarından sonra yeniden gözlemiş olması ve literatürde dönem değişiminin var olup olmadığı konusunda çelişkili sonuçlar bulunması. WASP-45 b için yılda yaklaşık 169 ms'lik hızlı bir kısalma bildirilmiş, ancak bu sonucun seyrek veriden kaynaklanabileceği belirtilmiştir. WASP-46 b için ise değişim olmadığını ve dönemin arttığını bildiren çalışmalar bulunmaktadır. İki sistemde de 2023–2026 yıllarında gözlenmiş ve incelediğimiz yayınlarda kullanılmamış TESS sektörleri vardır. Yayımlanmış geçiş zamanları ve yer gözlemleri derlenecek, tüm zamanlar BJD_TDB sistemine dönüştürülecek ve yeni TESS sektörlerinden orta geçiş zamanları ölçülecektir. O−C diyagramlarına doğrusal ve kuadratik modeller uyumlanacak, modeller χ² ve Bayes Bilgi Kriteri (BIC) istatistikleriyle karşılaştırılacak ve iki sistem için güncel efemeris belirlenecektir. Dönem değişimi bulunursa gelgit bozulması, apsis hareketi, Applegate mekanizması, üçüncü cisim ve kütle kaybı, geçiş zamanları ve yayımlanmış sistem parametreleri kullanılarak değerlendirilecektir. Projede yeni gözlem yapılmayacak ve bütçe gerekmemektedir. Proje sonunda iki sistem için güncel efemerisler, dönem değişiminin varlığı ve olası nedenlerine ilişkin bir sonuç tablosu ve açık erişimli bir veri seti elde edilecek; sonuçların danışmanla birlikte kısa bir makale olarak paylaşılması hedeflenmektedir.

**Anahtar Kelimeler:** Sıcak Jüpiter, geçiş zamanlaması, O−C diyagramı, TESS, WASP-45 b, WASP-46 b

# 1. Araştırma Önerisinin Bilimsel Niteliği

## 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Sıcak Jüpiterler, Jüpiter kütlesinde olan ve yıldızlarının etrafında birkaç günde dolanan gezegenlerdir. Yıldıza çok yakın oldukları için yıldızda bir gelgit şişkinliği oluştururlar. Yıldız kendi ekseni etrafında gezegenin yörünge hareketinden daha yavaş dönüyorsa bu şişkinlik gezegeni yavaşlatır, gezegen yıldıza yaklaşır ve yörünge dönemi kısalır. Bu sürecin hızı yıldızın gelgit kalite faktörüne (Q′*) bağlıdır. Q′* için kuramsal ve gözlemsel tahminler birkaç mertebe farklılık gösterdiğinden (Penev vd., 2018), dönem değişiminin doğrudan ölçülmesi yıldızların iç yapısı hakkında da bilgi verir.

Dönem değişimi, gözlenen geçiş zamanları (O) ile sabit dönemle hesaplanan zamanlar (C) arasındaki farkın çizildiği O−C diyagramıyla incelenir. Dönem sabit bir hızla değişiyorsa O−C diyagramı bir parabol çizer. Bugüne kadar gelgit bozulması kesin olarak gösterilmiş tek sistem WASP-12 b'dir (Yee vd., 2020; Winn ve Stefánsson, 2025). Wang vd. (2024), TESS (Ricker vd., 2015) verilerini literatürdeki zamanlarla birleştirerek 326 sıcak Jüpiteri incelemiş ve 26 dönem değişimi adayı bildirmiştir. Bu adaylardan 14'ü, sonucun tek bir ölçüme bağlı olup olmadığını sınayan LOOCV (Leave-One-Out Cross-Validation) testini geçmiştir.

Bu tür adaylarda bildirilen dönem değişimleri yeni verilerle her zaman doğrulanamamaktadır. Örneğin TrES-5 b'de birçok çalışmada bildirilen dönem kısalması, yeni gözlemler eklendiğinde belirgin biçimde zayıflamış (Rothmeier vd., 2025); WASP-22 b için bildirilen hızlı kısalma da 2026 yılında alınan TESS verileriyle doğrulanamamıştır (Stinga, 2026). Literatür zamanlarındaki zaman sistemi karışıklıkları, gerçekçi olmayan küçük ölçüm hataları ve tek tük aykırı ölçümler de sahte dönem değişimleri üretebilmektedir (Adams vd., 2024). Bu nedenle bir dönem değişiminin gerçek olup olmadığını anlamanın en güvenilir yolu, sonucu daha önce kullanılmamış yeni verilerle sınamaktır.

Bu projede incelenecek iki sistem bu sorunun iyi örnekleridir. WASP-45 b için Wang vd. (2024) yılda yaklaşık 169 ms'lik hızlı bir dönem kısalması bulmuştur. Sodickson ve Grunblatt (2025) ise aynı sistemde çok daha küçük bir değer bulmuş, verinin seyrek olduğunu, ölçüm hatalarının küçük verilmiş olabileceğini ve sistemde geçiş zamanlarını etkileyebilecek ek bir yıldız bulunduğunu belirterek bu sonucun fiziksel bir değişimi göstermediğini düşünmüştür. WASP-46 b için Petrucci vd. (2018) anlamlı bir değişim bulmamış ve geçiş zamanlarındaki saçılmanın yıldızın manyetik etkinliğinden kaynaklanabileceğini belirtmiştir. Davoudi vd. (2021) dönemin arttığını bildirmiş, Wang vd. (2024) yılda yaklaşık 52 ms'lik bir artış bulmuş; Adams vd. (2024) ve Kutluay vd. (2026) ise anlamlı bir değişim bulamamıştır.

Bu projenin özgün yanı, iki sistemin incelediğimiz yayınlarda kullanılmamış TESS verileriyle yeniden incelenmesidir. WASP-45 b için 2023, 2025 ve 2026 yıllarında gözlenen 69, 96, 106 ve 107. sektörler; WASP-46 b için 2025 ve 2026 yıllarında gözlenen 94, 95, 102, 103, 104 ve 105. sektörler MAST arşivinde bulunmaktadır. Projenin sorusu, bu yeni verilerle iki sistemin yörünge dönemlerinin anlamlı biçimde değişip değişmediğidir. WASP-45 b'de Wang vd.'nin bulduğu hızlı kısalma gerçekse yeni geçişler doğrusal efemerise göre belirgin biçimde erken gelmelidir; gelmiyorsa Sodickson ve Grunblatt'ın yorumu desteklenecektir. WASP-46 b'de ise değişimin olmadığı, sabit hızla arttığı ya da yıldızın manyetik etkinliğiyle ilişkili çevrimsel bir yapı gösterdiği durumlar birbirinden ayırt edilecektir. Anlamlı bir değişim bulunursa olası nedenleri, geçiş zamanları ve yayımlanmış sistem parametreleriyle sınanabilen mekanizmalar üzerinden değerlendirilecektir. Uzak bir eşlikçinin sabit ivmesinden kaynaklanan ışık-zaman (Rømer) etkisi geçiş zamanlarında gelgit bozulmasıyla aynı izi bıraktığı ve ancak dikine hız verisiyle ayırt edilebildiği için (Bouma vd., 2020) bu projenin kapsamı dışındadır; bu sınırlama sonuçların yorumunda açıkça belirtilecektir.

Proje, On İkinci Kalkınma Planı'nın (2024–2028) temel bilimlere özel önem verilmesini ve uzay araştırmalarını kritik alanlar arasında sayan hedefiyle (madde 270) ve genç nesillerin uzay alanında çalışmaya teşvik edilmesini öngören hedefiyle (madde 271) ilişkilidir (T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı, 2023). 2030 Sanayi ve Teknoloji Stratejisi de TÜBİTAK araştırma desteklerinin astronomi dahil temel bilimlerde artırılmasını öngörmektedir (T.C. Sanayi ve Teknoloji Bakanlığı, 2025). Proje, bir uzay görevinin (TESS) yeni verilerini işleyen ve yorumlayan lisans düzeyinde araştırmacılar yetiştirerek bu hedeflere katkı sağlayacaktır.

## 1.2. Amaç ve Hedefler

Projenin amacı, WASP-45 b ve WASP-46 b sistemlerinde yörünge dönemi değişiminin var olup olmadığını yeni TESS verileriyle sınamak ve değişim varsa olası nedenlerini değerlendirmektir.

**Hedef 1 (Veri seti):** İki sistem için yayımlanmış geçiş zamanlarını ve yer gözlemlerini tek bir tabloda toplamak, tüm zamanları BJD_TDB sistemine dönüştürmek ve yeni TESS sektörlerindeki (WASP-45 b: 69, 96, 106, 107; WASP-46 b: 94, 95, 102–105) tam geçişlerin orta geçiş zamanlarını ölçmek.

**Hedef 2 (O−C diyagramları):** İki sistem için O−C diyagramını oluşturmak; doğrusal ve kuadratik modelleri karşılaştırarak dönem değişim hızını (dP/dt) belirsizliğiyle birlikte vermek, yeni zamanların daha önce bildirilen değişimi doğrulayıp doğrulamadığını göstermek ve değişimin anlamlı olup olmadığına karar vermek.

**Hedef 3 (Güncel efemeris):** İki sistem için güncel efemerisleri (T0, P ve anlamlı ise dP/dt) belirlemek.

**Hedef 4 (Olası nedenler):** Dönem değişimi bulunursa gelgit bozulması, apsis hareketi, Applegate mekanizması, üçüncü cisim ve kütle kaybı mekanizmalarını önceden belirlenmiş ölçütlerle değerlendirmek ve sonuçları bir tabloda toplamak.

# 2. Yöntem

Proje, açık arşivlerdeki verilere dayanan gözlemsel bir çalışmadır; yeni gözlem yapılmayacaktır. Bağımsız değişken çevrim sayısı (E), bağımlı değişken gözlenen orta geçiş zamanı ve ondan hesaplanan O−C değeridir. Hesaplanacak temel büyüklük yörünge dönemindeki değişim hızıdır (dP/dt). Zaman sistemi, ölçüm belirsizliği ve verinin kaynağı kontrol edilen değişkenlerdir.

**2.1. Veri**

Her sistem için geçiş zamanları dört kaynaktan derlenecektir: Ivshina ve Winn (2022) ile Wang vd. (2024)'nin TESS zamanları, sisteme özel yayınlarda verilen zamanlar (WASP-45 b için Sodickson ve Grunblatt, 2025; WASP-46 b için Petrucci vd., 2018 ve Kutluay vd., 2026), yer gözlemi veritabanları olan ETD/VarAstro (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023), ve proje kapsamında ölçülecek yeni TESS zamanları. Katalog tabloları VizieR'den (Ochsenbein vd., 2000), sistem parametreleri NASA Exoplanet Archive'dan (Akeson vd., 2013), TESS ışık eğrileri MAST'tan alınacaktır.

Farklı çalışmalar zamanları farklı sistemlerde verdiğinden her zamanın sistemi kaynak makaleden kontrol edilecek ve HJD ya da BJD_UTC olarak verilen zamanlar Astropy (Astropy Collaboration vd., 2022) ile BJD_TDB sistemine dönüştürülecektir. Zaman sistemi belirlenemeyen zamanlar ayrıca işaretlenecek ve analiz bu zamanlarla ve onlar olmadan iki kez yapılacaktır. ETD verilerinden yalnızca veri kalitesi yüksek olarak işaretlenmiş tam geçişler kullanılacaktır.

**2.2. TESS Verilerinin Analizi ve Orta Geçiş Zamanlarının Belirlenmesi**

Daha önce yayımlanmış TESS zamanları yeniden ölçülmeyecek, yayımlandıkları tablolardan alınacaktır. Yalnızca incelenen yayınlarda kullanılmamış sektörler (WASP-45 b: 69, 96, 106, 107; WASP-46 b: 94, 95, 102–105) analiz edilecektir. Bu sektörlerin 2 dakikalık ışık eğrileri MAST'tan indirilecek, kalitesi düşük olarak işaretlenmiş ölçümler çıkarılacak ve her geçişin çevresindeki geçiş dışı akı düzeyine göre normalize edilecektir. Geçiş modeli batman paketiyle (Kreidberg, 2015) oluşturulacaktır. Önce bir sektördeki tüm geçişler evreye göre birleştirilerek gezegen-yıldız yarıçap oranı, a/R* ve yörünge eğim açısı belirlenecek; ardından her geçiş için bu değerler sabit tutularak yalnızca orta geçiş zamanı uyumlanacaktır. Orta geçiş zamanının belirsizliği emcee paketiyle yapılan Markov Zinciri Monte Carlo (MCMC) örneklemesinden (Foreman-Mackey vd., 2013) elde edilecektir. Kenar kararması katsayıları literatürden alınıp sabit tutulacak, verisi eksik olan kısmi geçişler kullanılmayacaktır.

**2.3. O−C Diyagramlarının Oluşturulması**

Her geçiş için çevrim sayısı E ve hesaplanan zaman C = T0 + P·E bulunacak, gözlenen zamandan çıkarılarak O−C değeri elde edilecektir. Burada T0 referans geçiş zamanı, P yörünge dönemidir. Zamanlara iki model, ölçüm hatalarıyla ağırlıklandırılmış en küçük kareler yöntemiyle uyumlanacaktır:

Doğrusal model (sabit dönem): T(E) = T0 + P·E

Kuadratik model (sabit hızla değişen dönem): T(E) = T0 + P·E + ½·(dP/dE)·E²

Dönem değişim hızı dP/dt = (1/P)·(dP/dE) bağıntısıyla hesaplanacaktır. Modelden 5σ'dan fazla sapan aykırı noktalar ayıklanacaktır. Literatür zamanları ile TESS zamanlarının ölçüm hataları ayrı ayrı ele alınacak; bir grubun artıklarının indirgenmiş χ² değeri 1'den büyükse o grubun hataları bu değer 1 olacak şekilde büyütülecektir. İki model χ² ve Bayes Bilgi Kriteri (BIC = χ² + k·ln n; Schwarz, 1978) istatistikleriyle karşılaştırılacaktır; burada k modeldeki parametre sayısı, n zaman sayısıdır. Wang vd. (2024) ile aynı ölçüt kullanılarak, kuadratik model doğrusal modelden ΔBIC > 10 farkla daha iyiyse ve dP/dt sıfırdan en az 3σ farklıysa dönem değişimi anlamlı kabul edilecektir. Ayrıca yeni TESS zamanlarının, yalnızca eski verilerle bulunan doğrusal ve kuadratik efemerislerden ne kadar saptığı ayrı ayrı hesaplanacaktır; bu karşılaştırma, daha önce bildirilen değişimin yeni verilerle doğrulanıp doğrulanmadığını doğrudan gösterecektir. Anlamlı değişim yoksa doğrusal model, varsa kuadratik model güncel efemeris olarak verilecektir.

**2.4. Olası Fiziksel Mekanizmalar**

Dönem değişimi anlamlı bulunursa aşağıdaki beş mekanizma, geçiş zamanları ve yayımlanmış sistem parametreleri (Mp, M*, R*, a) kullanılarak değerlendirilecektir. Bu parametreler NASA Exoplanet Archive'dan alınacaktır.

**2.4.1. Gelgit Bozulması (Orbital Decay)**

Gelgit bozulmasında dönem değişim hızı yıldızın gelgit kalite faktörüne bağlıdır (Patra vd., 2017):

dP/dt = −(27π / 2Q′*)·(Mp/M*)·(R*/a)⁵

Burada Mp gezegenin kütlesi, M* yıldızın kütlesi, R* yıldızın yarıçapı, a yörüngenin yarı-büyük eksenidir. Bu bağıntıdan gözlenen değişimi açıklamak için gereken Q′* hesaplanacak ve literatürdeki değerlerle (Penev vd., 2018) karşılaştırılacaktır. Yıldız gezegenin yörünge hareketinden yavaş döndüğünde gelgit dönemi yalnızca kısaltabileceği için, dönemi uzayan bir sistemde gelgit bozulması dışlanacaktır (Wang vd., 2024). Sabit ivmeli ışık-zaman etkisi dışlanamadığı için gelgit bozulması bu projede en fazla "olası" olarak değerlendirilebilecektir.

**2.4.2. Apsis Hareketi (Eksen Dönmesi)**

Yörünge dışmerkez ise yörüngenin büyük ekseni zamanla döner ve geçiş zamanlarında çevrimsel bir değişim oluşur. Geçiş zamanları şu bağıntıyla verilir (Patra vd., 2017):

t_geçiş(E) = T0 + Ps·E − (e·Pa/π)·cos ω(E), ω(E) = ω0 + (dω/dE)·E, Ps = Pa·[1 − (dω/dE)/2π]

Burada e dışmerkezlik, ω enberi boylamı, dω/dE enberi boylamının çevrim başına değişimi, Pa anomalistik dönem, Ps yıldızıl dönemdir. Bu model geçiş zamanlarına doğrudan uyumlanacak ve doğrusal ve kuadratik modellerle BIC istatistiği üzerinden karşılaştırılacaktır. Modelden bulunan dışmerkezlik, sistemin yayımlanmış yörünge parametreleriyle (Anderson vd., 2012) karşılaştırılacak; çok küçük bir dışmerkezlikle açıklanamayacak kadar büyük bir değişim varsa apsis hareketi olası görülmeyecektir.

**2.4.3. Applegate Mekanizması**

Yıldızın manyetik aktivite döngüsü kütle dağılımını değiştirir ve yörünge döneminde çevrimsel bir değişim yaratır (Applegate, 1992; Watson ve Marsh, 2010):

ΔP/P = −9·(R*/a)²·ΔQ/(M*·R*²) ve A = (P_mod/2π)·(ΔP/P)

Burada ΔQ yıldızın kuadrupol momentindeki değişim, P_mod aktivite döngüsünün süresi, A O−C diyagramındaki değişimin genliğidir. Gözlenen değişimi üretmek için gereken ΔQ ve buna karşılık gelen enerji, yıldızın ışınım gücüyle karşılaştırılacaktır. Manyetik etkinliği bilinen WASP-46 b'de (Petrucci vd., 2018) bu mekanizmaya özellikle bakılacaktır.

**2.4.4. Üçüncü Cisim**

Sisteme bağlı üçüncü bir cisim, ortak kütle merkezi etrafındaki dolanma nedeniyle O−C diyagramında çevrimsel bir ışık-zaman değişimi oluşturur; bu değişim gözlem süresi içinde bir ya da daha fazla çevrim tamamladığında geçiş zamanlarından belirlenebilir. Kuadratik modelin artıklarında Lomb-Scargle periyodogramıyla (Lomb, 1976; Scargle, 1982) periyodik sinyal aranacak; yanlış alarm olasılığı 0,01'den küçük olan sinyaller dikkate alınacak, gözlem mevsiminden kaynaklanan yaklaşık bir yıllık sinyaller dışarıda bırakılacaktır. Sinyal bulunursa yarı genliği A ve dönemi P₃ kullanılarak üçüncü cismin kütle fonksiyonu hesaplanacaktır (Irwin, 1952):

f(M₃) = 4π²·(A·c)³ / (G·P₃²) = (M₃·sin i₃)³ / (M* + Mp + M₃)²

Burada M₃ üçüncü cismin kütlesi, i₃ yörüngesinin eğim açısı, c ışık hızı, G kütle çekim sabitidir. WASP-45 sisteminde bulunduğu bildirilen ek yıldız (Sodickson ve Grunblatt, 2025) bu değerlendirmede dikkate alınacaktır.

**2.4.5. Kütle Kaybı**

Gezegen yıldızına Roche sınırı kadar yaklaşırsa kütle kaybedebilir ve bu durum yörüngeyi değiştirebilir. Roche sınırı a_Roche ≈ 2,16·Rp·(M*/Mp)^(1/3) bağıntısıyla (Ford ve Rasio, 2006) hesaplanacaktır; burada Rp gezegenin yarıçapıdır. a/a_Roche oranı 1'e yakın olan sistemlerde kütle kaybının katkısı tartışılacak, bu oranın belirgin biçimde büyük olduğu sistemlerde ihmal edilecektir.

Her mekanizma için sonuç "dışlandı", "olası değil", "olası" ya da "ayırt edilemedi" olarak verilecek ve iki sistemin sonuçları bir tabloda toplanacaktır. Uzak bir eşlikçinin sabit ivmesinden kaynaklanan ışık-zaman (Rømer) etkisi dikine hız verisi gerektirdiğinden değerlendirilmeyecek ve sonuç tablosunda kapsam dışı olarak belirtilecektir.

**2.5. Hedeflerin Seçimi (Ön Çalışma)**

Ön çalışma olarak yalnızca hedef seçimi yapılmıştır. Wang vd. (2024)'nin LOOCV testini geçen 14 adayı iki ölçüte göre incelenmiştir. Birinci ölçüt, adayın son yayımlanmış zamanlama çalışmasından sonra TESS tarafından yeniden gözlenmiş ve bu verilerin incelediğimiz yayınlarda kullanılmamış olmasıdır; yeni verinin zaman olarak yayılması için en az iki yeni sektör aranmış, verisi kullanılamadığı bildirilen sektörler dikkate alınmamıştır. Bunun için her adayın TESS sektörleri MAST arşivinde tek tek kontrol edilmiş ve son çalışmalarda kullanılan sektörlerle karşılaştırılmıştır. İkinci ölçüt, literatürde dönem değişiminin var olup olmadığı ya da büyüklüğü konusunda çelişkili sonuçlar bulunmasıdır. Çelişkinin yalnızca değişimin nedeni üzerine olduğu ve çözümü için dikine hız verisi gereken adaylar bu projenin kapsamına alınmamıştır. İki ölçütü sağlayan iki aday seçilmiştir (Tablo 1). Yöntemin adımları, çalışma takvimindeki iş paketleriyle aynı sırayla yürütülecektir.

# 3. Proje Yönetimi

## 3.1. Çalışma Takvimi

| Tarih Aralığı | Faaliyetler | Kim(ler) | Başarı Ölçütü ve Katkısı |
|---|---|---|---|
| 1.–2. ay | İP1: Yayımlanmış geçiş zamanlarının ve yer gözlemlerinin derlenmesi; zamanların BJD_TDB sistemine dönüştürülmesi | İdris Avlar (proje yürütücüsü; zaman sistemi dönüşümleri); Bahar Cayib (proje ortağı; zamanların ve kaynaklarının tabloya girilmesi); Hüseyin Er (akademik danışman) | İki sistem için kaynakları belirtilmiş, tümü BJD_TDB sisteminde bir zaman tablosu; zaman sistemi belirsiz kaynaklar işaretli (%20) |
| 3.–5. ay | İP2: Yeni TESS sektörlerinden (WASP-45 b: 69, 96, 106, 107; WASP-46 b: 94, 95, 102–105) orta geçiş zamanlarının ölçülmesi | İdris Avlar (proje yürütücüsü; ışık eğrisi modellemesi ve zaman ölçümü); Bahar Cayib (proje ortağı; ışık eğrilerinin indirilmesi ve geçişlerin gözle kontrolü) | Bu sektörlerdeki tüm tam geçişler için belirsizliğiyle birlikte orta geçiş zamanı (%30) |
| 6.–8. ay | İP3: O−C diyagramlarının oluşturulması; doğrusal ve kuadratik modellerin karşılaştırılması; yeni zamanların eski efemerislerle karşılaştırılması; güncel efemerislerin belirlenmesi | İdris Avlar (proje yürütücüsü; model uyumlama ve istatistiksel karşılaştırma); Bahar Cayib (proje ortağı; O−C diyagramlarının çizilmesi); Hüseyin Er (akademik danışman) | İki sistem için dP/dt ± σ, ΔBIC, "anlamlı değişim var/yok" kararı ve güncel efemeris (%30) |
| 9.–11. ay | İP4: Gelgit bozulması, apsis hareketi, Applegate mekanizması, üçüncü cisim ve kütle kaybının değerlendirilmesi | İdris Avlar (proje yürütücüsü; mekanizma testleri); Bahar Cayib (proje ortağı; sistem parametrelerinin derlenmesi); Hüseyin Er (akademik danışman) | Dönem değişimi bulunan sistem için beş mekanizmanın sonucunu gerekçesiyle veren tablo; değişim bulunmazsa sonucun gerekçesi (%20) |

## 3.2. Risk Yönetimi

| En Önemli Riskler | Alınacak Tedbirler (B Planı) |
|---|---|
| Literatürdeki zamanlarda zaman sistemi belirsizliği ya da gerçekçi olmayan küçük ölçüm hataları sahte bir dönem değişimi üretebilir. | Her zamanın sistemi kaynak makaleden kontrol edilecek; belirsiz zamanlarla ve onlar olmadan iki ayrı analiz yapılacak; ölçüm hataları her veri grubu için indirgenmiş χ² ile ölçeklenecektir. |
| Bazı yayınlardaki geçiş zamanları tablo olarak verilmemiş olabilir. | Bu zamanların ait olduğu TESS sektörleri aynı yöntemle (2.2) ölçülecektir; yöntemin geri kalanı değişmez. |
| Sönük yıldızlarda (özellikle WASP-46) tek tek geçişlerin orta zaman belirsizliği büyük olabilir. | Tek tek ölçülemeyen geçişler için sektördeki tüm geçişler birlikte uyumlanarak sektör başına bir orta geçiş zamanı elde edilecektir. |
| WASP-45 sistemindeki ek yıldızın ışığı geçiş derinliğini ve zaman ölçümünü etkileyebilir. | Ek yıldızın katkısı TESS veri işleme hattının sağladığı ışık karışımı düzeltmesiyle ve yayımlanmış parametrelerle kontrol edilecek; geçiş şekli sektörler arasında karşılaştırılacaktır. |
| Proje sürerken yeni TESS verilerini kullanan başka bir çalışma yayımlanabilir. | Yayınlar düzenli olarak izlenecek; yeni çalışmanın sonuçları kendi sonuçlarımızla karşılaştırılacak ve bu karşılaştırma raporda verilecektir. |
| Güncel verilerle anlamlı dönem değişimi bulunmayabilir. | Bu durum araştırma sorusunun bir cevabı olarak raporlanacak, doğrusal efemeris verilecek ve daha önce bildirilen değişimin neden bulunamadığı tartışılacaktır. |
| İş paketlerinde gecikme yaşanabilir. | İş paketleri ardışık planlanmış ve 12. ay tampon olarak bırakılmıştır; ilerleme danışmanla düzenli görüşmelerle izlenecektir. |
| Yazılım ya da bilgisayar arızası yaşanabilir. | Kod ve veriler düzenli olarak yedeklenecek; analizler ücretsiz çevrim içi Python ortamlarında da çalışabilecek şekilde hazırlanacaktır. |

## 3.3. Araştırma Olanakları

| Kuruluşta Bulunan Altyapı/Ekipman Türü, Modeli | Projede Kullanım Amacı |
|---|---|
| Proje yürütücüsünün kişisel dizüstü bilgisayarı ile üniversite kütüphanesindeki bilgisayarlar ve internet erişimi | Veri indirme, ışık eğrisi analizi ve O−C analizleri |
| Açık erişimli veri arşivleri: MAST (TESS), VizieR, NASA Exoplanet Archive, ETD/VarAstro, ExoClock | Geçiş zamanları, ışık eğrileri ve sistem parametreleri |
| Açık kaynak yazılımlar: Python, NumPy, Astropy, astroquery, batman, emcee | Tüm analizlerin ücretsiz ve tekrarlanabilir biçimde yapılması |

# 4. Araştırma Önerisinin Yaygın Etkisi

| Çıktı, Etki ve Kazanımlar | Öngörülen Çıktı(lar), Etki(ler) ve Kazanım(lar) |
|---|---|
| Bilimsel/Akademik Çıktılar | İki sistemin yeni TESS verileriyle güncellenmiş O−C analizini ve dönem değişiminin varlığı ile olası nedenlerine ilişkin sonuç tablosunu içeren proje sonuç raporu. Sonuçların, yeterli görülmesi halinde danışmanla birlikte kısa bir makale olarak sunulması hedeflenmektedir. |
| Ekonomik/Ticari/Sosyal Çıktılar | İki sistemin tüm geçiş zamanlarını (yeni TESS zamanları dahil) BJD_TDB sisteminde içeren açık erişimli veri seti, analiz kodu ve güncel efemerisler. Bu çıktılar gelecekteki geçiş gözlemlerinin planlanmasında kullanılabilecektir. Danışmanın uygun görmesi halinde bölüm öğrencilerine yönelik kısa bir O−C analizi tanıtım sunumu yapılması hedeflenmektedir. |
| Yeni Proje(ler) Oluşturmasına Yönelik Çıktılar | Aynı yöntemin Wang vd. (2024)'nin diğer adaylarına, yeni TESS verileri geldikçe uygulanmasıyla olası bir lisansüstü tez çalışmasına temel oluşturulması. |

# 5. Belirtmek İstediğiniz Diğer Konular

Aşağıdaki tablo, yöntem bölümünde (2.5) anlatılan hedef seçiminin sonucudur.

**Tablo 1.** Hedef seçim tablosu. Satırlar, Wang vd. (2024)'nin dönem değişimi bildirdiği 26 adaydan LOOCV testini geçen 14 adaydır (Wang vd., 2024, Tablo 3). dP/dt değerleri Wang vd. (2024)'ten alınmıştır. "Son zamanlama çalışması" sütunu, incelediğimiz yayınlar arasında aday için TESS verisi kullanan en son çalışmayı gösterir. "Kullanılmamış TESS sektörleri" sütunu, MAST arşivindeki sektörlerin bu çalışmalarda kullanılanlarla karşılaştırılmasıyla belirlenmiştir. Seçim ölçütleri: (1) en az iki kullanılmamış ve kullanılabilir TESS sektörü; (2) literatürde dönem değişiminin varlığı ya da büyüklüğü konusunda çelişkili sonuçlar (yalnızca nedeni tartışmalı olan ve dikine hız verisi gerektiren adaylar kapsam dışı). "–": aday birinci ölçütte elendiği için ikinci ölçüte bakılmadı.

| Aday | Wang vd. dP/dt (ms/yıl) | Son zamanlama çalışması | Kullanılmamış TESS sektörleri | Literatürdeki çelişki | Sonuç |
|---|---|---|---|---|---|
| CoRoT-2 b | −21,7 ± 3,0 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| HAT-P-37 b | −34,3 ± 6,7 | Wang vd. (2024) | 74, 75, 80, 82 (kullanılabilirliği şüpheli) | – | Elendi: TESS verisi arka plan kirliliği nedeniyle büyük ölçüde kullanılamıyor (Wang vd., 2024) |
| KELT-16 b | −27,8 ± 4,8 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| TrES-1 b | −14,8 ± 2,4 | Kutluay vd. (2026) | 81 | – | Elendi: tek sektör |
| TrES-5 b | −9,7 ± 2,1 | Rothmeier vd. (2025) | Yok | – | Elendi: yeni veri yok |
| WASP-4 b | −6,4 ± 0,6 | Winn ve Stefánsson (2025) | 103, 105, 106 | Yalnızca nedeni üzerine (gelgit / ışık-zaman) | Elendi: dikine hız verisi gerektiriyor |
| WASP-10 b | −27,7 ± 3,5 | Wang vd. (2024) | 83 | – | Elendi: tek sektör |
| WASP-12 b | −30,2 ± 0,9 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| WASP-22 b | −71,8 ± 17,1 | Stinga (2026) | Yok | – | Elendi: yeni veri yok |
| WASP-45 b | −169,2 ± 21,1 | Sodickson ve Grunblatt (2025) | 69, 96, 106, 107 | Değişimin büyüklüğü ve gerçekliği | **Seçildi** |
| XO-4 b | −62,6 ± 17,5 | Wang vd. (2024) | 74 | – | Elendi: tek sektör |
| HAT-P-7 b | +18,3 ± 4,1 | Yang vd. (2025) | Yok | – | Elendi: yeni veri yok |
| WASP-1 b | +22,5 ± 5,2 | Sodickson ve Grunblatt (2025) | En fazla bir (84) | – | Elendi: tek sektör |
| WASP-46 b | +51,7 ± 2,9 | Kutluay vd. (2026) | 94, 95, 102–105 | Değişimin varlığı | **Seçildi** |

# 6. Ekler — EK-1: Kaynaklar

- Adams, E. R. vd. 2024. "Doomed Worlds. I. No New Evidence for Orbital Decay in a Long-term Survey of 43 Ultrahot Jupiters", The Planetary Science Journal, 5, 163. https://doi.org/10.3847/PSJ/ad3e80
- Akeson, R. L. vd. 2013. "The NASA Exoplanet Archive: Data and Tools for Exoplanet Research", Publications of the Astronomical Society of the Pacific, 125, 989-999. https://doi.org/10.1086/672273
- Anderson, D. R. vd. 2012. "WASP-44b, WASP-45b and WASP-46b: Three Short-period, Transiting Extrasolar Planets", Monthly Notices of the Royal Astronomical Society, 422, 1988-1998. https://doi.org/10.1111/j.1365-2966.2012.20635.x
- Applegate, J. H. 1992. "A Mechanism for Orbital Period Modulation in Close Binaries", The Astrophysical Journal, 385, 621. https://doi.org/10.1086/170967
- Astropy Collaboration vd. 2022. "The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package", The Astrophysical Journal, 935, 167. https://doi.org/10.3847/1538-4357/ac7c74
- Bouma, L. G. vd. 2020. "WASP-4 Is Accelerating toward the Earth", The Astrophysical Journal Letters, 893, L29. https://doi.org/10.3847/2041-8213/ab8563
- Davoudi, F. vd. 2021. "Refined Ephemeris for Four Hot Jupiters Using Ground-Based and TESS Observations", Astronomy Letters, 47, 638-650. https://doi.org/10.1134/S1063773721090024
- Ford, E. B. ve Rasio, F. A. 2006. "On the Relation between Hot Jupiters and the Roche Limit", The Astrophysical Journal, 638, L45-L48. https://doi.org/10.1086/500734
- Foreman-Mackey, D. vd. 2013. "emcee: The MCMC Hammer", Publications of the Astronomical Society of the Pacific, 125, 306-312. https://doi.org/10.1086/670067
- Irwin, J. B. 1952. "The Determination of a Light-Time Orbit", The Astrophysical Journal, 116, 211. https://doi.org/10.1086/145604
- Ivshina, E. S. ve Winn, J. N. 2022. "TESS Transit Timing of Hundreds of Hot Jupiters", The Astrophysical Journal Supplement Series, 259, 62. https://doi.org/10.3847/1538-4365/ac545b
- Kokori, A. vd. 2023. "ExoClock Project. III. 450 New Exoplanet Ephemerides from Ground and Space Observations", The Astrophysical Journal Supplement Series, 265, 4. https://doi.org/10.3847/1538-4365/ac9da4
- Kreidberg, L. 2015. "batman: BAsic Transit Model cAlculatioN in Python", Publications of the Astronomical Society of the Pacific, 127, 1161-1165. https://doi.org/10.1086/683602
- Kutluay, A. C. vd. 2026. "Chasing the Tides: Searching for Orbital Decay Signatures in Transit Timing Data and Tidal Models for 20 Hot Jupiters", Publications of the Astronomical Society of the Pacific, 138, 024405. https://doi.org/10.1088/1538-3873/ae406a
- Lomb, N. R. 1976. "Least-squares Frequency Analysis of Unequally Spaced Data", Astrophysics and Space Science, 39, 447-462. https://doi.org/10.1007/BF00648343
- MAST (Mikulski Archive for Space Telescopes), Space Telescope Science Institute. https://archive.stsci.edu, Son erişim tarihi: 8 Kasım 2026.
- Ochsenbein, F., Bauer, P. ve Marcout, J. 2000. "The VizieR Database of Astronomical Catalogues", Astronomy and Astrophysics Supplement Series, 143, 23-32. https://doi.org/10.1051/aas:2000169
- Patra, K. C. vd. 2017. "The Apparently Decaying Orbit of WASP-12b", The Astronomical Journal, 154, 4. https://doi.org/10.3847/1538-3881/aa6d75
- Penev, K. vd. 2018. "Empirical Tidal Dissipation in Exoplanet Hosts from Tidal Spin-up", The Astronomical Journal, 155, 165. https://doi.org/10.3847/1538-3881/aaaf71
- Petrucci, R. vd. 2018. "A Search for Transit Timing Variations and Orbital Decay in WASP-46b", Monthly Notices of the Royal Astronomical Society, 473, 5126-5141. https://doi.org/10.1093/mnras/stx2647
- Poddaný, S., Brát, L. ve Pejcha, O. 2010. "Exoplanet Transit Database. Reduction and Processing of the Photometric Data of Exoplanet Transits", New Astronomy, 15, 297-301. https://doi.org/10.1016/j.newast.2009.09.001
- Ricker, G. R. vd. 2015. "Transiting Exoplanet Survey Satellite", Journal of Astronomical Telescopes, Instruments, and Systems, 1, 014003. https://doi.org/10.1117/1.JATIS.1.1.014003
- Rothmeier, M. vd. 2025. "Doomed Worlds. II. Reassessing Suggestions of Orbital Decay for TrES-5 b", The Planetary Science Journal, 6, 292. https://doi.org/10.3847/PSJ/ae1b9c
- Scargle, J. D. 1982. "Studies in Astronomical Time Series Analysis. II. Statistical Aspects of Spectral Analysis of Unevenly Spaced Data", The Astrophysical Journal, 263, 835. https://doi.org/10.1086/160554
- Schwarz, G. 1978. "Estimating the Dimension of a Model", The Annals of Statistics, 6, 461-464. https://doi.org/10.1214/aos/1176344136
- Sodickson, N. ve Grunblatt, S. 2025. "In Search of Decay: An Analysis of Transit Times of Hot Jupiters in Main-sequence and Post-main-sequence Systems", The Astrophysical Journal, 993, 78. https://doi.org/10.3847/1538-4357/adfd60
- Stinga, S. I. 2026. "TESS Transit Times from 2026 Do Not Confirm the Reported Orbital Decay of WASP-22 b", Research Notes of the AAS, 10, 297. https://doi.org/10.3847/2515-5172/aeb5e5
- T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. 2023. "On İkinci Kalkınma Planı (2024-2028)". https://www.sbb.gov.tr/wp-content/uploads/2023/12/On-Ikinci-Kalkinma-Plani_2024-2028_11122023.pdf, Son erişim tarihi: 8 Kasım 2026.
- T.C. Sanayi ve Teknoloji Bakanlığı. 2025. "2030 Sanayi ve Teknoloji Stratejisi". https://www.sanayi.gov.tr/assets/img/popup-image/pdf/SanayiTeknolojiStratejisi2030.pdf, Son erişim tarihi: 8 Kasım 2026.
- Wang, W. vd. 2024. "Long-term Variations in the Orbital Period of Hot Jupiters from Transit-timing Analysis Using TESS Survey Data", The Astrophysical Journal Supplement Series, 270, 14. https://doi.org/10.3847/1538-4365/ad0847
- Watson, C. A. ve Marsh, T. R. 2010. "Orbital Period Variations of Hot Jupiters Caused by the Applegate Effect", Monthly Notices of the Royal Astronomical Society, 405, 2037. https://doi.org/10.1111/j.1365-2966.2010.16602.x
- Winn, J. N. ve Stefánsson, G. 2025. "Orbital Decay Candidates Reconsidered: WASP-4 b Is Not Decaying and Kepler-1658 b Is Not a Planet", The Planetary Science Journal, 6, 300. https://doi.org/10.3847/PSJ/ae21db
- Yang, E., Su, Y. ve Winn, J. N. 2025. "A Third Star in the HAT-P-7 System and a New Dynamical Pathway to Misaligned Hot Jupiters", The Astrophysical Journal, 986, 117. https://doi.org/10.3847/1538-4357/add5f7
- Yee, S. W. vd. 2020. "The Orbit of WASP-12b Is Decaying", The Astrophysical Journal Letters, 888, L5. https://doi.org/10.3847/2041-8213/ab5c16
