# HeyDoc Design System

The visual and motion language of **HeyDoc AI**: tokens, components, icons, motion helpers, assets and worked examples for decks, product frames, explainer films and marketing visuals.

> **Version 1.0.0** · white-canvas, Open Sans, HeyDoc blues, one soft shadow, motion that morphs one shape through many states.

---

## Start in 2 minutes

1. Open **`examples/element-board.html`** in a browser. It shows every component, static, with its motion notes.
2. Open **`examples/starter-scene.html`**. It's an 8-second animated scene built only from this system. Scrub it with the bar; add `?brand=%23246B45` to the URL to see a partner colour applied.
3. To make something new, copy a starter:
   - **`examples/starter-frame.html`** for a static 1920×1080 frame (slide, keyframe, social card)
   - **`examples/starter-scene.html`** for an animated scene
4. Link one stylesheet and you have everything:

```html
<link rel="stylesheet" href="css/heydoc.css">        <!-- fonts + tokens + base + components + scene -->
<script src="js/motion.js"></script>                   <!-- window.HD: easing, springs, player, shape morph -->
<script src="js/brand.js"></script>                    <!-- window.HDBrand: partner colour from one hex -->
```

```html
<div class="hd-kicker">Scene 09</div>
<h1 class="hd-headline">4 care segments. <em>One company brain.</em></h1>
<button class="hd-btn hd-btn--primary">Book a test</button>
```

No build step and no dependencies. Every file works from `file://`.

---

## What's inside

| Path | What it is |
|---|---|
| `css/tokens.css` | Every design value as CSS custom properties: colour, type, space, radius, shadow, motion, partner slot |
| `tokens/tokens.json` | The same tokens in W3C design-tokens format (for Style Dictionary, Tokens Studio or code) |
| `css/base.css` | Reset and type defaults |
| `css/components.css` | All `.hd-*` components |
| `css/scene.css` | Stage, shape-morph shell and player for animated scenes |
| `css/heydoc.css` | One import for all of the above plus fonts |
| `js/motion.js` | Deterministic motion: easing tokens, springs, `P()` tweens, recipes, shape morph, scene player |
| `js/brand.js` | Partner accent: one brand hex → full shade set, applied as CSS variables |
| `icons/` | 38 stroke icons (24 grid, 2.2 stroke, round): individual SVGs, a sprite and JSON |
| `assets/logos/` | HeyDoc and partner logos |
| `assets/maps/` | India and Maharashtra outlines, land points for the dot globe |
| `assets/partner-screens/` | Partner app screenshots used in the film (**restricted**, see `docs/assets.md`) |
| `examples/` | Element board, explainer film (reference implementation), starters |
| `source/` | Python generators that build the element board and the film |
| `scripts/` | `build.sh`, `brand.py` (accent calculator), `check_tokens.py` |
| `docs/` | The written system. Start with `docs/README.md` |

## Documentation

| Read | When |
|---|---|
| [`docs/principles.md`](docs/principles.md) | Always, first. The rules that make it look like HeyDoc |
| [`docs/foundations.md`](docs/foundations.md) | Colour, type, space, shape, shadow |
| [`docs/components.md`](docs/components.md) | Which component to use, its classes and variants |
| [`docs/motion.md`](docs/motion.md) | Animating anything: tokens, recipes, the shape-morph pattern |
| [`docs/accent-system.md`](docs/accent-system.md) | Putting a partner brand (any company) into a scene |
| [`docs/content.md`](docs/content.md) | Voice, headlines, numbers and placeholders |
| [`docs/assets.md`](docs/assets.md) | Logos, screenshots, maps: what's cleared and what isn't |
| [`docs/film.md`](docs/film.md) | The 1:55 explainer film, scene by scene, as a worked example |
| [`docs/open-items.md`](docs/open-items.md) | Placeholders, approvals and decisions still pending |
| [`AGENTS.md`](AGENTS.md) | Briefing for AI assistants working in this repo |

## Rebuilding the board and film

```bash
./scripts/build.sh            # rebuilds examples/element-board.html
./scripts/build.sh --film     # also rebuilds examples/explainer-film.html
python3 scripts/check_tokens.py   # tokens.json and tokens.css must agree
```

Needs Python 3.9+ (standard library only).

## Ownership

Design: **Abhinandan Kumar** (abhinandan@heydoc.co.in) · HeyDoc AI.
Changes go through pull requests (see [`CONTRIBUTING.md`](CONTRIBUTING.md)); versions are recorded in [`CHANGELOG.md`](CHANGELOG.md).

© 2026 HeyDoc AI. Internal. Partner logos and screenshots belong to their owners. See `LICENSE`.
