import re, pathlib
text = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/arxiv_2601.11868.txt").read_text(encoding="utf-8")
start = text.index("Appendix H")
end = text.index("Appendix I")
region = text[start:end]
paras = [p.strip() for p in region.split("\n\n") if p.strip()]
diffset = {"Easy","Medium","Hard"}
diff_idx = [k for k,p in enumerate(paras) if p in diffset]
print("DIFF_COUNT=", len(diff_idx))
idlike = [k for k,p in enumerate(paras) if re.fullmatch(r"[a-z][a-z0-9-]{1,60}", p)]
print("TASKID_COUNT=", len(idlike))
for k in idlike:
    print("IDCAND", k, repr(paras[k][:40]))
# for each diff marker, print the three preceding paragraphs short
for k in diff_idx[:]:
    prev = paras[max(0,k-3):k]
    print("ENTRY", " | ".join((p[:30].replace("\n"," ") for p in prev)), " => ", paras[k])
