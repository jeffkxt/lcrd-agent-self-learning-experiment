import re, pathlib
text = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/arxiv_2601.11868.txt").read_text(encoding="utf-8")
lines = text.splitlines()
region = "\n".join(lines[8745:9614])
paras = [p.strip() for p in region.split("\n\n") if p.strip()]
ids, cats, diffs = [], [], []
diffset = {"Easy","Medium","Hard"}
for k, p in enumerate(paras):
    if p in diffset and k >= 3:
        tid = paras[k-3]; cat = paras[k-2]
        if re.fullmatch(r"[a-z][a-z0-9-]{1,60}", tid) and cat not in diffset:
            ids.append(tid); cats.append(cat); diffs.append(p)
print("COUNT= %d" % len(ids))
from collections import Counter
print("BY_CATEGORY= %s" % dict(sorted(Counter(cats).items())))
print("BY_DIFFICULTY= %s" % dict(Counter(diffs)))
out = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/appendixH_parsed.txt")
with out.open("w", encoding="utf-8") as f:
    for tid, cat, d in zip(ids, cats, diffs):
        f.write("%s\t%s\t%s\n" % (tid, cat, d))
print("SAVED= OK")
