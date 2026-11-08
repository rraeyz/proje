> BELGE B — Yeni gerekçe: kullanılmamış TESS verisi ve literatür çelişkisi. Hedefler: WASP-4 b, WASP-45 b, WASP-46 b. Dikine hız (RV) analizi dahil.

# A. Genel Bilgiler

| Alan | Değer |
|---|---|
| Başvuru Sahibinin Adı Soyadı | İdris Avlar |
| Araştırma Önerisinin Başlığı | Sıcak Jüpiterlerde Yörünge Dönemi Değişimlerinin Yeni TESS Verileri ve O−C Analiziyle İncelenmesi ve Fiziksel Kökenlerinin Belirlenmesi |
| Danışmanın Adı Soyadı | Hüseyin Er |
| Araştırmanın Yürütüleceği Kurum | Atatürk Üniversitesi, Fen Fakültesi, Astronomi ve Uzay Bilimleri Bölümü |

# Özet

Sıcak Jüpiterlerin yörünge dönemlerindeki değişimler, yıldız ile gezegen arasındaki gelgit etkileşimini gözlemle sınamanın az sayıdaki yolundan biridir. Bu değişimler geçiş zamanlarından oluşturulan O−C diyagramlarıyla izlenir. Son yıllarda TESS verileriyle birçok sistemde dönem değişimi bildirilmiş, ancak bu sonuçların bir kısmı yeni verilerle doğrulanamamıştır. Bu projede üç sıcak Jüpiter sistemi incelenecektir: WASP-4 b, WASP-45 b ve WASP-46 b. Sistemler, Wang vd. (2024)'nin bildirdiği dönem değişimi adayları arasından iki ölçütle seçilmiştir: TESS uydusunun bu sistemleri son yayımlanmış zamanlama çalışmalarından sonra yeniden gözlemiş olması ve literatürde dönem değişiminin varlığı ya da nedeni konusunda çelişkili sonuçlar bulunması. Üç sistemde de 2025–2026 yıllarında gözlenmiş ve incelediğimiz yayınlarda kullanılmamış TESS sektörleri bulunmaktadır. Her sistem için yayımlanmış geçiş zamanları ve yer gözlemleri derlenecek, tüm zamanlar BJD_TDB sistemine dönüştürülecek ve yeni TESS sektörlerinden orta geçiş zamanları ölçülecektir. O−C diyagramlarına doğrusal ve kuadratik modeller uyumlanacak, modeller χ² ve Bayes Bilgi Kriteri (BIC) istatistikleriyle karşılaştırılacak ve her sistem için güncel efemeris belirlenecektir. Dönem değişimi bulunan sistemlerde gelgit bozulması, apsis hareketi, ışık-zaman etkisi, Applegate mekanizması, üçüncü cisim ve kütle kaybı kendi bağıntılarıyla sınanacak; gelgit bozulması ile ışık-zaman etkisi, yeterli dikine hız verisi olan sistemlerde arşivdeki ölçümlerden hesaplanan ivme ile ayırt edilecektir. Proje, yürütücü, proje ortağı ve danışmandan oluşan ekiple 12 ay içinde dört iş paketi halinde yürütülecek; yeni gözlem yapılmayacak ve bütçe gerekmemektedir. Proje sonunda üç sistem için güncel efemerisler, dönem değişiminin varlığı ve nedenine ilişkin bir sonuç tablosu ve açık erişimli bir veri seti elde edilecek; sonuçların danışmanla birlikte kısa bir makale olarak paylaşılması hedeflenmektedir.

**Anahtar Kelimeler:** Sıcak Jüpiter, geçiş zamanlaması, O−C diyagramı, TESS, gelgit bozulması

# 1. Araştırma Önerisinin Bilimsel Niteliği

## 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği

Sıcak Jüpiterler, Jüpiter kütlesinde olan ve yıldızlarının etrafında birkaç günde dolanan gezegenlerdir. Yıldıza çok yakın oldukları için yıldızda bir gelgit şişkinliği oluştururlar. Yıldız kendi ekseni etrafında gezegenin yörünge hareketinden daha yavaş dönüyorsa bu şişkinlik gezegeni yavaşlatır, gezegen yıldıza yaklaşır ve yörünge dönemi kısalır. Bu sürecin hızı yıldızın gelgit kalite faktörüne (Q′*) bağlıdır. Q′* için kuramsal ve gözlemsel tahminler birkaç mertebe farklılık gösterdiğinden (Penev vd., 2018), dönem değişiminin doğrudan ölçülmesi yıldızların iç yapısı hakkında da bilgi verir.

Dönem değişimi, gözlenen geçiş zamanları (O) ile sabit dönemle hesaplanan zamanlar (C) arasındaki farkın çizildiği O−C diyagramıyla incelenir. Dönem sabit bir hızla değişiyorsa O−C diyagramı bir parabol çizer. Bugüne kadar gelgit bozulması kesin olarak gösterilmiş tek sistem WASP-12 b'dir (Yee vd., 2020; Winn ve Stefánsson, 2025). Wang vd. (2024), TESS (Ricker vd., 2015) verilerini literatürdeki zamanlarla birleştirerek 326 sıcak Jüpiteri incelemiş ve 26 dönem değişimi adayı bildirmiştir. Bu adaylardan 14'ü, sonucun tek bir ölçüme bağlı olup olmadığını sınayan LOOCV (Leave-One-Out Cross-Validation) testini geçmiştir.

