import json, pathlib, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb1_tasks_list.json").read_text(encoding="utf-8"))
print("ORIG_COUNT", len(data))
names = [e.get("name") for e in data]
print("ORIG_NAMES", ", ".join(names[:60]))
types = {}
for e in data: types[e.get("type")] = types.get(e.get("type"), 0) + 1
print("ORIG_TYPES", types)
r = requests.get("https://api.github.com/repos/laude-institute/terminal-bench-experiments/contents/configs", timeout=60, verify=False, headers={"User-Agent":"Mozilla/5.0"})
pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/exp_configs.json").write_bytes(r.content)
cfg = json.loads(r.content)
print("CONFIGS", [(e.get("type"), e.get("name"), e.get("size")) for e in cfg])
