import requests, pathlib, urllib3, json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def lst(url):
    r = requests.get(url, timeout=60, verify=False, headers={"User-Agent":"Mozilla/5.0"})
    try:
        return json.loads(r.content)
    except:
        return []
d = lst("https://api.github.com/repos/harbor-framework/terminal-bench-2-1/contents/tasks")
print("TB21_TASKS", len(d))
names = [e.get("name") for e in d]
print(names)
print("TASK_DIR", lst("https://api.github.com/repos/harbor-framework/terminal-bench-2-1/contents/tasks/adaptive-rejection-sampler"))
