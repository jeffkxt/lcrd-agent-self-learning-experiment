import json, pathlib, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
data = json.loads(pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8"))
print("TB21_LOOKUP")
hits = [e for e in data if e.get("version") == "2.1" or "2.1" in str(e.get("version"))]
print("HITS", [(e.get("name"), e.get("version")) for e in hits])
# also check text occurrences of '"version": "2.1"'
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_registry.json").read_text(encoding="utf-8")
print('RAW_2_1_COUNT', raw.count('"version": "2.1"'))
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://api.github.com/repos/laude-institute/terminal-bench-2/contents/", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb2repo_root.json")
grab("https://raw.githubusercontent.com/laude-institute/terminal-bench-2/main/README.md", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb2_README.md")
