import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/exp_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("TYPE=", type(data).__name__)
if isinstance(data, dict):
    print("TOPKEYS=", list(data.keys())[:30])
    for k, v in data.items():
        if isinstance(v, list):
            print("LISTKEY=%s len=%d" % (k, len(v)))
            if v:
                print("ITEM0TYPE=", type(v[0]).__name__)
                print("ITEM0KEYS=", list(v[0].keys()) if isinstance(v[0], dict) else repr(v[0])[:200])
