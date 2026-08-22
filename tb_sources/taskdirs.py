import requests, pathlib, urllib3, re, html as h
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def lst(url):
    r = requests.get(url, timeout=60, verify=False, headers={"User-Agent":"Mozilla/5.0"})
    import json
    try:
        d = json.loads(r.content)
        return [(e.get("type"), e.get("name"), e.get("size")) for e in d]
    except:
        return ("RAW", r.status_code, r.text[:150])
print("TASK_DIRS")
for t in ["adaptive-rejection-sampler", "feal-differential-cryptanalysis", "video-processing"]:
    print(t, lst("https://api.github.com/repos/laude-institute/terminal-bench-2/contents/%s" % t))
raw = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_run21.html").read_text(encoding="utf-8", errors="replace")
raw = re.sub(r"(?s)<script.*?</script>", " ", raw)
raw = re.sub(r"(?s)<style.*?</style>", " ", raw)
text = re.sub(r"<[^>]+>", "\n", raw)
text = h.unescape(text)
text = re.sub(r"[ \t\u00a0]+", " ", text)
text = re.sub(r"\n\s*\n+", "\n\n", text)
out = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_run21.txt")
out.write_text(text, encoding="utf-8")
print("TXT_OK bytes=%d saved=%s" % (len(text), out))
