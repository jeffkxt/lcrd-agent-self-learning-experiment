import re, pathlib
text = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/arxiv_2601.11868.txt").read_text(encoding="utf-8")
lines = text.splitlines()
region = "\n".join(lines[8745:9614])
paras = [p.strip() for p in region.split("\n\n") if p.strip()]
diffset = {"Easy","Medium","Hard"}
def short(p, n=34):
    s = " ".join(p.split())
    return s[:n]
idx = 0
for k, p in enumerate(paras):
    if p in diffset and k >= 3:
        idx += 1
        tid = paras[k-3]; cat = paras[k-2]; desc = paras[k-1]
        ok = bool(re.fullmatch(r"[a-z][a-z0-9-]{1,60}", tid)) and cat not in diffset
        print("D%d ok=%s tid=%r cat=%r desc=%r" % (idx, ok, short(tid), short(cat), short(desc)))
