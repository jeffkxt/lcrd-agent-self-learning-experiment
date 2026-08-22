import sys, requests, pathlib
url = sys.argv[1]
out = sys.argv[2]
r = requests.get(url, timeout=90, allow_redirects=True, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) research-fetch"})
pathlib.Path(out).write_bytes(r.content)
print(f"OK status={r.status_code} bytes={len(r.content)} saved={out}")
