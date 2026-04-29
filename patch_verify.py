#!/usr/bin/env python3
"""Patch verify.mjs to add headStripped step in J.1 regex fallback."""

with open('scripts/verify.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact line to insert after
old_line = "        const commentStripped = html.replace(/<!--[\\s\\S]*?-->/g, '__COMMENT__');\n        const scriptStripped = commentStripped.replace(/<script[\\s\\S]*?<\\/script>/gi, '__SCRIPT__');"
new_lines = "        const commentStripped = html.replace(/<!--[\\s\\S]*?-->/g, '__COMMENT__');\n        const headStripped = commentStripped.replace(/<head[\\s\\S]*?<\\/head>/gi, '__HEAD__');\n        const scriptStripped = headStripped.replace(/<script[\\s\\S]*?<\\/script>/gi, '__SCRIPT__');"

if old_line in content:
    content = content.replace(old_line, new_lines, 1)
    with open('scripts/verify.mjs', 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK - patched successfully')
else:
    # Try to find the lines individually to debug
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'commentStripped' in line and 'html.replace' in line:
            print(f'Line {i+1}: {repr(line)}')
        if 'scriptStripped' in line and 'commentStripped' in line:
            print(f'Line {i+1}: {repr(line)}')
    print('NOT FOUND - see above for actual line content')
