"""Word dosyasındaki metni form .md ile karşılaştırır. Kullanım: python word_karsilastir.py A"""
import re, sys, zipfile, html
X = sys.argv[1]
x = zipfile.ZipFile(f"{X}_Basvuru_Formu.docx").read("word/document.xml").decode()
D = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", x))))
md = open(f"{X}_form.md", encoding="utf-8").read()
eksik, say = [], 0
for s in md.splitlines():
    if not s.strip() or s.startswith((">", "[", "#", "|---")): continue
    for c in ([c.strip().replace("\\|", "|") for c in s.strip("|").split(" | ")] if s.startswith("|") else [s.lstrip("- ")]):
        c = re.sub(r"\s+", " ", c.replace("**", "")).strip()
        if not c or c in ("Alan", "Değer", "Başarı Ölçütü ve Katkısı"): continue
        say += 1
        if c not in D: eksik.append(c[:70])
print(f"{X}: {say} parça kontrol edildi, Word'de bulunmayan: {eksik if eksik else 'yok'}")