Bu tür adaylarda bildirilen dönem değişimleri yeni verilerle her zaman doğrulanamamaktadır. Örneğin TrES-5 b'de birçok çalışmada bildirilen dönem kısalması, yeni gözlemler eklendiğinde belirgin biçimde zayıflamış (Rothmeier vd., 2025); WASP-22 b için bildirilen hızlı kısalma da 2026 yılında alınan TESS verileriyle doğrulanamamıştır (Stinga, 2026). Literatür zamanlarındaki zaman sistemi karışıklıkları, gerçekçi olmayan küçük ölçüm hataları ve tek tük aykırı ölçümler de sahte dönem değişimleri üretebilmektedir (Adams vd., 2024). Bu nedenle bir dönem değişiminin gerçek olup olmadığını anlamanın en güvenilir yolu, sonucu daha önce kullanılmamış yeni verilerle sınamaktır. Değişimin gerçek olduğu durumda ise nedeni ayrıca belirlenmelidir, çünkü O−C diyagramındaki parabol tek başına nedenini göstermez. Uzak bir eşlikçi nedeniyle bakış doğrultusunda ivmelenen bir sistemde ışığın bize ulaşma süresi değişir ve geçiş zamanlarında gelgit bozulmasıyla aynı parabolik iz oluşur (Bouma vd., 2020). Bu iki mekanizma ancak yıldızın dikine hızındaki uzun dönemli değişimle ayırt edilebilir.

Bu projede incelenecek üç sistemde literatür bu sorulara farklı cevaplar vermektedir. WASP-45 b için Wang vd. (2024) yılda yaklaşık 169 ms'lik hızlı bir dönem kısalması bulmuştur. Sodickson ve Grunblatt (2025) ise aynı sistemde çok daha küçük bir değer (yılda yaklaşık 55 ms) bulmuş; verinin seyrek olması, ölçüm hatalarının küçük verilmiş olabilmesi ve sistemde ek bir yıldız bulunması nedeniyle bu sonucun büyük olasılıkla fiziksel bir değişimden kaynaklanmadığını belirtmiştir. Yeh vd. (2024), 32 geçiş zamanının ne sabit dönemle ne de kısalan dönemle iyi açıklanabildiğini bulmuş ve sistemi sınıflandıramamıştır. WASP-46 b için Petrucci vd. (2018) anlamlı bir değişim bulmamış, Davoudi vd. (2021) dönemin arttığını bildirmiş, Wang vd. (2024) yılda yaklaşık 52 ms'lik bir artış bulmuş; Adams vd. (2024) ve Kutluay vd. (2026) ise anlamlı bir değişim bulamamıştır. Petrucci vd. (2018), geçiş zamanlarındaki saçılmanın yıldızın manyetik etkinliğinden kaynaklanabileceğini de belirtmiştir. WASP-4 b'de dönem kısalması birçok çalışmada bulunmuştur, ancak nedeni tartışmalıdır. Bouma vd. (2020) dikine hızlarda bir ivme bularak değişimin büyük kısmını ışık-zaman etkisine bağlamış; Baluev vd. (2020) ve Turner vd. (2022) bu ivmeyi doğrulayamamıştır. Harre vd. (2023) ve Baştürk vd. (2025) değişimi gelgit bozulmasıyla açıklarken, Winn ve Stefánsson (2025) yeni dikine hız verileriyle değişimi uzak bir eşlikçinin ışık-zaman etkisine bağlamıştır.

Bu projenin özgün yanı, bu üç sistemin incelediğimiz yayınlarda kullanılmamış TESS verileriyle yeniden incelenmesidir. WASP-45 b için 2025 ve 2026 yıllarında gözlenen 96, 106 ve 107. sektörler; WASP-46 b için 2025 ve 2026 yıllarında gözlenen 94, 95, 102, 103, 104 ve 105. sektörler; WASP-4 b için ise 2026 yılında gözlenen 103, 105 ve 106. sektörler MAST arşivinde bulunmaktadır. Projenin sorusu, bu yeni verilerle üç sistemin yörünge dönemlerinin anlamlı biçimde değişip değişmediği ve değişiyorsa bunun hangi mekanizmadan kaynaklandığıdır. WASP-45 b'de Wang vd.'nin bulduğu hızlı kısalma gerçekse yeni geçişler doğrusal efemerise göre belirgin biçimde erken gelmelidir; gelmiyorsa Sodickson ve Grunblatt'ın yorumu desteklenecektir. WASP-46 b'de değişimin olmadığı, sabit hızla arttığı ya da yıldız etkinliğiyle ilişkili çevrimsel bir yapı gösterdiği durumlar birbirinden ayırt edilecektir. WASP-4 b'de ise yeni zamanlarla güncellenen dönem değişiminin dikine hızlardaki ivmeyle açıklanıp açıklanamayacağı sınanacaktır.

Proje, On İkinci Kalkınma Planı'nda (2024–2028) temel bilimlere özel önem verilmesini ve uzay araştırmalarını kritik alanlar arasında sayan madde 270, genç nesillerin uzay alanında çalışmaya teşvik edilmesini ve uzay araştırmalarının yaygınlaştırılmasını öngören madde 271 ve temel bilimlerde nitelikli araştırmacı insan gücünün ve araştırma faaliyetlerinin artırılmasını öngören madde 546 ile ilişkilidir (T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı, 2023). Proje, bir uzay görevinin (TESS) yeni verilerini işleyen ve yorumlayan lisans düzeyinde araştırmacılar yetiştirerek bu hedeflere katkı sağlayacaktır.

## 1.2. Amaç ve Hedefler

Projenin amacı, WASP-4 b, WASP-45 b ve WASP-46 b sistemlerinde yörünge dönemi değişiminin var olup olmadığını yeni TESS verileriyle sınamak ve değişim varsa nedenini belirlemektir.

**Hedef 1 (Veri seti):** Üç sistem için yayımlanmış geçiş zamanlarını ve yer gözlemlerini tek bir tabloda toplamak, tüm zamanları BJD_TDB sistemine dönüştürmek ve yeni TESS sektörlerindeki (WASP-4 b: 103, 105, 106; WASP-45 b: 96, 106, 107; WASP-46 b: 94, 95, 102–105) tam geçişlerin orta geçiş zamanlarını ölçmek.

**Hedef 2 (O−C diyagramları):** Her sistem için O−C diyagramını oluşturmak; doğrusal ve kuadratik modelleri karşılaştırarak dönem değişim hızını (dP/dt) belirsizliğiyle birlikte vermek ve değişimin anlamlı olup olmadığına karar vermek.

**Hedef 3 (Güncel efemeris):** Üç sistem için güncel efemerisleri (T0, P ve anlamlı ise dP/dt) belirlemek.

