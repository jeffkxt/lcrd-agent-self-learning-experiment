import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("TOP_TYPE", type(data).__name__)
if isinstance(data, list):
    print("LIST_LEN", len(data))
    if data:
        print("ITEM0_KEYS", list(data[0].keys()) if isinstance(data[0], dict) else repr(data[0])[:200])
        print("ITEM0", json.dumps(data[0], ensure_ascii=False)[:800])
elif isinstance(data, dict):
    print("TOP_KEYS", list(data.keys())[:30])
