#!/usr/bin/env python3
"""HeyDoc partner accent: one brand hex in, every shade out.
Usage:  python3 scripts/brand.py "#246B45"            → table + CSS custom properties
        python3 scripts/brand.py "#246B45" --slot acme  → --acme, --acme-deep …
Same rules as js/brand.js (see docs/accent-system.md)."""
import sys
def _rgb(h): h = h.lstrip('#'); return [int(h[i:i+2], 16) for i in (0, 2, 4)]
def _hex(c): return '#' + ''.join(f'{max(0, min(255, int(v + .5))):02x}' for v in c)
def _mix(a, b, p): A, B = _rgb(a), _rgb(b); return _hex([x + (y - x) * p for x, y in zip(A, B)])
def _lum(h):
    def ch(v):
        v /= 255; return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = map(ch, _rgb(h)); return .2126 * r + .7152 * g + .0722 * b
def contrast(a, b='#ffffff'):
    x, y = sorted([_lum(a), _lum(b)], reverse=True); return (x + .05) / (y + .05)

import colorsys
def _lighter(h, d=16):
    r, g, b = [v / 255 for v in _rgb(h)]; hh, l, ss = colorsys.rgb_to_hls(r, g, b)
    return _hex([v * 255 for v in colorsys.hls_to_rgb(hh, min(l + d / 100, .82), ss)])

def derive(base):
    """one brand hex -> full partner token set"""
    base = _hex(_rgb(base))
    ink = base; k = 0
    while contrast(ink) < 3 and k < 20:            # text on white: darken until ≥ 3:1 (large-text AA)
        k += 1; ink = _mix(base, '#000000', k * .05)
    T = {'base': base, 'deep': _mix(base, '#000000', .2), 'light': _lighter(base),
         'pale': _mix(base, '#ffffff', .62), 'line': _mix(base, '#ffffff', .8), 'tint': _mix(base, '#ffffff', .9),
         'dot': _mix(base, '#eceff1', .86), 'ink': ink, 'on': '#ffffff' if contrast(base) >= 3 else '#012b44'}
    T['rgb'] = ','.join(map(str, _rgb(base)))
    return T

def css_vars(slot, T):
    v = {f'--{slot}': T['base']}
    for k in ('deep', 'light', 'pale', 'line', 'tint', 'dot', 'ink', 'on', 'rgb'): v[f'--{slot}-{k}'] = T[k]
    v[f'--{slot}-orb'] = f'radial-gradient(circle at 30% 22%,{T["deep"]} 0%,{T["base"]} 55%,{T["light"]} 100%)'
    v[f'--{slot}-grad'] = f'linear-gradient(90deg,{T["base"]},{T["light"]})'
    return ';'.join(f'{k}:{x}' for k, x in v.items())


if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit(1)
    col = sys.argv[1]; slot = sys.argv[sys.argv.index('--slot') + 1] if '--slot' in sys.argv else 'partner'
    T = derive(col)
    w = max(len(k) for k in T)
    for k, v in T.items(): print(f'{k:<{w}}  {v}' + (f'   contrast on white {contrast(v):.2f}:1' if k in ('base', 'ink') else ''))
    print('\n:root{' + css_vars(slot, T).replace(';', ';\n  ') + '}')
