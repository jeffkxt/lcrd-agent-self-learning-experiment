import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/deepwiki_12.html")
grab("https://terminal-bench.com/", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbcom_index.html")
grab("https://www.tbench.ai/docs/introduction", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_docs_intro.html")
grab("https://www.tbench.ai/docs/tasks", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_docs_tasks.html")
grab("https://www.tbench.ai/docs/evaluation", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbench_docs_eval.html")
