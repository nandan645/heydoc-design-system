---
name: heydoc-design-system
description: Use for any HeyDoc AI visual work (slides, frames, animated scenes, explainer film, marketing pages, mockups, dashboards) so it follows the HeyDoc design system's tokens, components, motion and rules.
---

# HeyDoc Design System

HeyDoc AI's visual and motion language: white canvas, Open Sans, HeyDoc blues, one soft shadow, generous radius, and motion where one shape morphs through many states. This skill tells you where the system lives, the rules that are never broken, and how to build with it.

## 1. Find the system (in this order)

1. **Connected folder.** If a folder named `Design System` (Windows: `Documents\HeyDoc\Design System`) is connected, work from it. It is a git repo. Read `AGENTS.md` first.
2. **GitHub.** Otherwise clone `https://github.com/nandan645/heydoc-design-system` (private: needs the person's access) and read `AGENTS.md`.
3. **Neither available.** Use the essentials in sections 3–7 below. They are enough for a correct frame or scene. Say that you worked from the skill's summary, not the full repo.

Key files in the repo:

| Need | File |
|---|---|
| Rules | `docs/principles.md`, `AGENTS.md` |
| Every token | `css/tokens.css` (`tokens/tokens.json` is the same data) |
| Component classes | `docs/components.md`, CSS in `css/components.css` |
| Motion | `docs/motion.md`, `js/motion.js` (`window.HD`) |
| Partner colours | `docs/accent-system.md`, `js/brand.js`, `scripts/brand.py "#HEX"` |
| Voice and numbers | `docs/content.md` |
| One-file versions for artifacts | `dist/heydoc.bundle.css`, `dist/heydoc.bundle.js` |
| Starters | `examples/starter-frame.html`, `examples/starter-scene.html` |
| Everything rendered | `examples/element-board.html` |

Don't read `examples/*.html` or `source/` whole: they are 1–2 MB generated files. Search them.

## 2. Rules (never break)

1. **White canvas only.** No dark backgrounds, no fades to black. Transitions wipe or fade through white. (A phone's own dark wallpaper is allowed.)
2. **Tokens only.** No invented hex codes, sizes, radii, shadows or easings.
3. **Reuse `.hd-*` components** before making new ones; new ones use BEM (`.hd-block__part--variant`).
4. **No people, no stock photos, no real patient or hospital data.** Mockups, cards, maps, dots and counters only.
5. **Numbers are illustrative** and set per use case. If a figure isn't known, show `<span class="hd-ph">[N]</span>` instead of a number that looks final.
6. **Fonts:** Open Sans everywhere; Inter only inside phone/app mockups.
7. **Headlines:** short, sentence case, colour exactly one phrase with `<em>`. In films, one headline size for every scene (60px).
8. **Partner brands** (when their product is on screen) change only the accent slot. Text, type, layout, radius, shadow and motion stay HeyDoc.
9. **Names:** HeyDoc AI · "The Agentic Care OS" · **heydoc.co.in** (never heydoc.ai). Colour HeyDoc logo only (no white logo, no SVG exists).
10. **Restricted:** government marks (Maharashtra seal, NHA) and partner screenshots need approval before public use.

## 3. Essential tokens

```css
:root{
  --navy:#012b44; --blue:#0873ba; --sky:#139bf5; --pale:#8fcdf8; --tint:#eef7fd; --line:#d6e7f4;
  --muted:#5b6b78; --grey:#f4f6f8; --cyan:#3fd4f6;
  /* pastel surface + its ink (anything on a pastel uses that ink) */
  --aqua:#caf4f3; --aqua-ink:#0f8a85; --sun:#fff2cd; --sun-ink:#a87508; --peach:#ffdeaf; --peach-ink:#bd6512;
  --mint:#cbefd1; --mint-ink:#1f8a43; --rose:#fde0da; --rose-ink:#c8394f; --lav:#cad4f4; --lav-ink:#4a5bc4;
  /* status only */ --d-amber:#feb64f; --d-rose:#ea5c72; --d-mint:#3be6a2;
  --bg-wash:linear-gradient(160deg,#fff 0%,#fff 45%,#e9f8fb 70%,#c9f1f4 100%);
  --grad:linear-gradient(90deg,#1789f2,#3fd4f6);
  --orb:radial-gradient(circle at 28% 18%,#0a84e8 0%,#2ba7f5 55%,#43d0f2 100%);
  --font:'Open Sans',system-ui,sans-serif; --font-ui:'Inter',system-ui,sans-serif;
  --t-hero:84px; --t-title:56px; --t-scene:60px; --t-lead:30px; --t-body:28px; --t-small:22px; --t-kicker:19px; --t-mega:280px;
  --s-2:8px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px; --s-8:64px; --s-10:120px;
  --r-pill:999px; --r-panel:28px; --r-card:24px; --r-inner:16px; --r-sm:12px;
  --shadow-layered:0 1px 2px rgba(1,43,68,.05),0 4px 12px rgba(1,43,68,.05),0 10px 32px rgba(1,43,68,.07);
  --shadow-glow:0 12px 30px rgba(23,137,242,.30);
  --ease-out:cubic-bezier(.22,1,.36,1); --ease-in:cubic-bezier(.55,0,1,.45);
  --ease-in-out:cubic-bezier(.65,0,.35,1); --ease-spring:cubic-bezier(.34,1.56,.64,1);
  --dur-s:300ms; --dur-m:600ms; --dur-l:1200ms; --dur-xl:2400ms; --stagger:60ms;
}
```

Text: navy (14.7:1) or muted (5.5:1). Accent text: `--blue` (5.0:1). Never sky or pale for body text. Canvas 1920×1080, safe margins 120px sides.

## 4. Core components

| Need | Use |
|---|---|
| Kicker / headline / subline | `.hd-kicker`, `.hd-headline` (+`--xl`), `.hd-subline`, `.hd-caption` |
| Button | `.hd-btn--primary` (gradient, one per view), `--navy`, `--secondary`, `--ghost` |
| Chip / tag | `.hd-chip` (+`--solid` = active), `.hd-tag--mint/sun/rose/sky…` |
| Icon in a circle | `.hd-well--aqua/sun/peach/mint/rose/lav` + 24-grid stroke icon (2.2, round) |
| Card / stat | `.hd-panel`, `.hd-stat`, `.hd-statchip`, `.hd-counter`, `.hd-bignum--light` |
| Agent | `.hd-agent.is-idle` / `.is-active` (gradient border + glow) |
| Care segments | `.hd-seg--lav/aqua/mint/sun` |
| Phone | `.hd-ip` (vector iPhone, `--phone-w`), `.hd-scr`, `.hd-bubble--agent/--user` |
| Journey | `.hd-jrny` (kept vs lost), `.hd-jcol` (step stack), `.hd-flow` (today vs with HeyDoc) |
| Logos | `.hd-logotile` on white; `.hd-brandmark` (HeyDoc logo, in the bundle) |
| Not-yet-known figure | `.hd-ph` |

## 5. Motion

- Every scene is `render(t)`: a pure function of time. No CSS transitions or timers. `HD.player({duration, render, stage})` gives play/pause/seek and `?t=` deep links.
- `HD.P(t, start, dur, HD.EASE.out)` = eased 0→1. Entrances `out`, exits `in`, moves `inOut`, pops `spring`, shape morphs `soft`.
- Recipes: `HD.inOut` (rise 24px + fade + de-blur), `HD.words` (headline word by word, 60ms), `HD.pop`, `HD.ring` (highlight a tap target), `HD.count` (count-up, en-IN), `HD.hueMix` (colour hand-off).
- **One shape, many states:** morph the element you have (pulse → phone → panel → tile → dot) instead of cutting. Shape first, content blurs in ~0.35s after. Ripple on arrival. Hand-offs: match position/size/radius, cross-fade 0.2–0.3s.

## 6. Partner accent (one hex in)

`HDBrand.apply('#246B45')` (or `python3 scripts/brand.py "#HEX"`) sets `--partner`, `-deep` (20% to black), `-light` (+16 lightness), `-pale` (62% to white), `-line` (80%), `-tint` (90%), `-dot`, `-ink` (darkened until ≥3:1 on white; use for text), `-on` (text on a fill), `-orb`, `-grad`. Switch accents over ~0.6s with `HD.hueMix` at a story beat. Examples: Habuild `#246B45`, Pathkind `#FFCD05` (ink `#B39004`).

## 7. Voice

A presenter: loud and clear about the problem and the solution, empathetic without drama ("lost", not "panic"; nobody blamed). Thread: every result should come with a clear next step. Indian number formats (₹, `1,50,000`, `₹300 Cr`).

## 8. Workflow

1. Settle the output: static frame, animated scene, slide, or page.
2. Start from a starter (`examples/starter-frame.html` / `starter-scene.html`). For a Claude artifact or any single file, **inline `dist/heydoc.bundle.css` and `dist/heydoc.bundle.js`** instead of linking several files.
3. Build with tokens and `.hd-*` components only.
4. Render and look at it (screenshots; for scenes, capture key frames with `window.__render(t)`).
5. Check: white canvas · one `<em>` per headline · tokens only · no real data · heydoc.co.in · tell the person which numbers are illustrative.
6. If you add a component or token to the repo: update `docs/components.md` or both token files, run `python3 scripts/check_tokens.py`, `python3 scripts/bundle.py`, `./scripts/build.sh`, and add a CHANGELOG line.
