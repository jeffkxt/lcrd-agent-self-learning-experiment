import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def grab(url, out):
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("ZAI_HARBORFMT OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ZAI_HARBORFMT ERR %s %r" % (url, e))
grab("https://huggingface.co/datasets/zai-org/terminal-bench-2-verified", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/zai_verified.html")
grab("https://harborframework.com/docs/task-format", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/harbor_task_format.html")
