import json, pathlib
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8"))
print("TB_ENTRIES")
for e in data:
    if "terminal-bench" in e.get("name","").lower():
        print("%s v=%s tasks=%d desc=%s" % (e.get("name"), e.get("version"), len(e.get("tasks", [])), (e.get("description") or "")[:120]))
print("TB2_PATHS")
for e in data:
    if e.get("name") == "terminal-bench" and e.get("version") == "2.0":
        for t in e.get("tasks", [])[:5]:
            print(t.get("name"), "|", t.get("git_url"), "|", t.get("path"))
