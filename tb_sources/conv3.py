import pathlib, re, html as h, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/zai_verified.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/zai_verified.txt")
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_task_format.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_task_format.txt")
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://raw.githubusercontent.com/harbor-framework/terminal-bench-2-1/main/tasks/dataset.toml", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb21_dataset_toml")
grab("https://raw.githubusercontent.com/harbor-framework/terminal-bench-2-1/main/tasks/README.md", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb21_tasks_README.md")
