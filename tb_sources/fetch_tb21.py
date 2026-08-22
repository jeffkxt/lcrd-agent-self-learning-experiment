import requests, pathlib, urllib3, re, html as h
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://api.github.com/repos/harbor-framework/terminal-bench-2-1/contents/", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb21repo_root.json")
grab("https://raw.githubusercontent.com/harbor-framework/terminal-bench-2-1/main/README.md", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb21_README.md")
def totext(src, dst):
    raw = pathlib.Path(src).read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"(?s)<script.*?</script>", " ", raw)
    raw = re.sub(r"(?s)<style.*?</style>", " ", raw)
    text = re.sub(r"<[^>]+>", "\n", raw)
    text = h.unescape(text)
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    pathlib.Path(dst).write_text(text, encoding="utf-8")
    print("TXT_OK bytes=%d src=%s dst=%s" % (len(text), src, dst))
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_benchmarks2.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_benchmarks2.txt")
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_lb21.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_lb21.txt")
