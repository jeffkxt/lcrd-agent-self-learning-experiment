import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
grab("https://raw.githubusercontent.com/laude-institute/terminal-bench-experiments/main/registry.json", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/exp_registry.json")
grab("https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/registry.json", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb1_registry.json")
grab("https://api.github.com/repos/harbor-framework/terminal-bench-1/contents/original-tasks", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tb1_tasks_list.json")
