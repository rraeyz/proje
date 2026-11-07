"""TÜBİTAK 2209-A Word şablonunu TUBITAK_2209A_form_metinleri.md içeriğiyle doldurur."""
import re, copy, shutil, struct, sys
from lxml import etree

ACIK, MD, SEK = sys.argv[1], sys.argv[2], sys.argv[3]
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W}
q = lambda t: '{%s}%s' % (W, t)

# ---------- Markdown'u bölümlere ayır ----------
md = open(MD).read()
bolum, ad = {}, None
for satir in md.splitlines():
    m = re.match(r'^#{1,2} (.+)$', satir)
    if m:
        ad = m.group(1).strip(); bolum[ad] = []
    elif ad:
        bolum[ad].append(satir)

def paragraflar(ad):
    """Tablo ve boş satır dışındaki paragraflar."""
    out, cur = [], []
    for s in bolum[ad]:
        if s.startswith('|') or s.startswith('>') or not s.strip():
            if cur: out.append(' '.join(cur)); cur = []
            continue
        cur.append(s.strip().rstrip('\\').strip())
    if cur: out.append(' '.join(cur))
    out = [re.sub(r'\\([^\w\s])', r'\1', p) for p in out]   # Markdown kaçışlarını kaldır
    return [p for p in out if not p.startswith('[')]

def tablolar(ad):
    """Bölümdeki Markdown tablolarını satır listesi olarak döndürür."""
    tabs, cur = [], []
    for s in bolum[ad] + ['']:
        if s.startswith('|'):
            hucre = [re.sub(r'\\([^\w\s])', r'\1', h.strip()) for h in re.split(r'(?<!\\)\|', s)[1:-1]]
            if not all(re.fullmatch(r':?-+:?', h) for h in hucre):
                cur.append(hucre)
        elif cur:
            tabs.append(cur); cur = []
    return tabs

# ---------- XML yardımcıları ----------
def rpr(kalin=False, boy=18):
    r = etree.Element(q('rPr'))
    f = etree.SubElement(r, q('rFonts')); [f.set(q(k), 'Arial') for k in ('ascii', 'hAnsi', 'cs')]
    if kalin: etree.SubElement(r, q('b')); etree.SubElement(r, q('bCs'))
    etree.SubElement(r, q('color')).set(q('val'), '000000')
    etree.SubElement(r, q('sz')).set(q('val'), str(boy)); etree.SubElement(r, q('szCs')).set(q('val'), str(boy))
    return r

def run(metin, kalin=False, boy=18):
    r = etree.Element(q('r')); r.append(rpr(kalin, boy))
    t = etree.SubElement(r, q('t')); t.text = metin
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r

def para(metin='', kalin=False, hiza='both', boy=18, once=0, sonra=60):
    p = etree.Element(q('p')); pp = etree.SubElement(p, q('pPr'))
    sp = etree.SubElement(pp, q('spacing')); sp.set(q('before'), str(once)); sp.set(q('after'), str(sonra))
    etree.SubElement(pp, q('jc')).set(q('val'), hiza)
    pp.append(rpr(kalin, boy))
    for i, parca in enumerate(re.split(r'\*\*', metin)):   # **kalın** bölümler
        if parca: p.append(run(parca, kalin or i % 2 == 1, boy))
    return p

def hucre_doldur(tc, metinler, **kw):
    for p in tc.findall(q('p')): tc.remove(p)
    for m in metinler: tc.append(para(m, **kw))

def satir_doldur(tr, degerler, **kw):
    for tc, d in zip(tr.findall(q('tc')), degerler):
        hucre_doldur(tc, [d], **kw)

def tablo_satirlari(tbl, veri, **kw):
    """Şablon tablosunun ilk veri satırını örnek alıp veri kadar satır üretir."""
    satirlar = tbl.findall(q('tr'))
    ornek = satirlar[1]
    for tr in satirlar[1:]: tbl.remove(tr)
    for d in veri:
        tr = copy.deepcopy(ornek); satir_doldur(tr, d, **kw); tbl.append(tr)

