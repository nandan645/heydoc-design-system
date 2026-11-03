# Motion

HeyDoc motion is **calm, continuous and exact**: shapes morph instead of cutting, content blurs in as a shape settles, and every frame is reproducible. Reference: comotion's "one shape, many states".

## 1. The model: `render(t)`

Every scene is a pure function of time:

```js
function render(t) { /* set every element's style from t (seconds) */ }
HD.player({ duration: 12, render, stage: '#stage' });
```

- **Deterministic.** The same `t` always gives the same frame, so you can scrub, deep-link (`?t=4.2`), capture frames for video (`window.__render(t)` with Playwright) and review frame by frame.
- **No CSS transitions or `setTimeout` in scenes.** Timing lives in named constants (`const MORPH = 1.6`) at the top of the script.
- **Previous frame for velocity.** Pass `state(t - 1/60)` so movement can add a little motion blur (`HD.applyShell` does this).

## 2. Tokens

| Easing | Curve | Use |
|---|---|---|
| `HD.EASE.out` · `--ease-out` | cubic-bezier(.22,1,.36,1) | Entrances, count-ups, reveals |
| `HD.EASE.in` · `--ease-in` | cubic-bezier(.55,0,1,.45) | Exits |
| `HD.EASE.inOut` · `--ease-in-out` | cubic-bezier(.65,0,.35,1) | Moves, camera, screen swaps |
| `HD.EASE.spring` · `--ease-spring` | spring ζ .5 | Pops: chips, pins, badges, bubbles |
| `HD.EASE.soft` | spring ζ .78 | Shape morphs (settles, barely overshoots) |

| Duration | Value | Use |
|---|---|---|
| xs | 150ms | Taps, flashes |
| s | 300ms | Pops, fades |
| m | 600ms | Standard entrance |
| l | 1.2s | Count-ups, reveals, morphs |
| xl | 2.4s | Camera moves, long journeys |
| stagger | 60ms | Between siblings (words, chips, tiles) |

`HD.P(t, start, duration, ease)` returns eased progress 0→1. `HD.bump(t, start, duration)` returns a 0→1→0 hump for beats and presses.

## 3. Recipes (all in `js/motion.js`)

| Recipe | Call | What it does |
|---|---|---|
| Enter / exit | `HD.inOut(el, t, in, out)` | Rise 24px + fade + de-blur 8px → lift 16px + fade + blur |
| Headline | `HD.words(wordSpans, t, in, out)` | Word-by-word rise, 60ms stagger |
| Pop | `HD.pop(el, t, at)` | Spring scale .92→1 + rise 12px |
| Ring highlight | `HD.ring(el, t, at, rgb)` | Two expanding rings around a UI element (tap target, alert) |
| Count-up | `HD.count(el, t, at, to)` | Ease-out count with Indian digit grouping (1,50,000) |
| Colour hand-off | `HD.hueMix(a, b, p)` | Blend two brand colours along the hue wheel (green → lime → yellow, never olive) |

## 4. The shape-morph pattern ("one shape, many states")

One element, `.hd-shell`, travels through states. Each state is a plain object:

```js
{ x, y,          // centre, px from stage centre
  w, h, r,       // size and corner radius: circle → phone → panel → tile → dot
  s, rot, op,    // scale, rotation, opacity
  bg, orb,       // white card vs coloured orb (0..1)
  cop, cb,       // content opacity and blur
  ring, ringA, ringRGB }  // ripple ring
```

Write one `state(t)` function per shell that **starts from its resting state and layers each beat on top**:

```js
function coreState(t) {
  const st = { x:0, y:0, w:96, h:96, r:48, s:1, bg:1, orb:1, cop:0, cb:8 };
  const m = HD.P(t, MORPH, .9, HD.EASE.soft);         // pulse → card
  st.w = HD.lerp(96, 360, m); st.h = HD.lerp(96, 236, m); st.r = HD.lerp(48, 24, m);
  st.orb = 1 - HD.P(t, MORPH + .1, .35);              // colour drains as it opens
  st.cop = HD.P(t, MORPH + .35, .45); st.cb = 8 * (1 - st.cop);  // content blurs in after the shape settles
  return st;
}
```

Rules:
- **Shape first, content second.** Content fades and de-blurs ~0.35s after a morph starts and is gone before the next one starts.
- **Morphs use `soft`, pops use `spring`, moves use `inOut`.**
- **Hand-offs:** when two elements must swap, put them at the same position, size and radius at the swap moment and cross-fade over 0.2–0.3s.
- **Ripple on arrival:** a ring (`ring: 46*out(p)`, `ringA: .3*(1-p)`) when a shape lands or an agent fires.
- **Heartbeat:** `s *= 1 + .07*bump(t, beat, .45)` on the pulse at story beats.

## 5. Camera

Scenes can move a world container instead of every element: `translate(960px,540px) scale(z) translate(-cx,-cy)`. Ease camera moves with `inOut` over 1–1.6s. Zoom out to reveal scale; zoom in to focus.

## 6. Section accent hand-off

When the story moves from HeyDoc to a partner (or between partners), blend the accent over ~0.6s with `HD.hueMix`, on the element that carries the story (the orb, the dots). See `accent-system.md`.

## 7. Checklist before you ship a scene

- [ ] Scrubbing backwards and forwards shows no jumps (no state depends on the previous frame).
- [ ] Nothing pops in at full opacity: everything has an entrance.
- [ ] One headline size across the film (`--t-scene`).
- [ ] Every number is either final or marked `[N]`.
- [ ] Frame captures at `?t=` for every beat look right on their own.
