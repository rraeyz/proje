"""Kaynakçadaki her DOI'yi Crossref (arXiv için DataCite) ile karşılaştırır. Kullanım: python doi_kontrol.py A_form.md"""
import json, re, sys, time, urllib.request, unicodedata
md = open(sys.argv[1], encoding="utf-8").read().split("# 6. Ekler")[1]
def sade(t): return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", t.lower()).encode("ascii", "ignore").decode())
sorun = 0
for r in [l[2:] for l in md.splitlines() if l.startswith("- ")]:
    m = re.search(r"doi\.org/(\S+)", r)
    if not m: continue
    doi = m.group(1)
    d = None
    for k in range(5):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/" + doi, headers={"User-Agent": "kaynak-kontrol/1.0"}), timeout=40))["message"]; break
        except Exception: time.sleep(3 * (k + 1))
    if not d: print("ULAŞILAMADI:", doi); sorun += 1; continue
    soy = sade((d.get("author") or [{"family": ""}])[0].get("family", ""))
    yil = str((d.get("published-print") or d.get("published-online") or d.get("issued"))["date-parts"][0][0])
    yil2 = str(d["issued"]["date-parts"][0][0])
    cilt = str(d.get("volume") or ""); sayfa = str(d.get("page") or d.get("article-number") or "").split("-")[0]
    baslik = sade(d.get("title", [""])[0])[:25]
    kontroller = {"yazar": soy and soy[:5] in sade(r.split(".")[0] + r[:40]), "yıl": (yil in r or yil2 in r),
                  "cilt": (not cilt) or f", {cilt}," in r, "sayfa": (not sayfa) or sayfa in r, "başlık": baslik[:20] in sade(r)}
    kotu = [k for k, v in kontroller.items() if not v]
    print(("TAMAM " if not kotu else "KONTROL ET " + str(kotu) + " ") + doi + (f"  | CR: {soy} {yil} {cilt} {sayfa}" if kotu else ""))
    sorun += bool(kotu); time.sleep(0.7)
print("Toplam şüpheli:", sorun)
