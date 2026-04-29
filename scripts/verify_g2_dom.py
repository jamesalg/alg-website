#!/usr/bin/env python3
import re, os

DIST = '/home/ubuntu/alg-website/dist/collections'
PAGES = [
    'vintage-decor/edison',
    'vintage-decor/victorian',
    'vintage-decor/tubular',
    'vintage-decor/radio',
    'vintage-decor/candelabra',
    'vintage-decor/globe',
    'nostalgic-decor/a19',
    'nostalgic-decor/b10',
    'nostalgic-decor/ca10',
    'nostalgic-decor/g25',
    'nostalgic-decor/s14',
]

print(f"{'Page':<35} {'sw':>4} {'tl':>4} {'mr':>4} {'lp':>5} {'cor':>5} {'KB':>5} {'status':>6}")
print('-' * 75)
all_ok = True
for p in PAGES:
    path = os.path.join(DIST, p, 'index.html')
    if not os.path.exists(path):
        print(f"  {p}: MISSING")
        all_ok = False
        continue
    with open(path) as f:
        html = f.read()
    sw = len(re.findall(r'class="[^"]*swatch', html))
    tl = len(re.findall(r'class="[^"]*toc-link', html))
    mr = len(re.findall(r'class="[^"]*matrix-row', html))
    lp = 'lifestyle-photo' in html
    cor = 'Cormorant' in html[:4000]
    sz = len(html) // 1024
    ok = (sw >= 3 and tl >= 5 and mr >= 22 and lp and cor)
    if not ok:
        all_ok = False
    status = 'OK' if ok else 'FAIL'
    print(f"  {p:<33} {sw:>4} {tl:>4} {mr:>4} {str(lp):>5} {str(cor):>5} {sz:>4}KB  {status}")

print()
print('G2 OVERALL:', 'PASS' if all_ok else 'FAIL')
