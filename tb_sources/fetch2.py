import sys, requests, pathlib
def grab(url, out):
    try:
        r = requests.get(url, timeout=60, allow_redirects=True, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d saved=%s" % (r.status_code, len(r.content), out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://raw.githubusercontent.com/taveren-ai/tbench/main/README.md", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/github_README.md")
grab("https://api.github.com/repos/taveren-ai/tbench/contents/", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/github_root.json")
