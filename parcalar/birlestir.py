"""p1..p5 parcalarini tek kilavuz.tex dosyasinda birlestirir; %%KOD:dosya%% yerine kodu gomer."""
import re, pathlib
kok = pathlib.Path(__file__).resolve().parent.parent
parca = lambda ad: (kok / "parcalar" / ad).read_text()
p1 = parca("p1.tex"); i = p1.index("% ===================================================== BÖLÜM 0")
metin = p1[:i] + parca("pT.tex") + p1[i:] + "".join(parca(f"p{k}.tex") for k in range(2, 6))
metin = metin.replace(r"\pgfplotsset{compat=1.17}", "\\pgfplotsset{compat=1.17}\n\\usepgfplotslibrary{groupplots}")
metin = metin.replace("Kutluay, vd. 2026", "Kutluay, A. C., vd. 2026")
def kod(m):
    return "\\begin{lstlisting}\n" + (kok / "kod" / m.group(1)).read_text().rstrip() + "\n\\end{lstlisting}"
metin = re.sub(r"%%KOD:([\w.]+)%%", kod, metin)
(kok / "kilavuz.tex").write_text(metin)
print("kilavuz.tex:", len(metin.splitlines()), "satir")
