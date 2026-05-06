#!/usr/bin/env python3
"""
fix_j1_violations.py — v2.7.23
Wraps bare Ⓐ (U+24B6) and ⓐ (U+24D0) characters in <span class="aa">…</span>
across all 14 new luxoARCH PDP .astro source files.

Rules:
- Only touch HTML content sections (not inside <style>…</style> or <script>…</script>)
- Only wrap Ⓐ/ⓐ that are NOT already inside <span class="aa">
- Handles both uppercase Ⓐ (U+24B6) and lowercase ⓐ (U+24D0)
- Also wraps Ⓐ/ⓐ inside alt="" attribute values (the verifier checks text nodes only,
  but alt text is not a text node so those are safe — skip alt attrs to avoid double-wrapping)
"""

import re
import os
import sys

SLUGS = [
    "anaheim", "atlanta", "aura", "everest", "guardian",
    "heritage", "navigator", "nightwatch", "pathfinder",
    "radiator", "ramparts", "sentinel", "watchtower", "wedge"
]

PAGES_DIR = "/home/ubuntu/alg-website/src/pages/products"

# Characters to wrap
AA_CHARS = "\u24b6\u24d0"  # Ⓐ ⓐ

def wrap_aa_in_html_chunk(chunk: str) -> str:
    """
    In a chunk of HTML (not script/style), wrap bare Ⓐ/ⓐ that are not
    already inside <span class="aa">…</span>.
    
    Strategy: use a regex that matches either:
      (a) already-wrapped: <span class="aa">Ⓐ</span>  → keep as-is
      (b) bare Ⓐ/ⓐ → wrap it
    """
    # Pattern: match already-wrapped spans OR bare Ⓐ/ⓐ
    # We use a "consume already-wrapped, replace bare" approach
    already_wrapped = re.compile(
        r'<span\s+class=["\']aa["\']>[\u24b6\u24d0]</span>'
    )
    
    result = []
    pos = 0
    text = chunk
    
    while pos < len(text):
        # Try to find the next Ⓐ/ⓐ character
        next_aa = -1
        next_char = None
        for i, c in enumerate(text[pos:], pos):
            if c in AA_CHARS:
                next_aa = i
                next_char = c
                break
        
        if next_aa == -1:
            # No more Ⓐ/ⓐ — append rest and done
            result.append(text[pos:])
            break
        
        # Append everything up to this Ⓐ/ⓐ
        result.append(text[pos:next_aa])
        
        # Check if this Ⓐ/ⓐ is already inside <span class="aa">
        # Look back for <span class="aa"> and forward for </span>
        # Simple heuristic: check if the preceding text (up to 30 chars) ends with
        # <span class="aa"> or <span class='aa'>
        preceding = text[max(0, next_aa-30):next_aa]
        following = text[next_aa+1:next_aa+10]
        
        already = (
            (preceding.endswith('<span class="aa">') or preceding.endswith("<span class='aa'>"))
            and following.startswith('</span>')
        )
        
        if already:
            # Already wrapped — emit as-is
            result.append(next_char)
        else:
            # Wrap it
            result.append(f'<span class="aa">{next_char}</span>')
        
        pos = next_aa + 1
    
    return ''.join(result)


def split_into_sections(content: str):
    """
    Split .astro file content into alternating sections:
    - 'html': content outside <style> and <script> blocks
    - 'style': content inside <style>…</style>
    - 'script': content inside <script>…</script>
    
    Returns list of (section_type, text) tuples.
    """
    # We need to handle nested/multiple style and script blocks
    # Use a state machine approach
    sections = []
    pos = 0
    text = content
    
    # Pattern to find opening <style or <script tags (not self-closing)
    tag_open = re.compile(r'<(style|script)(\s[^>]*)?>(?!.*/>)', re.IGNORECASE)
    
    while pos < len(text):
        m = tag_open.search(text, pos)
        if not m:
            # Rest is HTML
            sections.append(('html', text[pos:]))
            break
        
        tag_name = m.group(1).lower()
        tag_start = m.start()
        tag_end = m.end()
        
        # Append HTML section before this tag
        if tag_start > pos:
            sections.append(('html', text[pos:tag_start]))
        
        # Find the closing tag
        close_tag = f'</{tag_name}>'
        close_pos = text.lower().find(close_tag.lower(), tag_end)
        
        if close_pos == -1:
            # No closing tag found — treat rest as this type
            sections.append((tag_name, text[tag_start:]))
            pos = len(text)
            break
        
        close_end = close_pos + len(close_tag)
        sections.append((tag_name, text[tag_start:close_end]))
        pos = close_end
    
    return sections


def fix_file(filepath: str) -> tuple[int, int]:
    """Fix J.1 violations in a single .astro file. Returns (changes_made, aa_wraps)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    sections = split_into_sections(original)
    
    total_wraps = 0
    fixed_sections = []
    
    for section_type, section_text in sections:
        if section_type == 'html':
            fixed = wrap_aa_in_html_chunk(section_text)
            wraps = fixed.count('<span class="aa">') - section_text.count('<span class="aa">')
            total_wraps += wraps
            fixed_sections.append(fixed)
        else:
            # script or style — leave untouched
            fixed_sections.append(section_text)
    
    result = ''.join(fixed_sections)
    
    if result != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return 1, total_wraps
    
    return 0, 0


def main():
    total_files_changed = 0
    total_wraps = 0
    
    for slug in SLUGS:
        filepath = os.path.join(PAGES_DIR, slug, 'index.astro')
        if not os.path.exists(filepath):
            print(f"  MISSING: {filepath}")
            continue
        
        changed, wraps = fix_file(filepath)
        if changed:
            print(f"  Fixed {slug}: {wraps} Ⓐ/ⓐ wraps")
            total_files_changed += 1
            total_wraps += wraps
        else:
            print(f"  No changes: {slug}")
    
    print(f"\nTotal: {total_files_changed} files changed, {total_wraps} Ⓐ/ⓐ wraps applied")


if __name__ == '__main__':
    main()
