#!/bin/bash
# Kullanım: bash word_uret.sh A   → A_form.md'den A_Basvuru_Formu.docx üretir
set -e
X=$1; W=/tmp/claude-0/-home-user/a8e4d0c8-222a-5a23-987f-21b6319b1c4a/scratchpad/word; S=/mnt/skills/public/docx/scripts
cd $W && rm -rf acik_$X && mkdir acik_$X && (cd acik_$X && unzip -q ../orijinal.docx)
python3 $S/merge_runs.py acik_$X >/dev/null
python3 doldur.py acik_$X /home/user/proje/basvurular/${X}_form.md /home/user/proje/sekiller
rm -f ${X}.docx && (cd acik_$X && zip -qr -X -D ../${X}.docx '[Content_Types].xml' _rels docProps word customXml)
python3 $S/office/validate.py ${X}.docx --original orijinal.docx 2>&1 | tail -1
soffice --headless --convert-to pdf ${X}.docx >/dev/null 2>&1
echo "sayfa: $(pdfinfo ${X}.pdf | grep Pages | awk '{print $2}')"
cp ${X}.docx /home/user/proje/basvurular/${X}_Basvuru_Formu.docx
