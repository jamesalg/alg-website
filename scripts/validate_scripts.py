#!/usr/bin/env python3
"""Validate each <script> block in all new PDP pages using Node.js acorn parser."""
import re, subprocess, os, tempfile

SLUGS = [
    "anaheim", "atlanta", "aura", "everest", "guardian",
    "heritage", "navigator", "nightwatch", "pathfinder",
    "radiator", "ramparts", "sentinel", "watchtower", "wedge"
]

def validate_js(js_code, label):
    """Use node --check to validate JS syntax."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
        f.write(js_code)
        fname = f.name
    try:
        result = subprocess.run(
            ['node', '--check', fname],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return result.stderr.strip()
        return None
    except Exception as e:
        return str(e)
    finally:
        os.unlink(fname)

total_errors = 0
for slug in SLUGS:
    path = f'/home/ubuntu/alg-website/src/pages/products/{slug}/index.astro'
    if not os.path.exists(path):
        print(f"MISSING: {slug}")
        continue
    
    with open(path) as f:
        content = f.read()
    
    script_blocks = list(re.finditer(r'<script([^>]*)>(.*?)</script>', content, re.DOTALL))
    page_errors = 0
    for i, m in enumerate(script_blocks):
        tag = m.group(1).strip()
        body = m.group(2)
        
        # Skip JSON-LD blocks
        if 'application/ld+json' in tag:
            continue
        # Skip blocks with type= that aren't plain JS
        if 'type=' in tag and 'module' not in tag and 'text/javascript' not in tag:
            continue
        
        error = validate_js(body, f"{slug} block {i}")
        if error:
            # Get line number from error
            line_match = re.search(r':(\d+)', error)
            line_num = int(line_match.group(1)) if line_match else '?'
            
            # Find the actual problematic line
            lines = body.split('\n')
            if isinstance(line_num, int) and line_num <= len(lines):
                bad_line = lines[line_num - 1]
            else:
                bad_line = '(unknown)'
            
            print(f"\nERROR in {slug} block {i} ({len(body)} chars):")
            print(f"  {error[:200]}")
            print(f"  Bad line: {repr(bad_line[:150])}")
            page_errors += 1
            total_errors += 1
    
    if page_errors == 0:
        print(f"OK: {slug}")

print(f"\nTotal errors: {total_errors}")
