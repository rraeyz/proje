"""TUBITAK_2209A_form_metinleri.md -> kilavuz_ek_form.tex (kılavuzun Ek A'sı).
Kullanim (proje kokunden):  python kod/kilavuz_ek_uret.py
Form metni degisirse bunu calistirip kilavuzu yeniden derle; Ek A her zaman formla ayni olur.
"""
import pathlib, re

KOK = pathlib.Path(__file__).resolve().parent.parent
md = (KOK / "TUBITAK_2209A_form_metinleri.md").read_text()


def kacis(t):
    url = []
    t = re.sub(r"https?://\S+", lambda m: url.append(m.group(0)) or f"@@URL{len(url) - 1}@@", t)
    t = t.replace("\\|", "|").replace("\\", "")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#"), ("$", r"\$"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        t = t.replace(a, b)
    t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
    for i, u in enumerate(url):
        t = t.replace(f"@@URL{i}@@", r"\url{" + u.replace("%", r"\%").replace("#", r"\#") + "}")
    return t


out, tablo, liste = [], [], False
for s in md.splitlines():
    if s.startswith(">") or s.startswith("["):
        continue
    if s.startswith("|"):
        if not re.match(r"^\|[-| ]+\|$", s):
            tablo.append([kacis(c.strip()) for c in s.strip().strip("|").split(" | ")])
        continue
    if tablo:
        n = len(tablo[0])
        out.append(r"{\footnotesize\begin{longtable}{|" + ("p{%.3f\\linewidth}|" % ((0.97 - 0.035 * n) / n)) * n + "}\\hline")
        out.append(" & ".join(r"\textbf{%s}" % c for c in tablo[0]) + r"\\\hline\endhead")
        out += [" & ".join(r) + r"\\\hline" for r in tablo[1:]]
        out.append(r"\end{longtable}}"); tablo = []
    if s.startswith("- "):
        if not liste:
            out.append(r"\begin{itemize}[leftmargin=1em,itemsep=1pt]"); liste = True
        out.append(r"\item " + kacis(s[2:])); continue
    if liste:
        out.append(r"\end{itemize}"); liste = False
    m = re.match(r"^(#{1,2}) (.+)$", s)
    if m:
        out.append((r"\subsection*{%s}" if m.group(1) == "#" else r"\subsubsection*{%s}") % kacis(m.group(2)))
    elif s.strip():
        out.append(kacis(s) + "\n")
if liste:
    out.append(r"\end{itemize}")
(KOK / "kilavuz_ek_form.tex").write_text("\n".join(out) + "\n")
print("kilavuz_ek_form.tex yazildi")