**Hedef 4 (Fiziksel mekanizmalar):** Dönem değişimi bulunan her sistem için gelgit bozulması, apsis hareketi, ışık-zaman etkisi, Applegate mekanizması, üçüncü cisim ve kütle kaybı mekanizmalarını önceden belirlenmiş ölçütlerle değerlendirmek ve sonuçları bir tabloda toplamak.

# 2. Yöntem

Proje, açık arşivlerdeki verilere dayanan gözlemsel bir çalışmadır; yeni gözlem yapılmayacaktır. Bağımsız değişken çevrim sayısı (E), bağımlı değişken gözlenen orta geçiş zamanı ve ondan hesaplanan O−C değeridir. Hesaplanacak temel büyüklük yörünge dönemindeki değişim hızıdır (dP/dt). Zaman sistemi, ölçüm belirsizliği ve verinin kaynağı kontrol edilen değişkenlerdir.

**2.1. Veri**

Her sistem için geçiş zamanları dört kaynaktan derlenecektir: Ivshina ve Winn (2022) ile Wang vd. (2024)'nin TESS zamanları, 1.1'de anılan sisteme özel zamanlama çalışmalarında verilen zamanlar, yer gözlemi veritabanları olan ETD/VarAstro (Poddaný vd., 2010) ve ExoClock (Kokori vd., 2023, 2026), ve proje kapsamında ölçülecek yeni TESS zamanları. Katalog tabloları VizieR'den (Ochsenbein vd., 2000), sistem parametreleri NASA Exoplanet Archive'dan (Akeson vd., 2013), TESS ışık eğrileri MAST'tan alınacaktır. Dikine hız ölçümleri yayımlanmış makale tablolarından (WASP-4 b için Turner vd., 2022 ve Winn ve Stefánsson, 2025; WASP-45 b ve WASP-46 b için Anderson vd., 2012) ve DACE arşivinden alınacaktır.

Farklı çalışmalar zamanları farklı sistemlerde verdiğinden her zamanın sistemi kaynak makaleden kontrol edilecek ve HJD ya da BJD_UTC olarak verilen zamanlar Astropy (Astropy Collaboration vd., 2022) ile BJD_TDB sistemine dönüştürülecektir. Zaman sistemi belirlenemeyen zamanlar ayrıca işaretlenecek ve analiz bu zamanlarla ve onlar olmadan iki kez yapılacaktır. ETD verilerinden yalnızca veri kalitesi yüksek olarak işaretlenmiş tam geçişler kullanılacaktır.

**2.2. TESS Verilerinin Analizi ve Orta Geçiş Zamanlarının Belirlenmesi**

Daha önce yayımlanmış TESS zamanları yeniden ölçülmeyecek, yayımlandıkları tablolardan alınacaktır. Yalnızca incelenen yayınlarda kullanılmamış sektörler (WASP-4 b: 103, 105, 106; WASP-45 b: 96, 106, 107; WASP-46 b: 94, 95, 102–105) analiz edilecektir. Bu sektörlerin 2 dakikalık ışık eğrileri MAST'tan indirilecek, kalitesi düşük olarak işaretlenmiş ölçümler çıkarılacak ve her geçişin çevresindeki geçiş dışı akı düzeyine göre normalize edilecektir. Geçiş modeli batman paketiyle (Kreidberg, 2015) oluşturulacaktır. Önce bir sektördeki tüm geçişler evreye göre birleştirilerek gezegen-yıldız yarıçap oranı, a/R* ve yörünge eğim açısı belirlenecek; ardından her geçiş için bu değerler sabit tutularak yalnızca orta geçiş zamanı uyumlanacaktır. Orta geçiş zamanının belirsizliği emcee paketiyle yapılan Markov Zinciri Monte Carlo (MCMC) örneklemesinden (Foreman-Mackey vd., 2013) elde edilecektir. Kenar kararması katsayıları literatürden alınıp sabit tutulacak, verisi eksik olan kısmi geçişler kullanılmayacaktır.

**2.3. O−C Diyagramlarının Oluşturulması**

Her geçiş için çevrim sayısı E ve hesaplanan zaman C = T0 + P·E bulunacak, gözlenen zamandan çıkarılarak O−C değeri elde edilecektir. Burada T0 referans geçiş zamanı, P yörünge dönemidir. Zamanlara iki model, ölçüm hatalarıyla ağırlıklandırılmış en küçük kareler yöntemiyle uyumlanacaktır:

Doğrusal model (sabit dönem): T(E) = T0 + P·E

Kuadratik model (sabit hızla değişen dönem): T(E) = T0 + P·E + ½·(dP/dE)·E²

Dönem değişim hızı dP/dt = (1/P)·(dP/dE) bağıntısıyla hesaplanacaktır. Modelden 5σ'dan fazla sapan aykırı noktalar ayıklanacaktır. Ölçüm hataları üç veri grubu (TESS zamanları, yayımlanmış yer gözlemleri, ETD ve ExoClock zamanları) için ayrı ayrı ele alınacak; bir grubun artıklarının indirgenmiş χ² değeri 1'den büyükse o grubun hataları bu değer 1 olacak şekilde büyütülecektir. İki model χ² ve Bayes Bilgi Kriteri (BIC = χ² + k·ln n; Schwarz, 1978) istatistikleriyle karşılaştırılacaktır; burada k modeldeki parametre sayısı, n zaman sayısıdır. Wang vd. (2024) ile aynı ölçüt kullanılarak, kuadratik model doğrusal modelden ΔBIC > 10 farkla daha iyiyse ve dP/dt sıfırdan en az 3σ farklıysa dönem değişimi anlamlı kabul edilecektir. Ayrıca yeni TESS zamanlarının, yalnızca eski verilerle bulunan doğrusal ve kuadratik efemerislerden ne kadar saptığı ayrı ayrı hesaplanacaktır; bu karşılaştırma, daha önce bildirilen değişimin yeni verilerle doğrulanıp doğrulanmadığını doğrudan gösterecektir. Anlamlı değişim yoksa doğrusal model, varsa kuadratik model güncel efemeris olarak verilecektir.

**2.4. Fiziksel Mekanizmalar**

