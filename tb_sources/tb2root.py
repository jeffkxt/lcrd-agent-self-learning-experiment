import json, pathlib
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb2repo_root.json").read_text(encoding="utf-8"))
print("ROOT_CT", len(data))
dirs = [e.get("name") for e in data if e.get("type")=="dir"]
files = [(e.get("name"), e.get("size")) for e in data if e.get("type")=="file"]
print("DIRS", len(dirs), dirs)
print("FILES", files)