def yeni_tablo(veri, genislikler):
    """Kenarlıklı basit tablo (Bölüm 5 içindeki Tablo 1 ve 2)."""
    tbl = etree.Element(q('tbl')); tp = etree.SubElement(tbl, q('tblPr'))
    w = etree.SubElement(tp, q('tblW')); w.set(q('w'), str(sum(genislikler))); w.set(q('type'), 'dxa')
    kb = etree.SubElement(tp, q('tblBorders'))
    for k in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = etree.SubElement(kb, q(k)); e.set(q('val'), 'single'); e.set(q('sz'), '4'); e.set(q('space'), '0'); e.set(q('color'), '000000')
    g = etree.SubElement(tbl, q('tblGrid'))
    for gw in genislikler: etree.SubElement(g, q('gridCol')).set(q('w'), str(gw))
    for i, satir in enumerate(veri):
        tr = etree.SubElement(tbl, q('tr'))
        for gw, d in zip(genislikler, satir):
            tc = etree.SubElement(tr, q('tc')); tcp = etree.SubElement(tc, q('tcPr'))
            x = etree.SubElement(tcp, q('tcW')); x.set(q('w'), str(gw)); x.set(q('type'), 'dxa')
            if i == 0:
                s = etree.SubElement(tcp, q('shd')); s.set(q('val'), 'clear'); s.set(q('color'), 'auto'); s.set(q('fill'), 'D9D9D9')
            pp = para(d, kalin=(i == 0), hiza='left', boy=16, sonra=0)
            sp = pp.find(q('pPr')).find(q('spacing')); sp.set(q('line'), '240'); sp.set(q('lineRule'), 'auto')   # tek satır aralığı
            tc.append(pp)
    return tbl