Dönem değişimi anlamlı bulunan sistemlerde aşağıdaki altı mekanizma tek tek değerlendirilecektir. Gerekli sistem parametreleri (Mp, M*, R*, L*, a, e) NASA Exoplanet Archive'dan, yıldızın dönme dönemi yayımlanmış çalışmalardan alınacaktır.

**2.4.1. Gelgit Bozulması (Orbital Decay)**

Gelgit bozulmasında dönem değişim hızı yıldızın gelgit kalite faktörüne bağlıdır (Patra vd., 2017):

dP/dt = −(27π / 2Q′*)·(Mp/M*)·(R*/a)⁵

Burada Mp gezegenin kütlesi, M* yıldızın kütlesi, R* yıldızın yarıçapı, a yörüngenin yarı-büyük eksenidir. Bu bağıntıdan gözlenen değişimi açıklamak için gereken Q′* hesaplanacak ve literatürdeki değerlerle (Penev vd., 2018) karşılaştırılacaktır. Yıldızın dönme dönemi gezegenin yörünge döneminden uzunsa gelgit etkileşimi yörünge dönemini yalnızca kısaltabilir; bu nedenle yıldızı bu koşulu sağlayan ve dönemi uzayan bir sistemde gelgit bozulması dışlanacaktır (Wang vd., 2024).

**2.4.2. Apsis Hareketi (Eksen Dönmesi)**

Yörünge dışmerkez ise yörüngenin büyük ekseni zamanla döner ve geçiş zamanlarında çevrimsel bir değişim oluşur. Geçiş ve ikincil tutulma zamanları şu bağıntılarla verilir (Patra vd., 2017):

t_geçiş(E) = T0 + Ps·E − (e·Pa/π)·cos ω(E)

t_ikincil(E) = T0 + Pa/2 + Ps·E + (e·Pa/π)·cos ω(E)

ω(E) = ω0 + (dω/dE)·E ve Ps = Pa·[1 − (dω/dE)/2π]

Burada e dışmerkezlik, ω enberi boylamı, dω/dE enberi boylamının çevrim başına değişimi, Pa anomalistik dönem, Ps yıldızıl dönemdir. Dışmerkezlik ve enberi boylamı dikine hız modelinden (2.4.4) ya da literatürden alınacak ve beklenen en büyük değişim genliği (e·Pa/π) gözlenen O−C değişimiyle karşılaştırılacaktır. İkincil tutulma zamanı bulunan sistemlerde iki bağıntının farkından e·cos ω ayrıca hesaplanacaktır; apsis hareketinde ikincil tutulmalar geçişlerle zıt yönde, gelgit bozulmasında ise aynı yönde kayar.

**2.4.3. Işık-Zaman Etkisi (Rømer Etkisi)**

Sistem uzak bir eşlikçi nedeniyle bakış doğrultusunda sabit bir ivmeyle hareket ediyorsa, ışığın bize ulaşma süresi değişir ve dönem değişiyormuş gibi görünür (Bouma vd., 2020):

(dP/dt)_ışık-zaman = P·γ̇ / c

Burada γ̇ dikine hızdaki ivme (2.4.4), c ışık hızıdır. Bu değer O−C'den bulunan dP/dt ile karşılaştırılacaktır. İki değerin farkı, birleşik belirsizliğe (√(σ²_O−C + σ²_ışık-zaman)) oranla 2σ'dan küçükse değişim ışık-zaman etkisiyle açıklanabilir; 3σ'dan büyükse açıklanamaz ve ışık-zaman katkısı çıkarıldıktan sonra kalan değişim diğer mekanizmalarla değerlendirilir; arada kalan durumlar "kısmen açıklanabilir" olarak verilecektir.

**2.4.4. Dikine Hız Verilerinin Modellenmesi**

Işık-zaman etkisi ve apsis hareketi için gereken ivme, dışmerkezlik ve enberi boylamı, yayımlanmış dikine hız ölçümlerinden elde edilecektir. Dikine hız modeli şudur:

v(t) = γ_j + K·[cos(ν + ω) + e·cos ω] + γ̇·(t − t0)

Burada K gezegenin oluşturduğu hız genliği, ν gerçek anomali, γ_j j. tayfçekerin sistemik hızı, γ̇ ivme, t0 referans zamandır. Farklı tayfçekerlerin ölçümleri aynı yıldız için farklı sistemik hız değerleri verdiğinden her tayfçekere ayrı bir γ_j tanımlanacaktır. Gezegen yıldızın önünden geçerken alınan ölçümler (Rossiter-McLaughlin etkisi) çıkarılacak; yıldız etkinliğinden kaynaklanan ek hız gürültüsü (jitter) ölçüm hatalarına eklenecektir. Model en küçük kareler yöntemiyle uyumlanacak, parametrelerin belirsizlikleri emcee ile MCMC örneklemesinden alınacaktır. WASP-4 b için birden fazla tayfçekerle uzun süreye yayılan ölçümler bulunmaktadır (Bouma vd., 2020). WASP-45 b ve WASP-46 b için yayımlanmış ölçümler sayıca az ya da duyarlılığı düşük olabilir; bu durumda ışık-zaman etkisi için sonuç "ayırt edilemedi" olarak gerekçesiyle verilecektir.

**2.4.5. Applegate Mekanizması**

Yıldızın manyetik aktivite döngüsü kütle dağılımını değiştirir ve yörünge döneminde çevrimsel bir değişim yaratır (Applegate, 1992; Watson ve Marsh, 2010):

ΔP/P = −9·(R*/a)²·ΔQ/(M*·R*²) ve A = (P_mod/2π)·(ΔP/P)

Burada ΔQ yıldızın kuadrupol momentindeki değişim, P_mod aktivite döngüsünün süresi, A O−C diyagramındaki değişimin genliğidir. Bu değişimi üretmek için yıldızın sağlaması gereken enerji şu bağıntıyla hesaplanacaktır (Watson ve Marsh, 2010):

ΔE = (1/6)·(M*/Ms)·[G²·M*³·a⁴ / (Ω²·R*⁸)]·(ΔP/P)²

