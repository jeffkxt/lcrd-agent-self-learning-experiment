import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/exp_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("COUNT", len(data))
print("KEYS", list(data[0].keys()) if data else None)
import pprint
for item in data[:3]:
    print("ITEM", json.dumps(item, ensure_ascii=False)[:600])
