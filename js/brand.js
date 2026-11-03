/* =====================================================================
   HeyDoc Design System · brand.js · v1.0.0
   Partner accent system: ONE brand hex in → every shade out (docs/accent-system.md).
   Mirrors scripts/brand.py exactly, so print and screen agree.
     HDBrand.derive('#246B45')               → { base, deep, light, pale, line, tint, dot, ink, on, rgb }
     HDBrand.apply('#246B45', el?, 'partner') → sets --partner, --partner-deep … on el (default :root)
   ===================================================================== */
(function (root) {
  'use strict';
  const rgb = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
  const hex = c => '#' + c.map(v => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, '0')).join('');
  const mix = (a, b, p) => { const A = rgb(a), B = rgb(b); return hex(A.map((v, i) => v + (B[i] - v) * p)); };
  const lum = h => { const [r, g, b] = rgb(h).map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * r + .7152 * g + .0722 * b; };
  const contrast = (a, b = '#ffffff') => { const x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); };
  function hsl(h) {
    let [r, g, b] = rgb(h).map(v => v / 255); const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2; let s = 0, hh = 0;
    if (mx !== mn) { const d = mx - mn; s = l > .5 ? d / (2 - mx - mn) : d / (mx + mn); hh = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; hh *= 60; }
    return [hh, s, l];
  }
  function lighter(h, d = .16) {   // same hue + saturation, +16 lightness (capped at 82%)
    const [hh, s] = hsl(h), L = Math.min(hsl(h)[2] + d, .82), a = s * Math.min(L, 1 - L);
    const f = n => { const k = (n + hh / 30) % 12; return 255 * (L - a * Math.max(-1, Math.min(k - 3, 9 - k, 1))); };
    return hex([f(0), f(8), f(4)]);
  }
  function derive(base) {
    base = hex(rgb(base.toLowerCase()));
    let ink = base, k = 0;
    while (contrast(ink) < 3 && k < 20) { k++; ink = mix(base, '#000000', k * .05); }   // text on white ≥ 3:1
    return {
      base, deep: mix(base, '#000000', .2), light: lighter(base),
      pale: mix(base, '#ffffff', .62), line: mix(base, '#ffffff', .8), tint: mix(base, '#ffffff', .9),
      dot: mix(base, '#eceff1', .86), ink, on: contrast(base) >= 3 ? '#ffffff' : '#012b44', rgb: rgb(base).join(','),
    };
  }
  function apply(color, el = document.documentElement, slot = 'partner') {
    const T = derive(color), s = el.style;
    s.setProperty(`--${slot}`, T.base);
    ['deep', 'light', 'pale', 'line', 'tint', 'dot', 'ink', 'on', 'rgb'].forEach(k => s.setProperty(`--${slot}-${k}`, T[k]));
    s.setProperty(`--${slot}-orb`, `radial-gradient(circle at 30% 22%,${T.deep} 0%,${T.base} 55%,${T.light} 100%)`);
    s.setProperty(`--${slot}-grad`, `linear-gradient(90deg,${T.base},${T.light})`);
    return T;
  }
  root.HDBrand = { derive, apply, contrast, mix };
})(window);