Burada Ms yıldızın dış katmanının kütlesi (Ms = 0,1·M* alınacaktır), Ω yıldızın açısal dönme hızıdır (Ω = 2π/P_dönme). Hesaplanan ΔE, yıldızın bir aktivite döngüsü boyunca yaydığı enerjiyle (L*·P_mod) karşılaştırılacak; ΔE bu enerjiden büyükse mekanizma dışlanacaktır. Yıldızının manyetik etkinliği bilinen WASP-46 sisteminde bu mekanizmaya özellikle bakılacaktır.

**2.4.6. Üçüncü Cisim**

Üçüncü bir cisim, sistemin ortak kütle merkezi etrafında dolanması nedeniyle O−C diyagramında çevrimsel bir değişim oluşturur. Kuadratik modelin artıklarında Lomb-Scargle periyodogramıyla (Lomb, 1976; Scargle, 1982) periyodik sinyal aranacak; yanlış alarm olasılığı 0,01'den küçük olan sinyaller dikkate alınacak, gözlem mevsiminden kaynaklanan yaklaşık bir yıllık sinyaller dışarıda bırakılacaktır. Sinyal bulunursa yarı genliği A ve dönemi P₃ kullanılarak üçüncü cismin kütle fonksiyonu hesaplanacaktır (Irwin, 1952):

f(M₃) = 4π²·(A·c)³ / (G·P₃²) = (M₃·sin i₃)³ / (M* + Mp + M₃)²

Burada M₃ üçüncü cismin kütlesi, i₃ yörüngesinin eğim açısı, G kütle çekim sabitidir.

**2.4.7. Kütle Kaybı**

Gezegen yıldızına Roche sınırı kadar yaklaşırsa kütle kaybedebilir ve bu durum yörüngeyi değiştirebilir. Roche sınırı a_Roche ≈ 2,16·Rp·(M*/Mp)^(1/3) bağıntısıyla (Ford ve Rasio, 2006) hesaplanacaktır; burada Rp gezegenin yarıçapıdır. a/a_Roche oranı 1'e yakın olan sistemlerde kütle kaybının katkısı tartışılacak, bu oranın belirgin biçimde büyük olduğu sistemlerde ihmal edilecektir.

Her mekanizma için sonuç "dışlandı", "olası değil", "olası" ya da "ayırt edilemedi" olarak verilecek ve üç sistemin sonuçları bir tabloda toplanacaktır.

**2.5. Hedeflerin Seçimi (Ön Çalışma)**

Ön çalışma olarak yalnızca hedef seçimi yapılmıştır. Wang vd. (2024)'nin LOOCV testini geçen 14 adayı iki ölçüte göre incelenmiştir. Birinci ölçüt, adayın son yayımlanmış zamanlama çalışmasından sonra TESS tarafından yeniden gözlenmiş ve bu verilerin incelediğimiz yayınlarda kullanılmamış olmasıdır; yeni verinin zaman olarak yayılması için en az iki yeni sektör aranmış, verisi kullanılamadığı bildirilen sektörler dikkate alınmamıştır. Bunun için her adayın TESS sektörleri MAST arşivinde tek tek kontrol edilmiş ve son çalışmalarda kullanılan sektörlerle karşılaştırılmıştır. İkinci ölçüt, literatürde dönem değişiminin varlığı ya da nedeni konusunda birbiriyle çelişen sonuçların bulunmasıdır. İki ölçütü birlikte sağlayan üç aday seçilmiştir (Tablo 1). Yöntemin adımları, çalışma takvimindeki iş paketleriyle aynı sırayla yürütülecektir.

# 3. Proje Yönetimi

## 3.1. Çalışma Takvimi

| Tarih Aralığı | Faaliyetler | Kim(ler) | Başarı Ölçütü ve Katkısı |
|---|---|---|---|
| 1.–2. ay | İP1: Yayımlanmış geçiş zamanlarının ve yer gözlemlerinin derlenmesi; zamanların BJD_TDB sistemine dönüştürülmesi | İdris Avlar (proje yürütücüsü; zaman sistemi dönüşümleri); Bahar Cayib (proje ortağı; zamanların ve kaynaklarının tabloya girilmesi); Hüseyin Er (akademik danışman) | Üç sistem için kaynakları belirtilmiş, tümü BJD_TDB sisteminde bir zaman tablosu; zaman sistemi belirsiz kaynaklar işaretli (%20) |
| 3.–5. ay | İP2: Yeni TESS sektörlerinden (WASP-4 b: 103, 105, 106; WASP-45 b: 96, 106, 107; WASP-46 b: 94, 95, 102–105) orta geçiş zamanlarının ölçülmesi | İdris Avlar (proje yürütücüsü; ışık eğrisi modellemesi ve zaman ölçümü); Bahar Cayib (proje ortağı; ışık eğrilerinin indirilmesi ve geçişlerin gözle kontrolü) | Bu sektörlerdeki tüm tam geçişler için belirsizliğiyle birlikte orta geçiş zamanı (%25) |
| 6.–7. ay | İP3: O−C diyagramlarının oluşturulması; doğrusal ve kuadratik modellerin karşılaştırılması; yeni zamanların eski efemerislerle karşılaştırılması; güncel efemerislerin belirlenmesi | İdris Avlar (proje yürütücüsü; model uyumlama ve istatistiksel karşılaştırma); Bahar Cayib (proje ortağı; O−C diyagramlarının çizilmesi); Hüseyin Er (akademik danışman) | Üç sistem için dP/dt ± σ, ΔBIC, "anlamlı değişim var/yok" kararı ve güncel efemeris (%25) |
| 8.–11. ay | İP4: Dikine hız verilerinin modellenmesi; gelgit bozulması, apsis hareketi, ışık-zaman etkisi, Applegate mekanizması, üçüncü cisim ve kütle kaybının değerlendirilmesi | İdris Avlar (proje yürütücüsü; dikine hız modeli ve mekanizma testleri); Bahar Cayib (proje ortağı; dikine hız ölçümlerinin ve sistem parametrelerinin derlenmesi); Hüseyin Er (akademik danışman) | Dönem değişimi bulunan her sistem için altı mekanizmanın sonucunu gerekçesiyle veren tablo (%30) |

