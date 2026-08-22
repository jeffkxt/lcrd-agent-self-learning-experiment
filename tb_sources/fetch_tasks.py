import requests, pathlib, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
tasks = ["adaptive-rejection-sampler","break-filter-js-from-html","chess-best-move","caffe-cifar-10","constraints-scheduling","db-wal-recovery"]
for t in tasks:
    url = "https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/original-tasks/%s/task.yaml" % t
    out = r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/task_%s.yaml" % t
    try:
        r = requests.get(url, timeout=90, allow_redirects=True, verify=False, headers={"User-Agent":"Mozilla/5.0 (research)"})
        pathlib.Path(out).write_bytes(r.content)
        print("OK status=%d bytes=%d url=%s saved=%s" % (r.status_code, len(r.content), url, out))
    except Exception as e:
        print("ERR %s %r" % (url, e))
