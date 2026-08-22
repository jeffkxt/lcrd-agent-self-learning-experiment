import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb1_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("TYPE", type(data).__name__)
if isinstance(data, list):
    print("COUNT", len(data))
    print("KEYS", list(data[0].keys()) if data else None)
    for item in data[:2]:
        print("ITEM", json.dumps(item, ensure_ascii=False)[:1200])
elif isinstance(data, dict):
    print("TOPKEYS", list(data.keys()))
    for k, v in data.items():
        if isinstance(v, list):
            print("LIST %s len=%d" % (k, len(v)))
            if v: print("ITEM0", json.dumps(v[0], ensure_ascii=False)[:1200])