## 3.2. Risk Yönetimi

| En Önemli Riskler | Alınacak Tedbirler (B Planı) |
|---|---|
| Literatürdeki zamanlarda zaman sistemi belirsizliği ya da gerçekçi olmayan küçük ölçüm hataları sahte bir dönem değişimi üretebilir. | Her zamanın sistemi kaynak makaleden kontrol edilecek; belirsiz zamanlarla ve onlar olmadan iki ayrı analiz yapılacak; ölçüm hataları her veri grubu için indirgenmiş χ² ile ölçeklenecektir. |
| Bazı yayınlardaki geçiş zamanları tablo olarak verilmemiş olabilir. | Yer gözlemlerine ait zamanlar ETD ve ExoClock veritabanlarından alınacak; bir TESS sektörünün zamanları hiçbir yayında ya da veritabanında bulunmuyorsa yalnızca o sektör 2.2'deki yöntemle ölçülecektir. |
| Sönük yıldızlarda (WASP-45 ve WASP-46) tek tek geçişlerin orta zaman belirsizliği büyük olabilir. | Tek tek ölçülemeyen geçişler için sektördeki tüm geçişler birlikte uyumlanarak sektör başına bir orta geçiş zamanı elde edilecektir. |
| WASP-45 sistemindeki ek yıldızın (Sodickson ve Grunblatt, 2025) ışığı geçiş derinliğini ve zaman ölçümünü etkileyebilir. | Ek yıldızın katkısı TESS veri işleme hattının sağladığı ışık karışımı düzeltmesiyle ve yayımlanmış parametrelerle kontrol edilecek; geçiş şekli sektörler arasında karşılaştırılacaktır. |
| Proje sürerken yeni TESS verilerini kullanan başka bir çalışma yayımlanabilir. | Yayınlar düzenli olarak izlenecek; yeni çalışmanın sonuçları kendi sonuçlarımızla karşılaştırılacak ve bu karşılaştırma raporda verilecektir. |
| Güncel verilerle bir sistemde anlamlı dönem değişimi bulunmayabilir. | Bu durum araştırma sorusunun bir cevabı olarak raporlanacak ve doğrusal efemeris verilecektir; daha önce bildirilen değişimin neden bulunamadığı tartışılacaktır. |
| WASP-45 b ve WASP-46 b için dikine hız verisi ışık-zaman etkisini sınamaya yetmeyebilir. | Bu sistemlerde ışık-zaman etkisi için sonuç "ayırt edilemedi" olarak verilecek; dikine hız gerektirmeyen testler (Q′*, periyodogram, Roche sınırı) yine uygulanacaktır. |
| İş paketlerinde gecikme yaşanabilir. | İş paketleri ardışık planlanmış ve 12. ay tampon olarak bırakılmıştır; ilerleme danışmanla düzenli görüşmelerle izlenecektir. |
| Yazılım ya da bilgisayar arızası yaşanabilir. | Kod ve veriler düzenli olarak yedeklenecek; analizler ücretsiz çevrim içi Python ortamlarında da çalışabilecek şekilde hazırlanacaktır. |

## 3.3. Araştırma Olanakları

| Kuruluşta Bulunan Altyapı/Ekipman Türü, Modeli | Projede Kullanım Amacı |
|---|---|
| Üniversite kütüphanesindeki bilgisayarlar ve kampüs internet erişimi; proje yürütücüsünün kişisel dizüstü bilgisayarı | Veri indirme, ışık eğrisi analizi, O−C ve dikine hız analizleri |
| Açık erişimli veri arşivleri: MAST (TESS), VizieR, NASA Exoplanet Archive, DACE, ETD/VarAstro, ExoClock | Geçiş zamanları, ışık eğrileri, sistem parametreleri ve dikine hız ölçümleri |
| Açık kaynak yazılımlar: Python, NumPy, Astropy, astroquery, batman, emcee | Tüm analizlerin ücretsiz ve tekrarlanabilir biçimde yapılması |

# 4. Araştırma Önerisinin Yaygın Etkisi

| Çıktı, Etki ve Kazanımlar | Öngörülen Çıktı(lar), Etki(ler) ve Kazanım(lar) |
|---|---|
| Bilimsel/Akademik Çıktılar | Üç sistemin yeni TESS verileriyle güncellenmiş O−C analizini ve dönem değişiminin varlığı ile nedenine ilişkin sonuç tablosunu içeren proje sonuç raporu. Sonuçların, yeterli görülmesi halinde danışmanla birlikte kısa bir makale olarak sunulması hedeflenmektedir. |
| Ekonomik/Ticari/Sosyal Çıktılar | Üç sistemin tüm geçiş zamanlarını (yeni TESS zamanları dahil) BJD_TDB sisteminde içeren açık erişimli veri seti, analiz kodu ve güncel efemerisler. Bu çıktılar gelecekteki geçiş gözlemlerinin planlanmasında kullanılabilecektir. Danışmanın uygun görmesi halinde bölüm öğrencilerine yönelik kısa bir O−C analizi tanıtım sunumu yapılması hedeflenmektedir. |
| Yeni Proje(ler) Oluşturmasına Yönelik Çıktılar | Aynı yöntemin Wang vd. (2024)'nin diğer adaylarına, yeni TESS verileri geldikçe uygulanmasıyla olası bir lisansüstü tez çalışmasına temel oluşturulması. |

# 5. Belirtmek İstediğiniz Diğer Konular

Aşağıdaki tablo, yöntem bölümünde (2.5) anlatılan hedef seçiminin sonucudur.

**Tablo 1.** Hedef seçim tablosu. Satırlar, Wang vd. (2024)'nin dönem değişimi bildirdiği 26 adaydan LOOCV testini geçen 14 adaydır (Wang vd., 2024, Tablo 3). dP/dt değerleri Wang vd. (2024)'ten alınmıştır. "Son zamanlama çalışması" sütunu, incelediğimiz yayınlar arasında aday için en yeni TESS verisini kullanan çalışmayı gösterir. "Kullanılmamış TESS sektörleri" sütunu, MAST arşivindeki sektörlerin bu çalışmalarda kullanılanlarla karşılaştırılmasıyla belirlenmiştir. Seçim ölçütleri: (1) en az iki kullanılmamış ve kullanılabilir TESS sektörü; (2) literatürde dönem değişiminin varlığı ya da nedeni konusunda çelişkili sonuçlar. "–": aday birinci ölçütte elendiği için ikinci ölçüte bakılmadı.

