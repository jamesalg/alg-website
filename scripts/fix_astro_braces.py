#!/usr/bin/env python3
"""
Escape curly brace expressions in HTML markup (outside script/style/frontmatter)
that Astro would try to evaluate as JSX expressions.
Strategy: replace { with {'{'} and } with {'}'} — Astro's escape syntax for literal braces.
Only in HTML sections, not inside script/style blocks or frontmatter.
"""
import re, os

SLUGS = [
    "anaheim", "atlanta", "aura", "everest", "guardian",
    "heritage", "navigator", "nightwatch", "pathfinder",
    "radiator", "ramparts", "sentinel", "watchtower", "wedge"
]

def fix_page(path):
    with open(path) as f:
        content = f.read()
    
    original = content
    
    # Split into segments: frontmatter, script/style blocks, and HTML
    # We need to only modify the HTML parts
    
    # First, extract frontmatter (between --- markers at start)
    fm_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        rest = content[len(frontmatter):]
    else:
        frontmatter = ''
        rest = content
    
    # Now process the rest: replace { and } in HTML sections only
    # We'll use a state machine approach
    result_parts = [frontmatter]
    
    # Find all script and style blocks and their positions
    protected_ranges = []
    for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', rest, re.DOTALL):
        protected_ranges.append((m.start(), m.end()))
    
    # Also protect HTML comments
    for m in re.finditer(r'<!--.*?-->', rest, re.DOTALL):
        protected_ranges.append((m.start(), m.end()))
    
    # Sort ranges
    protected_ranges.sort()
    
    # Process the rest, escaping braces only in unprotected sections
    pos = 0
    result = []
    for start, end in protected_ranges:
        # Process unprotected section before this range
        unprotected = rest[pos:start]
        # Escape { and } that are Astro expressions
        # Only escape { that start an expression (not already escaped)
        # Astro expression: {anything} where anything is not empty
        # Replace {expr} with {'{'}{expr}{'}'} — no, simpler:
        # Replace { with {'{'} and } with {'}'} in HTML context
        # But we need to be careful not to break CSS in style attributes
        # Actually the safest approach: only escape { that appear to be template vars
        # i.e., {word}, {word|word}, {/regex?}, etc.
        # Pattern: { followed by non-whitespace content that's not valid JS
        
        # Replace all { } pairs that look like template placeholders
        # These are: {word}, {word|word}, {/regex}, {number|number}
        def escape_braces(text):
            # Replace { with {'{'} only when it's a template expression
            # A template expression is: { followed by non-space content, then }
            # that doesn't start with a valid JS expression opener
            # Simplest: escape ALL { and } in HTML that aren't in attributes with CSS
            
            # Actually, the safest fix for Astro is to use set:html or just
            # replace { with &#123; and } with &#125; in text content
            # But in attribute values, { is fine as long as it's not a valid JS expr
            
            # The problematic patterns we found:
            # {150|300}, {U|H}, {/UA?}, {/PS?}, {/BLS?}, {wattage}, {cct}, etc.
            # These are all in text content (inside tags), not in attribute values
            
            # Replace { } pairs that look like SKU template vars
            # Pattern: {[A-Za-z0-9_/|?]+}
            result = re.sub(
                r'\{([A-Za-z0-9_.\-/|? ,]+)\}',
                lambda m: '&#123;' + m.group(1) + '&#125;',
                text
            )
            return result
        
        result.append(escape_braces(unprotected))
        result.append(rest[start:end])
        pos = end
    
    # Process remaining unprotected section
    remaining = rest[pos:]
    result.append(escape_braces(remaining))
    
    new_content = frontmatter + ''.join(result)
    
    if new_content != original:
        with open(path, 'w') as f:
            f.write(new_content)
        # Count replacements
        count = new_content.count('&#123;')
        print(f"Fixed {path.split('/')[-3]}: {count} brace escapes")
        return count
    else:
        print(f"No changes: {path.split('/')[-3]}")
        return 0

total = 0
for slug in SLUGS:
    path = f'/home/ubuntu/alg-website/src/pages/products/{slug}/index.astro'
    if os.path.exists(path):
        total += fix_page(path)
    else:
        print(f"MISSING: {slug}")

print(f"\nTotal brace escapes: {total}")
