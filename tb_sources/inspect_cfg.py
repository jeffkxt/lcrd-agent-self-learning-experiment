import json, pathlib, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def lst(url):
    r = requests.get(url, timeout=60, verify=False, headers={"User-Agent":"Mozilla/5.0"})
    try:
        d = json.loads(r.content)
        return [(e.get("type"), e.get("name"), e.get("size")) for e in d]
    except:
        return ("RAW", r.status_code, r.text[:200])
print("TB2_CONFIGS", lst("https://api.github.com/repos/laude-institute/terminal-bench-experiments/contents/configs/tb2"))
print("TB15_CONFIGS", lst("https://api.github.com/repos/laude-institute/terminal-bench-experiments/contents/configs/tb1-5"))
print("TASK_DIR", lst("https://api.github.com/repos/harbor-framework/terminal-bench-1/contents/original-tasks/adaptive-rejection-sampler"))
