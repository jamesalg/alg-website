#!/usr/bin/env python3
"""
fix_j1_v2.py — v2.7.23 (corrected)
Fixes J.1 violations: wraps bare Ⓐ (U+24B6) and ⓐ (U+24D0) in <span class="aa">…</span>
across all 14 new luxoARCH PDP .astro source files.

This version correctly:
1. Undoes bad wrapping inside HTML attribute values (alt, title, aria-label, etc.)
2. Only wraps Ⓐ/ⓐ in TEXT CONTENT (between tags), not inside attribute values
3. Skips <style> and <script> blocks entirely
4. Fixes double-wrapping issues from the previous script run

The verifier (J.1) checks text nodes in the rendered DOM — it does NOT check
attribute values. So Ⓐ in alt="" is fine as-is; only Ⓐ in text content needs wrapping.
"""

import re
import os

SLUGS = [
    "anaheim", "atlanta", "aura", "everest", "guardian",
    "heritage", "navigator", "nightwatch", "pathfinder",
    "radiator", "ramparts", "sentinel", "watchtower", "wedge"
]

PAGES_DIR = "/home/ubuntu/alg-website/src/pages/products"

AA_CHARS = "\u24b6\u24d0"  # Ⓐ ⓐ

WRAPPED_AA = re.compile(r'<span\s+class=["\']aa["\'][^>]*>[\u24b6\u24d0]</span>')
DOUBLE_WRAPPED = re.compile(r'<span\s+class=["\']aa[^"\']*["\']><span\s+class=["\']aa["\']>([\u24b6\u24d0])</span></span>')


def undo_attr_wrapping(content: str) -> str:
    """
    Undo <span class="aa">Ⓐ</span> wrapping that ended up inside HTML attribute values.
    
    Strategy: find all attribute values (content between quotes after = in a tag),
    and within those, replace <span class="aa">Ⓐ</span> back to bare Ⓐ.
    
    We handle this by tokenizing the content into:
    - attribute values (between quotes in tag contexts)
    - everything else
    """
    result = []
    pos = 0
    text = content
    
    # We need to find attribute values within HTML tags
    # A tag starts with < and ends with > (not inside quotes)
    # We'll use a state machine
    
    in_tag = False
    in_attr_value = False
    attr_quote = None
    i = 0
    
    while i < len(text):
        ch = text[i]
        
        if not in_tag and not in_attr_value:
            if ch == '<' and i + 1 < len(text) and text[i+1] not in ('!',):
                # Check it's not a comment or CDATA
                if text[i:i+4] != '<!--' and text[i:i+9] != '<![CDATA[':
                    in_tag = True
            result.append(ch)
            i += 1
        elif in_tag and not in_attr_value:
            if ch in ('"', "'"):
                in_attr_value = True
                attr_quote = ch
                result.append(ch)
                i += 1
            elif ch == '>':
                in_tag = False
                result.append(ch)
                i += 1
            else:
                result.append(ch)
                i += 1
        elif in_attr_value:
            if ch == attr_quote:
                in_attr_value = False
                attr_quote = None
                result.append(ch)
                i += 1
            else:
                # We're inside an attribute value — check for wrapped Ⓐ
                # Try to match <span class="aa">Ⓐ</span> at this position
                span_match = re.match(
                    r'<span\s+class=["\']aa["\']>([\u24b6\u24d0])</span>',
                    text[i:]
                )
                if span_match:
                    # Replace with bare character
                    result.append(span_match.group(1))
                    i += len(span_match.group(0))
                else:
                    result.append(ch)
                    i += 1
        else:
            result.append(ch)
            i += 1
    
    return ''.join(result)


def fix_double_wraps(content: str) -> str:
    """Fix double-wrapped spans: <span class="aa X"><span class="aa">Ⓐ</span></span> → <span class="aa X">Ⓐ</span>"""
    # Pattern: outer span with aa class wrapping inner span.aa wrapping Ⓐ
    # Replace with just the outer span containing bare Ⓐ
    result = re.sub(
        r'(<span\s+class=["\']aa[^"\']*["\']>)<span\s+class=["\']aa["\']>([\u24b6\u24d0])</span>(</span>)',
        lambda m: m.group(1) + m.group(2) + m.group(3),
        content
    )
    return result


def split_into_sections(content: str):
    """
    Split .astro file content into sections:
    - 'html': content outside <style> and <script> blocks
    - 'style': content inside <style>…</style>
    - 'script': content inside <script>…</script>
    """
    sections = []
    pos = 0
    text = content
    
    tag_open = re.compile(r'<(style|script)(\s[^>]*)?>(?!.*/>)', re.IGNORECASE)
    
    while pos < len(text):
        m = tag_open.search(text, pos)
        if not m:
            sections.append(('html', text[pos:]))
            break
        
        tag_name = m.group(1).lower()
        tag_start = m.start()
        tag_end = m.end()
        
        if tag_start > pos:
            sections.append(('html', text[pos:tag_start]))
        
        close_tag = f'</{tag_name}>'
        close_pos = text.lower().find(close_tag.lower(), tag_end)
        
        if close_pos == -1:
            sections.append((tag_name, text[tag_start:]))
            pos = len(text)
            break
        
        close_end = close_pos + len(close_tag)
        sections.append((tag_name, text[tag_start:close_end]))
        pos = close_end
    
    return sections


