import re, pathlib
text = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/arxiv_2601.11868.txt").read_text(encoding="utf-8")
lines = text.splitlines()
region = "\n".join(lines[8745:9614])
paras = [p.strip() for p in region.split("\n\n") if p.strip()]
diffset = {"Easy","Medium","Hard"}
idre = re.compile(r"^[a-z][a-z0-9.\-]{1,60}$")
ids, cats, diffs = [], [], []
for k, p in enumerate(paras):
    if p in diffset:
        j = k - 1
        while j >= 0 and not idre.fullmatch(paras[j]):
            j -= 1
        if j >= 0 and j + 1 < k and paras[j+1] not in diffset:
            ids.append(paras[j]); cats.append(paras[j+1]); diffs.append(p)
print("COUNT= %d" % len(ids))
from collections import Counter
print("BY_CATEGORY= %s" % dict(sorted(Counter(cats).items(), key=lambda x: -x[1])))
print("BY_DIFFICULTY= %s" % dict(Counter(diffs)))
out = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/appendixH_parsed.txt")
with out.open("w", encoding="utf-8") as f:
    for tid, cat, d in zip(ids, cats, diffs):
        f.write("%s\t%s\t%s\n" % (tid, cat, d))
print("SAVED= OK")
