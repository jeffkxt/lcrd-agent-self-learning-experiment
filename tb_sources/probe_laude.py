import requests, pathlib, urllib3, json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d saved=%s" % (r.status_code, len(r.content), out))
        return r
    except Exception as e:
        print("ERR %s %r" % (url, e))
r = grab("https://api.github.com/repos/laude-institute/terminal-bench/contents/", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/laude_root.json")
