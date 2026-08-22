import json, pathlib
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8")
data = json.loads(raw)
print("TOP_TYPE", type(data).__name__)
if isinstance(data, dict):
    print("TOP_KEYS", list(data.keys())[:20])
    print("TERMINAL_BENCH_ENTRIES")
    for k, v in data.items():
        if "terminal-bench" in str(k).lower() or "tbench" in str(k).lower():
            print("KEY", k, "VALTYPE", type(v).__name__)
            print(json.dumps(v, ensure_ascii=False)[:1500])
