import json, pathlib
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/exp_root.json").read_text(encoding="utf-8"))
for e in data:
    print("%s\t%s\t%s" % (e.get("type"), e.get("name"), e.get("size")))
