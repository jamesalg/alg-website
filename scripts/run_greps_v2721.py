#!/usr/bin/env python3
import subprocess, re

SRC = '/home/ubuntu/alg-website/src'

def grep(pattern, path='', flags='', count_only=False):
    cmd = f'grep -rn {flags} "{pattern}" {path or SRC}'
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if count_only:
        return len([l for l in r.stdout.splitlines() if l.strip()])
    return r.stdout.strip()

def grep_file(pattern, filepath, flags=''):
    r = subprocess.run(f'grep -n {flags} "{pattern}" {filepath}', shell=True, capture_output=True, text=True)
    return r.stdout.strip()

H = f'{SRC}/components/Header.astro'
C = f'{SRC}/pages/collections/consumer.astro'

print("=== G1: site-header.is-main-nav-hidden in CSS (expect 0) ===")
hits = grep_file(r'site-header\.is-main-nav-hidden', H)
print(f"  Hits: {len(hits.splitlines()) if hits else 0}")
print(f"  {hits[:200] if hits else '(none)'}")

print("\n=== G2: :root.is-main-nav-hidden in CSS (expect >=1) ===")
hits = grep_file(r':root\.is-main-nav-hidden', H)
print(f"  Hits: {len(hits.splitlines()) if hits else 0}")
print(f"  {hits[:200] if hits else '(none)'}")

print("\n=== G3: JS toggle target (expect documentElement) ===")
hits = grep_file(r'is-main-nav-hidden', H)
for line in hits.splitlines():
    if 'classList.toggle' in line or 'classList.add' in line or 'classList.remove' in line:
        print(f"  {line}")

print("\n=== G4: --header-bottom NOT in prefers-reduced-motion (expect 0) ===")
r = subprocess.run(f'grep -A 8 "prefers-reduced-motion" {H}', shell=True, capture_output=True, text=True)
header_bottom_in_rm = [l for l in r.stdout.splitlines() if '--header-bottom' in l]
print(f"  Hits: {len(header_bottom_in_rm)}")
if header_bottom_in_rm:
    print(f"  FAIL: {header_bottom_in_rm}")

print("\n=== G5: transition-duration:0ms in reduced-motion (expect >=1) ===")
r = subprocess.run(f'grep -A 10 "prefers-reduced-motion" {H}', shell=True, capture_output=True, text=True)
td_hits = [l for l in r.stdout.splitlines() if 'transition-duration' in l and '0' in l]
print(f"  Hits: {len(td_hits)}")
for l in td_hits:
    print(f"  {l.strip()}")

print("\n=== G6: no inherit in .site-tagline typography (expect 0) ===")
r = subprocess.run(f'grep -A 20 ".site-tagline" {H}', shell=True, capture_output=True, text=True)
inherit_hits = [l for l in r.stdout.splitlines()
                if re.search(r'font-(family|size|weight)|letter-spacing|line-height', l)
                and 'inherit' in l.lower()]
print(f"  Hits: {len(inherit_hits)}")
if inherit_hits:
    print(f"  FAIL: {inherit_hits}")

print("\n=== G7: explicit font-size in .site-tagline (expect >=1) ===")
r = subprocess.run(f'grep -A 20 ".site-tagline" {H}', shell=True, capture_output=True, text=True)
fs_hits = [l for l in r.stdout.splitlines() if re.search(r'font-size:\s*[0-9]', l)]
print(f"  Hits: {len(fs_hits)}: {[l.strip() for l in fs_hits]}")

print("\n=== G7b: explicit letter-spacing in .site-tagline (expect >=1) ===")
ls_hits = [l for l in r.stdout.splitlines() if re.search(r'letter-spacing:\s*[0-9]', l)]
print(f"  Hits: {len(ls_hits)}: {[l.strip() for l in ls_hits]}")

print("\n=== G8: --page-sticky-extra defined (expect >=2) ===")
r2 = subprocess.run(f'grep -rn -- "--page-sticky-extra" {SRC}', shell=True, capture_output=True, text=True)
lines = [l for l in r2.stdout.splitlines() if l.strip()]
print(f"  Hits: {len(lines)}")
for l in lines:
    print(f"  {l}")

print("\n=== G9: scroll-padding-top with calc() (expect 1 with calc) ===")
r3 = subprocess.run(f'grep -rn "scroll-padding-top" {SRC}', shell=True, capture_output=True, text=True)
for l in r3.stdout.splitlines():
    print(f"  {l}")

print("\n=== Standard: slogan exact (expect >=1) ===")
r4 = subprocess.run(f'grep -rn "Lighting | Reinvented, since 1997\\." {SRC} --include="*.astro"', shell=True, capture_output=True, text=True)
print(f"  Hits: {len(r4.stdout.splitlines())}")

print("\n=== Standard: no Reinvented since (no comma, expect 0) ===")
r5 = subprocess.run(f'grep -rn "Reinvented since 1997" {SRC}', shell=True, capture_output=True, text=True)
bad = [l for l in r5.stdout.splitlines() if 'Reinvented, since 1997' not in l]
print(f"  Violations: {len(bad)}")

print("\n=== Standard: no Watt Selectable (expect 0) ===")
r6 = subprocess.run(f'grep -rn "Watt Selectable" {SRC}', shell=True, capture_output=True, text=True)
print(f"  Hits: {len(r6.stdout.splitlines())}")

print("\n=== Standard: no wrong red hex (expect 0) ===")
r7 = subprocess.run(f'grep -rn "#E3353C|#FF0000|#E60000|#D32F2F" {SRC} --include="*.css" --include="*.scss"', shell=True, capture_output=True, text=True)
print(f"  Hits: {len(r7.stdout.splitlines())}")

print("\nDONE")
