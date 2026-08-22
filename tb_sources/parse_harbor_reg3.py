import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("LIST_LEN", len(data) if isinstance(data, list) else "notlist")
print("ITEM0_KEYS", list(data[0].keys()) if isinstance(data, list) and data and isinstance(data[0], dict) else "?")
if isinstance(data, list) and data:
    print("ITEM0", json.dumps(data[0], ensure_ascii=False)[:2500])
print("TB_COUNT", raw.count("terminal-bench"))
idx = raw.find("terminal-bench")
print("TB_CTX", raw[max(0,idx-200):idx+300])
