import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out, timeout=300):
    try:
        r = requests.get(url, timeout=timeout, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
base = r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/"
grab("https://raw.githubusercontent.com/harbor-framework/harbor/main/registry.json", base + "harbor_registry.json", 600)
grab("https://tbench.ai/docs/run-terminal-bench-2-1", base + "tbench_run21.html")
grab("https://tbench.ai/benchmarks/terminal-bench-2", base + "tbench_benchmarks2.html")
grab("https://tbench.ai/leaderboard/terminal-bench/2.1", base + "tbench_lb21.html")
