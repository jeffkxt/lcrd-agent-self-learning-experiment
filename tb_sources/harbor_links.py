import json, pathlib, re
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_root.json").read_text(encoding="utf-8"))
print("HARBOR_ENTRIES")
for e in data:
    print("%s\t%s\t%s" % (e.get("type"), e.get("name"), e.get("size")))
html = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_docs_index.html").read_text(encoding="utf-8", errors="replace")
links = sorted(set(re.findall(r'href="([^"]+)"', html)))
print("DOC_LINKS")
for l in links:
    if "docs" in l or "html" in l or l.startswith("/"):
        print(l)
