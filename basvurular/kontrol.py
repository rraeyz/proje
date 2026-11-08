"""Başvuru metni kontrolü. Kullanım: python kontrol.py A_form.md"""
import re, sys

md = open(sys.argv[1], encoding="utf-8").read()
govde, kay = md.split("# 6. Ekler")
sorun = []

def bolum(bas, son):
    return govde.split(bas)[1].split(son)[0]

ozet = bolum("# Özet", "**Anahtar")
n = len(ozet.split())
print("Özet kelime:", n); sorun += [] if 25 <= n <= 450 else ["özet kelime sınırı"]
for ad, a, b in [("1.1", "## 1.1.", "## 1.2."), ("1.2", "## 1.2.", "# 2. Yöntem"), ("2", "# 2. Yöntem", "# 3. Proje")]:
    k = len(bolum(a, b)); print(f"{ad} karakter: {k}")
    if k < 350: sorun.append(ad + " < 350 karakter")

y = bolum("# 2. Yöntem", "# 3. Proje")
if re.search(r"İP\d", y): sorun.append("Yöntem'de İP var")

refs = [l[2:] for l in kay.splitlines() if l.startswith("- ")]
print("Kaynak sayısı:", len(refs))
def anahtar(r):
    for k, v in [("T.C. Cumhur", "T.C. Cumhurbaşkanlığı"), ("T.C. Sanayi", "T.C. Sanayi ve Teknoloji Bakanlığı"),
                 ("Astropy", "Astropy Collaboration"), ("DACE", "DACE"), ("MAST", "MAST")]:
        if r.startswith(k): return v, None
    yil = re.search(r"\b(1[89]\d\d|20\d\d)\b", r).group(1)
    return r.split(",")[0].strip(), yil
for r in refs:
    soy, yil = anahtar(r)
    if yil is None:
        ok = soy in govde
    else:
        ok = re.search(re.escape(soy) + r"[^()\n]{0,60}?" + yil, govde) or re.search(re.escape(soy) + r"[^\n]{0,60}?\(" + yil, govde)
    if not ok: sorun.append(f"atıf yok/yıl uymuyor: {soy} {yil}")
    if "doi.org" not in r and yil is not None: sorun.append("DOI yok: " + soy)
sira = [r.lower().replace("ş", "s").replace("ö", "o").replace("ü", "u").replace("ç", "c").replace("ı", "i") for r in refs]
if sira != sorted(sira): sorun.append("kaynaklar alfabetik değil")

# metindeki atıfların kaynakçada olması
for m in re.finditer(r"([A-ZÇŞÖÜİ][a-zçğışöüá\-]+)(?: ve [A-ZÇŞÖÜİ][a-zçğışöüá\-]+| vd\.)?(?:'[a-zığüşöç]+)?,? \(?((?:19|20)\d\d)\)?", govde):
    soy, yil = m.group(1), m.group(2)
    if soy in ("Tablo", "Ay", "Plan", "Kalkınma", "Strateji", "Stratejisi", "Sanayi", "Bakanlığı", "Başkanlığı", "Collaboration", "Mackey", "Planı"): continue
    if not any(r.startswith(soy) and yil in r for r in refs):
        sorun.append(f"kaynakçada yok?: {soy} {yil}")

yasak = ["vaka", "hüküm", "karar ağacı", "görgül", "birini dışarıda bırak", "kalite bayrak", "taban çizgisi",
         "yinelemeli kırp", "hata çubu", "sıfır noktası", "yıldız kaynaklı saçılma", "ışık-yolu", "ışık yolu",
         "UAK", "kongre", "bildiri ", "GitHub", "Google", "Zenodo", "Research Notes", "epok numarası",
         "kesirli kısmı", "sarmallan", "kabarıklı", "örtülme", "dört kutup", "Bayes Bilgi Ölçütü", "yapay zek"]
for k in yasak:
    if k.lower() in govde.lower(): sorun.append("yasak/işaretli terim: " + k)

t = re.findall(r"\(%(\d+)\)", md); print("Takvim toplamı:", sum(map(int, t)))
if sum(map(int, t)) != 100: sorun.append("takvim toplamı 100 değil")
print("'ön çalışma' geçiş sayısı:", len(re.findall(r"[Öö]n çalışma", md)))
print("SORUNLAR:" if sorun else "Sorun bulunmadı.")
for s in dict.fromkeys(sorun): print("  -", s)