| Aday | Wang vd. dP/dt (ms/yıl) | Son zamanlama çalışması | Kullanılmamış TESS sektörleri | Literatürde çelişki | Sonuç |
|---|---|---|---|---|---|
| CoRoT-2 b | −21,7 ± 3,0 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| HAT-P-37 b | −34,3 ± 6,7 | Wang vd. (2024) | 74, 75, 80, 82 (kullanılabilirliği şüpheli) | – | Elendi: TESS verisi arka plan kirliliği nedeniyle büyük ölçüde kullanılamıyor (Wang vd., 2024) |
| KELT-16 b | −27,8 ± 4,8 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| TrES-1 b | −14,8 ± 2,4 | Kutluay vd. (2026) | 81 | – | Elendi: tek sektör |
| TrES-5 b | −9,7 ± 2,1 | Rothmeier vd. (2025) | Yok | – | Elendi: yeni veri yok |
| WASP-4 b | −6,4 ± 0,6 | Winn ve Stefánsson (2025) | 103, 105, 106 | Var (gelgit / ışık-zaman) | **Seçildi** |
| WASP-10 b | −27,7 ± 3,5 | Wang vd. (2024) | 83 | – | Elendi: tek sektör |
| WASP-12 b | −30,2 ± 0,9 | Kutluay vd. (2026) | Yok | – | Elendi: yeni veri yok |
| WASP-22 b | −71,8 ± 17,1 | Stinga (2026) | Yok | – | Elendi: yeni veri yok |
| WASP-45 b | −169,2 ± 21,1 | Kokori vd. (2026) | 96, 106, 107 | Var (değişimin büyüklüğü) | **Seçildi** |
| XO-4 b | −62,6 ± 17,5 | Wang vd. (2024) | 74 | – | Elendi: tek sektör |
| HAT-P-7 b | +18,3 ± 4,1 | Yang vd. (2025) | Yok | – | Elendi: yeni veri yok |
| WASP-1 b | +22,5 ± 5,2 | Sodickson ve Grunblatt (2025) | En fazla bir (84) | – | Elendi: tek sektör |
| WASP-46 b | +51,7 ± 2,9 | Kutluay vd. (2026) | 94, 95, 102–105 | Var (değişimin varlığı) | **Seçildi** |

# 6. Ekler — EK-1: Kaynaklar

