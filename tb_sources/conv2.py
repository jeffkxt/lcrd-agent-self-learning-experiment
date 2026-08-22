import pathlib, re, html as h
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
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/deepwiki_12.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/deepwiki_12.txt")
totext(r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbcom_index.html", r"C:/MyDocuments/Documents/LCRDTEST/tb_sources/tbcom_index.txt")
