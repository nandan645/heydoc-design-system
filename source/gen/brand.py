"""Universal accent system: two states.
   HeyDoc  = the core design-system blues (fixed tokens in css.py).
   Partner = ONE brand hex per partner section; every other shade is derived from it with the rules below,
             so any company can be dropped in by changing a single colour.
The same rules run in the film's JS (DERIVE_JS) so colours can be changed live in Edit mode."""

# partner slots used by the film. Change `color` (or use Edit mode → Brand colours) to re-skin a section.
PARTNERS = [
    {'slot': 'partner1', 'name': 'Habuild',  'section': 'Act 2 · 16–34s', 'color': '#246B45'},
    {'slot': 'partner2', 'name': 'Pathkind', 'section': 'Act 3 · 34–54s', 'color': '#FFCD05'},
]

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

def root_css():
    return ':root{' + ';'.join(css_vars(p['slot'], derive(p['color'])) for p in PARTNERS) + '}\n'

DERIVE_JS = r'''
/* ---------- universal accents: HeyDoc (fixed) + Partner (one hex → all shades) ---------- */
const BR={rgb:h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)),hex:c=>'#'+c.map(v=>Math.max(0,Math.min(255,Math.round(v))).toString(16).padStart(2,'0')).join('')};
BR.mix=(a,b,p)=>{const A=BR.rgb(a),B=BR.rgb(b);return BR.hex(A.map((v,i)=>v+(B[i]-v)*p))};
BR.lum=h=>{const [r,g,b]=BR.rgb(h).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b};
BR.con=(a,b='#ffffff')=>{const x=BR.lum(a),y=BR.lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
function derive(base){base=base.toLowerCase();let ink=base,k=0;while(BR.con(ink)<3&&k<20){k++;ink=BR.mix(base,'#000000',k*.05)}
  const T={base,deep:BR.mix(base,'#000000',.2),light:lighter(base),pale:BR.mix(base,'#ffffff',.62),line:BR.mix(base,'#ffffff',.8),tint:BR.mix(base,'#ffffff',.9),
    dot:BR.mix(base,'#eceff1',.86),ink,on:BR.con(base)>=3?'#ffffff':'#012b44'};T.rgb=BR.rgb(base).join(',');return T}
function lighter(h,d=16){const [hh,ss,l]=hslOf(h);const L=Math.min(l+d,82)/100,S=ss/100,a=S*Math.min(L,1-L),f=n=>{const k=(n+hh/30)%12;return 255*(L-a*Math.max(-1,Math.min(k-3,9-k,1)))};return BR.hex([f(0),f(8),f(4)])}
// hue-path blend between two brand colours (never a muddy straight RGB mix)
function hslOf(h){let [r,g,b]=BR.rgb(h).map(v=>v/255);const mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2;let s=0,hh=0;
  if(mx!==mn){const d=mx-mn;s=l>.5?d/(2-mx-mn):d/(mx+mn);hh=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;hh*=60}return [hh,s*100,l*100]}
function hueMix(a,b,p){const A=hslOf(a),B=hslOf(b);let dh=B[0]-A[0];if(dh>180)dh-=360;if(dh<-180)dh+=360;return `hsl(${(A[0]+dh*p+360)%360},${A[1]+(B[1]-A[1])*p}%,${A[2]+(B[2]-A[2])*p}%)`}
const PARTNERS=__PARTNERS__;const ACC={};
function applyBrand(){PARTNERS.forEach(p=>{const c=(ED.brand&&ED.brand[p.slot])||p.color,T=derive(c);ACC[p.slot]=T;const s=document.documentElement.style;
  s.setProperty('--'+p.slot,T.base);['deep','light','pale','line','tint','dot','ink','on','rgb'].forEach(k=>s.setProperty(`--${p.slot}-${k}`,T[k]));
  s.setProperty(`--${p.slot}-orb`,`radial-gradient(circle at 30% 22%,${T.deep} 0%,${T.base} 55%,${T.light} 100%)`);s.setProperty(`--${p.slot}-grad`,`linear-gradient(90deg,${T.base},${T.light})`)})}
'''