- Adams, E. R. vd. 2024. "Doomed Worlds. I. No New Evidence for Orbital Decay in a Long-term Survey of 43 Ultrahot Jupiters", The Planetary Science Journal, 5 (7), 163. https://doi.org/10.3847/PSJ/ad3e80
- Akeson, R. L. vd. 2013. "The NASA Exoplanet Archive: Data and Tools for Exoplanet Research", Publications of the Astronomical Society of the Pacific, 125 (930), 989-999. https://doi.org/10.1086/672273
- Anderson, D. R. vd. 2012. "WASP-44b, WASP-45b and WASP-46b: Three Short-period, Transiting Extrasolar Planets", Monthly Notices of the Royal Astronomical Society, 422 (3), 1988-1998. https://doi.org/10.1111/j.1365-2966.2012.20635.x
- Applegate, J. H. 1992. "A Mechanism for Orbital Period Modulation in Close Binaries", The Astrophysical Journal, 385, 621. https://doi.org/10.1086/170967
- Astropy Collaboration vd. 2022. "The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package", The Astrophysical Journal, 935 (2), 167. https://doi.org/10.3847/1538-4357/ac7c74
- Baluev, R. V. vd. 2020. "WASP-4 Transit Timing Variation from a Comprehensive Set of 129 Transits", Monthly Notices of the Royal Astronomical Society: Letters, 496 (1), L11-L15. https://doi.org/10.1093/mnrasl/slaa069
- Baştürk, Ö. vd. 2025. "The Orbit of WASP-4 b is in Decay", Monthly Notices of the Royal Astronomical Society, 541 (2), 714-730. https://doi.org/10.1093/mnras/staf1009
- Bouma, L. G. vd. 2020. "WASP-4 Is Accelerating toward the Earth", The Astrophysical Journal Letters, 893 (2), L29. https://doi.org/10.3847/2041-8213/ab8563
- DACE. "Data & Analysis Center for Exoplanets". https://dace.unige.ch, Son erişim tarihi: 8 Kasım 2026.
- Davoudi, F. vd. 2021. "Refined Ephemeris for Four Hot Jupiters Using Ground-Based and TESS Observations", Astronomy Letters, 47 (9), 638-650. https://doi.org/10.1134/S1063773721090024
- Ford, E. B., Rasio, F. A. 2006. "On the Relation between Hot Jupiters and the Roche Limit", The Astrophysical Journal, 638 (1), L45-L48. https://doi.org/10.1086/500734
- Foreman-Mackey, D. vd. 2013. "emcee: The MCMC Hammer", Publications of the Astronomical Society of the Pacific, 125 (925), 306-312. https://doi.org/10.1086/670067
- Harre, J.-V. vd. 2023. "Examining the Orbital Decay Targets KELT-9 b, KELT-16 b, and WASP-4 b, and the Transit-timing Variations of HD 97658 b", Astronomy & Astrophysics, 669, A124. https://doi.org/10.1051/0004-6361/202244529
- Irwin, J. B. 1952. "The Determination of a Light-Time Orbit", The Astrophysical Journal, 116, 211. https://doi.org/10.1086/145604
- Ivshina, E. S., Winn, J. N. 2022. "TESS Transit Timing of Hundreds of Hot Jupiters", The Astrophysical Journal Supplement Series, 259 (2), 62. https://doi.org/10.3847/1538-4365/ac545b
- Kokori, A. vd. 2023. "ExoClock Project. III. 450 New Exoplanet Ephemerides from Ground and Space Observations", The Astrophysical Journal Supplement Series, 265 (1), 4. https://doi.org/10.3847/1538-4365/ac9da4
- Kokori, A. vd. 2026. "ExoClock Project. IV. A Homogeneous Catalog of 620 Updated Exoplanet Ephemerides", The Astrophysical Journal Supplement Series, 283 (1), 5. https://doi.org/10.3847/1538-4365/ae3238
- Kreidberg, L. 2015. "batman: BAsic Transit Model cAlculatioN in Python", Publications of the Astronomical Society of the Pacific, 127 (957), 1161-1165. https://doi.org/10.1086/683602
- Kutluay, A. C. vd. 2026. "Chasing the Tides: Searching for Orbital Decay Signatures in Transit Timing Data and Tidal Models for 20 Hot Jupiters", Publications of the Astronomical Society of the Pacific, 138 (2), 024405. https://doi.org/10.1088/1538-3873/ae406a
- Lomb, N. R. 1976. "Least-squares Frequency Analysis of Unequally Spaced Data", Astrophysics and Space Science, 39 (2), 447-462. https://doi.org/10.1007/BF00648343
- MAST. "Mikulski Archive for Space Telescopes". https://archive.stsci.edu, Son erişim tarihi: 8 Kasım 2026.
- Ochsenbein, F., Bauer, P., Marcout, J. 2000. "The VizieR Database of Astronomical Catalogues", Astronomy and Astrophysics Supplement Series, 143 (1), 23-32. https://doi.org/10.1051/aas:2000169
- Patra, K. C. vd. 2017. "The Apparently Decaying Orbit of WASP-12b", The Astronomical Journal, 154 (1), 4. https://doi.org/10.3847/1538-3881/aa6d75
- Penev, K. vd. 2018. "Empirical Tidal Dissipation in Exoplanet Hosts from Tidal Spin-up", The Astronomical Journal, 155 (4), 165. https://doi.org/10.3847/1538-3881/aaaf71
- Petrucci, R. vd. 2018. "A Search for Transit Timing Variations and Orbital Decay in WASP-46b", Monthly Notices of the Royal Astronomical Society, 473 (4), 5126-5141. https://doi.org/10.1093/mnras/stx2647
- Poddaný, S., Brát, L., Pejcha, O. 2010. "Exoplanet Transit Database. Reduction and Processing of the Photometric Data of Exoplanet Transits", New Astronomy, 15 (3), 297-301. https://doi.org/10.1016/j.newast.2009.09.001
- Ricker, G. R. vd. 2015. "Transiting Exoplanet Survey Satellite", Journal of Astronomical Telescopes, Instruments, and Systems, 1 (1), 014003. https://doi.org/10.1117/1.JATIS.1.1.014003
- Rothmeier, M. vd. 2025. "Doomed Worlds. II. Reassessing Suggestions of Orbital Decay for TrES-5 b", The Planetary Science Journal, 6 (12), 292. https://doi.org/10.3847/PSJ/ae1b9c
- Scargle, J. D. 1982. "Studies in Astronomical Time Series Analysis. II. Statistical Aspects of Spectral Analysis of Unevenly Spaced Data", The Astrophysical Journal, 263, 835. https://doi.org/10.1086/160554
- Schwarz, G. 1978. "Estimating the Dimension of a Model", The Annals of Statistics, 6 (2), 461-464. https://doi.org/10.1214/aos/1176344136
- Sodickson, N., Grunblatt, S. 2025. "In Search of Decay: An Analysis of Transit Times of Hot Jupiters in Main-sequence and Post-main-sequence Systems", The Astrophysical Journal, 993 (1), 78. https://doi.org/10.3847/1538-4357/adfd60
- Stinga, S. I. 2026. "TESS Transit Times from 2026 Do Not Confirm the Reported Orbital Decay of WASP-22 b", Research Notes of the AAS, 10 (10), 297. https://doi.org/10.3847/2515-5172/aeb5e5
- T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. 2023. "On İkinci Kalkınma Planı (2024-2028)". https://www.sbb.gov.tr/wp-content/uploads/2023/12/On-Ikinci-Kalkinma-Plani_2024-2028_11122023.pdf, Son erişim tarihi: 8 Kasım 2026.
- Turner, J. D. vd. 2022. "Characterizing the WASP-4 System with TESS and Radial Velocity Data: Constraints on the Cause of the Hot Jupiter's Changing Orbit and Evidence of an Outer Planet", The Astronomical Journal, 163 (6), 281. https://doi.org/10.3847/1538-3881/ac686f
- Wang, W. vd. 2024. "Long-term Variations in the Orbital Period of Hot Jupiters from Transit-timing Analysis Using TESS Survey Data", The Astrophysical Journal Supplement Series, 270 (1), 14. https://doi.org/10.3847/1538-4365/ad0847
- Watson, C. A., Marsh, T. R. 2010. "Orbital Period Variations of Hot Jupiters Caused by the Applegate Effect", Monthly Notices of the Royal Astronomical Society, 405, 2037. https://doi.org/10.1111/j.1365-2966.2010.16602.x
- Winn, J. N., Stefánsson, G. 2025. "Orbital Decay Candidates Reconsidered: WASP-4 b Is Not Decaying and Kepler-1658 b Is Not a Planet", The Planetary Science Journal, 6 (12), 300. https://doi.org/10.3847/PSJ/ae21db
- Yang, E., Su, Y., Winn, J. N. 2025. "A Third Star in the HAT-P-7 System and a New Dynamical Pathway to Misaligned Hot Jupiters", The Astrophysical Journal, 986 (2), 117. https://doi.org/10.3847/1538-4357/add5f7
- Yee, S. W. vd. 2020. "The Orbit of WASP-12b Is Decaying", The Astrophysical Journal Letters, 888 (1), L5. https://doi.org/10.3847/2041-8213/ab5c16
- Yeh, L.-C., Jiang, I.-G., A-thano, N. 2024. "Searching for Candidates of Orbital Decays among Transit Exoplanets", New Astronomy, 106, 102130. https://doi.org/10.1016/j.newast.2023.102130
