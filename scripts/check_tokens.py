#!/usr/bin/env python3
"""Verify tokens/tokens.json and css/tokens.css agree. Exit 1 on any mismatch (use in CI or before committing)."""
import json, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css = dict(re.findall(r'(--[\w-]+):([^;]+);', open(os.path.join(R, 'css/tokens.css')).read()))
css = {k: v.strip() for k, v in css.items()}
bad = 0
def walk(n):
    global bad
    for k, v in n.items():
        if isinstance(v, dict) and '$value' in v:
            c = v['css']
            if c not in css: print(f'missing in css/tokens.css: {c}'); bad += 1
            elif css[c] != v['$value']: print(f'value differs for {c}: json={v["$value"]}  css={css[c]}'); bad += 1
        elif isinstance(v, dict): walk(v)
walk(json.load(open(os.path.join(R, 'tokens/tokens.json'))))
print('tokens OK' if not bad else f'{bad} problem(s)'); sys.exit(1 if bad else 0)
