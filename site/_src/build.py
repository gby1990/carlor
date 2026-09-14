#!/usr/bin/env python3
"""Assemble site/*.html from _src/pages/*.html + header/footer."""
import pathlib, re
src = pathlib.Path(__file__).parent
out = src.parent
hdr = (src/'header.html').read_text()
ftr = (src/'footer.html').read_text()
for page in sorted((src/'pages').glob('*.html')):
    body = page.read_text()
    m = re.match(r'<!--\s*title:(.*?)\|\s*desc:(.*?)-->\s*', body, re.S)
    title, desc = (m.group(1).strip(), m.group(2).strip()) if m else (page.stem.title(), '')
    body = body[m.end():] if m else body
    html = hdr.replace('{{TITLE}}', title).replace('{{DESC}}', desc) + body + ftr
    (out/page.name).write_text(html)
    print('wrote', page.name)
