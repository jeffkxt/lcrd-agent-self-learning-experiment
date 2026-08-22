import pathlib, yaml, json
names = ["adaptive-rejection-sampler","break-filter-js-from-html","chess-best-move","caffe-cifar-10","constraints-scheduling","db-wal-recovery"]
print("YAML_KEYS")
for n in names:
    p = pathlib.Path(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/task_%s.yaml" % n)
    try:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        print("%s keys=%s cat=%s diff=%s" % (n, list(d.keys()), d.get("category"), d.get("difficulty")))
    except Exception as e:
        print("%s ERR %r" % (n, e))
