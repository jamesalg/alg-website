#!/usr/bin/env python3
"""Fix naked Ⓐ in tubulararch pages by wrapping in <span class="aa">Ⓐ</span>"""
import os, re

BASE = '/home/ubuntu/alg-website/src/pages/collections/tubulararch'
NAKED = '\u24b6'  # Ⓐ
WRAPPED = '<span class="aa">\u24b6</span>'

files = ['t5.astro', 'pl.astro', 'pll.astro', 'u6.astro']

for fname in files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count naked Ⓐ before fix
    naked_count = content.count(NAKED)
    
    # Replace all naked Ⓐ with wrapped version
    # But don't double-wrap already-wrapped ones
    # Strategy: replace WRAPPED back to placeholder, fix all naked, restore
    PLACEHOLDER = '__AA_WRAPPED__'
    content2 = content.replace(WRAPPED, PLACEHOLDER)
    content2 = content2.replace(NAKED, WRAPPED)
    content2 = content2.replace(PLACEHOLDER, WRAPPED)
    
    wrapped_count = content2.count(WRAPPED)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content2)
    
    print(f'  {fname}: {naked_count} naked Ⓐ → {wrapped_count} wrapped')

print('Done.')
