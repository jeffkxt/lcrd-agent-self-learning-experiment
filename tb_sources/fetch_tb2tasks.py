import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base = "https://raw.githubusercontent.com/laude-institute/terminal-bench-2/main/%s"
tasks = ["adaptive-rejection-sampler","feal-differential-cryptanalysis","video-processing","mailman","cobol-modernization"]
for t in tasks:
    for f in ["task.toml", "instruction.md"]:
        url = base % (t + "/" + f)
        out = r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb2_%s_%s" % (t, f.replace(".", "_"))
        try:
            r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
            pathlib.Path(out).write_bytes(r.content)
            print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
        except Exception as e:
            print("ERR %s %r" % (url, e))
