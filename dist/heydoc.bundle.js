/* HeyDoc Design System 1.1.0 · single-file bundle: motion.js + brand.js (generated, do not edit) */
/* =====================================================================
   HeyDoc Design System · motion.js · v1.0.0
   Deterministic motion helpers: every frame is a pure function of time t (seconds).
   Same easing as css/tokens.css, plus springs, a scene player and the shape-morph helper.
   No dependencies. Load with <script src="js/motion.js"></script> → window.HD
   ===================================================================== */
(function (root) {
  'use strict';

  /* ---------- math ---------- */
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, p) => a + (b - a) * p;

  /* cubic-bezier solver (same curves as the CSS tokens) */
  function bez(x1, y1, x2, y2) {
    const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
    const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
    const X = t => ((ax * t + bx) * t + cx) * t, Y = t => ((ay * t + by) * t + cy) * t, dX = t => (3 * ax * t + 2 * bx) * t + cx;
    return x => {
      if (x <= 0) return 0; if (x >= 1) return 1;
      let t = x;
      for (let i = 0; i < 8; i++) { const d = dX(t); if (Math.abs(d) < 1e-6) break; t -= (X(t) - x) / d; }
      return Y(clamp(t));
    };
  }

  /* damped spring as a 0→1 easing (zeta = damping ratio, w = stiffness); always lands exactly on 1 */
  function spring(zeta, w) {
    const wd = w * Math.sqrt(1 - zeta * zeta);
    return p => {
      if (p <= 0) return 0; if (p >= 1) return 1;
      const v = 1 - Math.exp(-zeta * w * p) * (Math.cos(wd * p) + zeta * w / wd * Math.sin(wd * p));
      return v + (1 - v) * Math.pow(p, 6);
    };
  }

  /* motion tokens (see docs/motion.md) */
  const EASE = {
    linear: x => x,
    out: bez(.22, 1, .36, 1),        // --ease-out     · entrances, count-ups
    in: bez(.55, 0, 1, .45),         // --ease-in      · exits
    inOut: bez(.65, 0, .35, 1),      // --ease-in-out  · moves, camera, swaps
    spring: spring(.5, 12),          // --ease-spring  · pops, badges, pins (overshoots)
    soft: spring(.78, 10),           //                · shape morphs (settles, barely overshoots)
  };
  const DUR = { xs: .15, s: .3, m: .6, l: 1.2, xl: 2.4, stagger: .06 };   // seconds

  /* progress of a tween that starts at t0 and lasts d seconds */
  const P = (t, t0, d, e = EASE.out) => e(clamp((t - t0) / d));
  /* 0 → 1 → 0 hump over [t0, t0+d] (beats, presses, squash) */
  const bump = (t, t0, d) => { const p = (t - t0) / d; return p > 0 && p < 1 ? Math.sin(p * Math.PI) : 0; };
  /* smooth deterministic noise in roughly [-1, 1] (jitter, breathing) */
  const noise = (seed, t) => Math.sin(t * 13.1 + seed * 7.3) * .5 + Math.sin(t * 23.7 + seed * 3.1) * .3 + Math.sin(t * 7.9 + seed * 11) * .2;
  /* seeded random (same layout every load) */
  function rng(seed) { let s = seed >>> 0 || 1; return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296; }

  /* ---------- ready-made recipes ---------- */
  /* enter: rise + fade + de-blur; exit: lift + fade + blur. Apply to any element. */
  function inOut(el, t, a, b = Infinity, dy = 24) {
    const p = P(t, a, DUR.m, EASE.out), q = P(t, b, .4, EASE.in);
    el.style.opacity = p * (1 - q);
    el.style.transform = `translateY(${dy * (1 - p) - 16 * q}px)`;
    const bl = 8 * (1 - p) + 8 * q; el.style.filter = bl > .2 ? `blur(${bl}px)` : 'none';
  }
  /* headline word-by-word: words = array of .w spans */
  function words(list, t, a, b = Infinity) {
    list.forEach((w, j) => inOut(w, t, a + j * DUR.stagger, b + j * .03));
  }
  /* pop: spring scale-in for chips, pins, bubbles */
  function pop(el, t, a, dy = 12) {
    const p = P(t, a, .45, EASE.spring);
    el.style.opacity = clamp((t - a) / .15);
    el.style.transform = `translateY(${(1 - p) * dy}px) scale(${.92 + .08 * p})`;
  }
  /* ring highlight: two expanding rings (box-shadow) around a UI element */
  function ring(el, t, a, rgb = '19,155,245') {
    let sp = 0, al = 0;
    [a, a + .55].forEach(f => { const rp = clamp((t - f) / .8); if (rp > 0 && rp < 1) { sp = Math.max(sp, 14 * EASE.out(rp)); al = Math.max(al, .4 * (1 - rp)); } });
    el.style.boxShadow = al > .002 ? `0 0 0 2px rgba(${rgb},${Math.min(1, al * 2.2)}),0 0 0 ${sp}px rgba(${rgb},${al})` : 'none';
  }
  /* count-up with Indian digit grouping */
  function count(el, t, a, to, d = DUR.l, from = 0) {
    el.textContent = Math.round(lerp(from, to, P(t, a, d, EASE.out))).toLocaleString('en-IN');
  }

  /* ---------- shape morph ("one shape, many states") ----------
     A shell is a box that keeps its identity while it changes size, radius and content:
     pulse (circle) → phone → panel → tile → dot.  Markup:
       <div class="hd-shell"><div class="hd-shell__bg"></div><div class="hd-shell__orb"></div>
         <div class="hd-shell__clip"><div class="hd-shell__content">…</div></div></div>
     state = {x,y,w,h,r,s,rot,op, bg,orb, cop,cb, ring,ringA,ringRGB}                         */
  function shell(el) {
    return { el, bg: el.querySelector('.hd-shell__bg'), orb: el.querySelector('.hd-shell__orb'), ct: el.querySelector('.hd-shell__content') };
  }
  function applyShell(o, st, prev) {
    const v = prev ? Math.hypot(st.x - prev.x, st.y - prev.y) : 0, mb = clamp(v * .14, 0, 9);   // motion blur from velocity
    const s = o.el.style;
    s.width = st.w + 'px'; s.height = st.h + 'px'; s.borderRadius = st.r + 'px';
    s.transform = `translate(${st.x}px,${st.y}px) translate(-50%,-50%) rotate(${st.rot || 0}deg) scale(${st.s == null ? 1 : st.s})`;
    s.opacity = st.op == null ? 1 : st.op; s.filter = mb > .3 ? `blur(${mb.toFixed(2)}px)` : 'none';
    s.boxShadow = st.ringA > .002 ? `0 0 0 ${st.ring}px rgba(${st.ringRGB || '19,155,245'},${st.ringA})` : '';
    if (o.bg) o.bg.style.opacity = st.bg == null ? 1 : st.bg;
    if (o.orb) o.orb.style.opacity = st.orb || 0;
    if (o.ct) { o.ct.style.opacity = st.cop == null ? 1 : st.cop; o.ct.style.filter = st.cb > .2 ? `blur(${st.cb}px)` : 'none'; }
  }

  /* ---------- hue-path colour blend (no muddy mid-tones between brand colours) ---------- */
  function hsl(hex) {
    let [r, g, b] = [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16) / 255);
    const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2; let s = 0, h = 0;
    if (mx !== mn) { const d = mx - mn; s = l > .5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h *= 60; }
    return [h, s * 100, l * 100];
  }
  function hueMix(a, b, p) {
    const A = hsl(a), B = hsl(b); let dh = B[0] - A[0]; if (dh > 180) dh -= 360; if (dh < -180) dh += 360;
    return `hsl(${(A[0] + dh * p + 360) % 360},${lerp(A[1], B[1], p)}%,${lerp(A[2], B[2], p)}%)`;
  }

  /* ---------- player: fixed 1920×1080 stage, scaled to fit; play/pause/seek; ?t= deep link ----------
     HD.player({ duration: 12, render: t => {…}, stage: '#stage', markers: [[0,'1'],[4,'2']] })      */
  function player(opt) {
    const stage = typeof opt.stage === 'string' ? document.querySelector(opt.stage) : opt.stage;
    const D = opt.duration; let T = 0, playing = true, last = null;
    const bar = document.createElement('div'); bar.className = 'hd-player';
    bar.innerHTML = `<button class="hd-player__pp" aria-label="Play or pause"></button><div class="hd-player__bar">${(opt.markers || []).map(([s, n]) => `<span style="left:${s / D * 100}%">${n}</span>`).join('')}<input type="range" min="0" max="${D}" step="0.001" value="0"></div><span class="hd-player__tc"></span>`;
    document.body.appendChild(bar);
    const pp = bar.querySelector('button'), range = bar.querySelector('input'), tc = bar.querySelector('.hd-player__tc');
    const icon = () => pp.innerHTML = playing ? '<svg width="14" height="14" viewBox="0 0 14 14"><rect x="2" y="1" width="3.5" height="12" rx="1" fill="#fff"/><rect x="8.5" y="1" width="3.5" height="12" rx="1" fill="#fff"/></svg>' : '<svg width="14" height="14" viewBox="0 0 14 14"><path d="M3 1.5v11l9-5.5z" fill="#fff"/></svg>';
    const fit = () => { const k = Math.min(innerWidth / 1920, innerHeight / 1080); stage.style.transform = `translate(${(innerWidth - 1920 * k) / 2}px,${(innerHeight - 1080 * k) / 2}px) scale(${k})`; };
    const set = v => { T = clamp(v, 0, D); opt.render(T); range.value = T; tc.textContent = `${T.toFixed(2)} / ${D.toFixed(2)}`; };
    const frame = now => { if (last == null) last = now; const dt = (now - last) / 1000; last = now; if (playing) { let n = T + dt; if (n >= D) n = opt.loop === false ? (playing = false, icon(), D) : 0; set(n); } requestAnimationFrame(frame); };
    pp.onclick = () => { playing = !playing; if (playing && T >= D) T = 0; icon(); };
    range.oninput = () => { playing = false; icon(); set(+range.value); };
    addEventListener('keydown', e => {
      if (e.target.closest && e.target.closest('input,textarea')) return;
      if (e.code === 'Space') { e.preventDefault(); pp.click(); }
      if (e.key === 'ArrowRight') { playing = false; icon(); set(T + (e.shiftKey ? 1 : 1 / 30)); }
      if (e.key === 'ArrowLeft') { playing = false; icon(); set(T - (e.shiftKey ? 1 : 1 / 30)); }
    });
    addEventListener('resize', fit); fit();
    const q = new URLSearchParams(location.search); if (q.has('t')) { T = +q.get('t'); playing = q.get('play') === '1'; }
    window.__render = t => { playing = false; icon(); set(t); };   // hook for frame capture (Playwright etc.)
    icon(); set(T); requestAnimationFrame(frame);
    return { seek: set, play: () => { playing = true; icon(); }, pause: () => { playing = false; icon(); }, get time() { return T; } };
  }

  root.HD = { clamp, lerp, bez, spring, EASE, DUR, P, bump, noise, rng, inOut, words, pop, ring, count, shell, applyShell, hueMix, player };
})(window);

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