# ---------- resim ekleme ----------
resim_no = [100]
def resim(dosya, gen_cm):
    w, h = struct.unpack('>II', open(dosya, 'rb').read()[16:24])
    cx = int(gen_cm * 360000); cy = int(cx * h / w)
    resim_no[0] += 1; rid = 'rIdSekil%d' % resim_no[0]; ad = 'sekil%d.png' % resim_no[0]
    shutil.copy(dosya, f'{ACIK}/word/media/{ad}')
    rels = f'{ACIK}/word/_rels/document.xml.rels'
    s = open(rels).read().replace('</Relationships>',
        f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{ad}"/></Relationships>')
    open(rels, 'w').write(s)
    xml = f'''<w:p xmlns:w="{W}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:pPr><w:spacing w:before="120" w:after="60"/><w:jc w:val="center"/></w:pPr>
<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{resim_no[0]}" name="{ad}"/>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="{resim_no[0]}" name="{ad}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''
    return etree.fromstring(xml)

# ---------- doldurma ----------
doc = etree.parse(f'{ACIK}/word/document.xml'); body = doc.getroot().find(q('body'))
ogeler = list(body)
metin = lambda e: ''.join(e.itertext()).strip()
def bul(tur, basla, sonra_index=0):
    for i, e in enumerate(ogeler):
        if i >= sonra_index and etree.QName(e).localname == tur and metin(e).startswith(basla): return i, e
    raise KeyError(basla)

# Yıl
i, p = bul('p', '.....Yılı')
for t in p.iter(q('t')):
    if '.....' in (t.text or ''): t.text = t.text.replace('.....', '2026 ')

# A. Genel bilgiler
genel = {r[0]: r[1] for r in tablolar('A. Genel Bilgiler')[0]}
i, tbl = bul('tbl', 'Başvuru Sahibinin')
for tr, anahtar in zip(tbl.findall(q('tr')), ['Başvuru Sahibinin Adı Soyadı', 'Araştırma Önerisinin Başlığı',
                                            'Danışmanın Adı Soyadı', 'Araştırmanın Yürütüleceği Kurum']):
    deger = re.sub(r'\\([\[\]])', r'\1', genel.get(anahtar, '')) or '[Danışmanın unvanı, adı ve soyadı]'
    p = tr.find(q('tc')).find(q('p')); p.append(run(' ' + deger))

# Özet
ozet = paragraflar('Özet')
i, tbl = bul('tbl', 'Özet')
tr0, tr1 = tbl.findall(q('tr'))
tc = tr0.find(q('tc')); ps = tc.findall(q('p'))
for p in ps[1:]: tc.remove(p)
tc.append(para(ozet[0]))
anahtar = [x for x in ozet if x.startswith('**Anahtar')][0]
hucre_doldur(tr1.find(q('tc')), [anahtar])

# Metin kutuları
for baslik, kutu_sonrasi in [('1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği', '1.1. Konunun'),
                             ('1.2. Amaç ve Hedefler', 'Amaç ve Hedefler'), ('2. Yöntem', 'YÖNTEM')]:
    j, _ = bul('p', kutu_sonrasi)
    k, tbl = bul('tbl', 'En az 350', j)
    hucre_doldur(tbl.find(q('tr')).find(q('tc')), paragraflar(baslik))

# Çalışma takvimi, risk, olanaklar
i, tbl = bul('tbl', 'Tarih Aralığı'); tablo_satirlari(tbl, tablolar('3.1. Çalışma Takvimi')[0][1:], hiza='left')
i, tbl = bul('tbl', 'En Önemli Riskler'); tablo_satirlari(tbl, tablolar('3.2. Risk Yönetimi')[0][1:], hiza='left')
i, tbl = bul('tbl', 'Kuruluşta Bulunan'); tablo_satirlari(tbl, tablolar('3.3. Araştırma Olanakları')[0][1:], hiza='left')

# Yaygın etki: ikinci sütun
i, tbl = bul('tbl', 'Çıktı, Etki')
for tr, (_, d) in zip(tbl.findall(q('tr'))[1:], tablolar('4. Araştırma Önerisinin Yaygın Etkisi')[0][1:]):
    hucre_doldur(tr.findall(q('tc'))[1], [d], hiza='left')

# 5. Diğer konular: metin + şekiller + tablolar
ad5 = '5. Belirtmek İstediğiniz Diğer Konular'
p5 = paragraflar(ad5); t5 = tablolar(ad5)
i, _ = bul('p', '5. BELİRTMEK')
k, tbl = bul('tbl', '', i)
tc = tbl.find(q('tr')).find(q('tc'))
for p in tc.findall(q('p')): tc.remove(p)
giris = [x for x in p5 if not x.startswith('**')]
tab1 = [x for x in p5 if x.startswith('**Tablo 1.')][0]
for g in giris: tc.append(para(g))
tc.append(para(tab1, boy=16, once=120)); tc.append(yeni_tablo(t5[0], [1250, 950, 1000, 1100, 900, 3500]))
tc.append(para(''))   # hücre bir paragrafla bitmeli

# EK-1 Kaynaklar
i, ek = bul('p', 'EK-1')
kaynaklar = [x[2:].strip() for x in bolum['6. Ekler — EK-1: Kaynaklar'] if x.startswith('- ')]
hedef = ek
for kay in kaynaklar:
    yeni = para(kay.lstrip('- ').strip(), hiza='left', sonra=40); hedef.addnext(yeni); hedef = yeni

doc.write(f'{ACIK}/word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
ct = f'{ACIK}/[Content_Types].xml'; s = open(ct).read()
if 'Extension="png"' not in s:
    s = s.replace('<Default Extension="rels"', '<Default Extension="png" ContentType="image/png"/><Default Extension="rels"')
    open(ct, 'w').write(s)
print("doldurma bitti")