def wrap_aa_in_text_content(chunk: str) -> str:
    """
    In an HTML chunk, wrap bare Ⓐ/ⓐ in text content (not in attribute values).
    
    Tokenize into: tag content (< to >) vs text content (> to <).
    Only process text content sections.
    """
    result = []
    pos = 0
    text = chunk
    
    while pos < len(text):
        # Find the next < (start of a tag)
        tag_start = text.find('<', pos)
        
        if tag_start == -1:
            # Rest is text content
            text_chunk = text[pos:]
            result.append(wrap_bare_aa(text_chunk))
            break
        
        # Process text content before this tag
        if tag_start > pos:
            text_chunk = text[pos:tag_start]
            result.append(wrap_bare_aa(text_chunk))
        
        # Find the end of this tag (handling quoted attributes)
        tag_end = find_tag_end(text, tag_start)
        
        if tag_end == -1:
            # Malformed — just append rest as-is
            result.append(text[tag_start:])
            break
        
        # Append the tag as-is (no wrapping inside tags)
        result.append(text[tag_start:tag_end])
        pos = tag_end
    
    return ''.join(result)


def find_tag_end(text: str, start: int) -> int:
    """Find the position after the closing > of a tag, respecting quoted attributes."""
    i = start + 1  # skip the <
    
    # Handle comments
    if text[i:i+3] == '!--':
        end = text.find('-->', i)
        return end + 3 if end != -1 else -1
    
    in_quote = False
    quote_char = None
    
    while i < len(text):
        ch = text[i]
        if in_quote:
            if ch == quote_char:
                in_quote = False
        else:
            if ch in ('"', "'"):
                in_quote = True
                quote_char = ch
            elif ch == '>':
                return i + 1
        i += 1
    
    return -1


def wrap_bare_aa(text: str) -> str:
    """Wrap bare Ⓐ/ⓐ in text that is NOT already wrapped."""
    if not any(c in text for c in AA_CHARS):
        return text
    
    result = []
    i = 0
    
    while i < len(text):
        ch = text[i]
        
        if ch in AA_CHARS:
            # Check if already wrapped: look back for <span class="aa"> and forward for </span>
            preceding = text[max(0, i-30):i]
            following = text[i+1:i+10]
            
            already = (
                (preceding.endswith('<span class="aa">') or preceding.endswith("<span class='aa'>"))
                and following.startswith('</span>')
            )
            
            if already:
                result.append(ch)
            else:
                result.append(f'<span class="aa">{ch}</span>')
        else:
            result.append(ch)
        
        i += 1
    
    return ''.join(result)


def fix_file(filepath: str) -> tuple[int, int, int]:
    """Fix J.1 violations in a single .astro file. Returns (changed, wraps, undos)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    # Step 1: Undo bad wrapping inside attribute values
    step1 = undo_attr_wrapping(original)
    
    # Step 2: Fix double-wraps
    step2 = fix_double_wraps(step1)
    
    # Step 3: Process HTML sections to wrap bare Ⓐ/ⓐ in text content
    sections = split_into_sections(step2)
    
    fixed_sections = []
    total_wraps = 0
    
    for section_type, section_text in sections:
        if section_type == 'html':
            fixed = wrap_aa_in_text_content(section_text)
            wraps = fixed.count('<span class="aa">') - section_text.count('<span class="aa">')
            total_wraps += wraps
            fixed_sections.append(fixed)
        else:
            # script or style — leave untouched
            fixed_sections.append(section_text)
    
    result = ''.join(fixed_sections)
    
    # Count undos
    undos = original.count('<span class="aa">') - step1.count('<span class="aa">')
    
    if result != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return 1, total_wraps, undos
    
    return 0, 0, 0


def main():
    total_files_changed = 0
    total_wraps = 0
    total_undos = 0
    
    for slug in SLUGS:
        filepath = os.path.join(PAGES_DIR, slug, 'index.astro')
        if not os.path.exists(filepath):
            print(f"  MISSING: {filepath}")
            continue
        
        changed, wraps, undos = fix_file(filepath)
        if changed:
            print(f"  Fixed {slug}: +{wraps} wraps, -{undos} attr undos")
            total_files_changed += 1
            total_wraps += wraps
            total_undos += undos
        else:
            print(f"  No changes: {slug}")
    
    print(f"\nTotal: {total_files_changed} files changed, +{total_wraps} wraps, -{total_undos} attr undos")


if __name__ == '__main__':
    main()
