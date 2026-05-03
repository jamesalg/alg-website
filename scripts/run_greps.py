#!/usr/bin/env python3.11
import subprocess, os

os.chdir('/home/ubuntu/alg-website')

def grep(label, pattern, path="src/", flags="", include="--include=*.astro --include=*.html --include=*.css --include=*.scss"):
    cmd = f'grep -rn {flags} "{pattern}" {path} {include} 2>/dev/null'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    hits = result.stdout.strip()
    count = len(hits.splitlines()) if hits else 0
    print(f"\n=== {label} === ({count} hits)")
    if hits:
        for line in hits.splitlines()[:8]:
            print(f"  {line}")
    else:
        print("  (none)")

grep("G1: utility-bar-right wrapper", "utility-bar-right", include="--include=*.astro --include=*.html")
grep("G2a: Find a Distributor", "Find a Distributor", include="--include=*.astro --include=*.html")
grep("G2b: Find a Rep", "Find a Rep", include="--include=*.astro --include=*.html")
grep("G2c: Sample Request", "Sample Request", include="--include=*.astro --include=*.html")
grep("G2d: Contact href", '/contact"', include="--include=*.astro --include=*.html")
grep("G3: --header-bottom defined", r"\-\-header-bottom", include="--include=*.css --include=*.scss --include=*.astro")
grep("G4: scroll-padding-top var", "scroll-padding-top.*--header-bottom", include="--include=*.css --include=*.scss --include=*.astro")
grep("G5: is-main-nav-hidden JS", "is-main-nav-hidden", include="--include=*.js --include=*.ts --include=*.astro")
grep("G6: isProgrammaticScroll", "isProgrammaticScroll", include="--include=*.js --include=*.ts --include=*.astro")
grep("G7: top:120px (should be 0)", r"top:\s*120px", include="--include=*.css --include=*.scss")
grep("G8: Slogan", r"Lighting | Reinvented, since 1997\.", include="--include=*.astro --include=*.html")
grep("G9: Reinvented since 1997 (no comma)", "Reinvented since 1997")
grep("G10: Lighting Reinvented (no pipe)", "Lighting Reinvented")
grep("G11: Watt Selectable", "Watt Selectable")
grep("G12: Accreditation", r"accredit\|CEU\|AIA\|IDCEC\|HSW", flags="-i", include="--include=*.astro --include=*.md")
grep("G13: Wrong brand red hex", r"#E3353C\|#FF0000\|#E60000\|#D32F2F", include="--include=*.css --include=*.scss")
print("\nDone.")
