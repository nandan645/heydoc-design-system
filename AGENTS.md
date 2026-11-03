# Briefing for AI assistants

You are working in the **HeyDoc Design System**. Read this file fully before making anything.

## Read first (in order)
1. `docs/principles.md` (the 7 rules)
2. `docs/foundations.md` (tokens)
3. `docs/components.md` (what exists, class names)
4. `docs/motion.md` (only if animating)
5. `docs/accent-system.md` (only if a partner brand is on screen)
6. `docs/content.md` (before writing any on-screen text)

Don't read `examples/*.html` or `source/` whole: they are large generated files (1–2 MB with embedded images). Search them for the component you need.

## Hard rules
- **White canvas only.** No dark backgrounds, no fades to black.
- **Tokens only.** Use `var(--…)` from `css/tokens.css`; never invent hex codes, sizes, radii, shadows or easings.
- **Reuse components** (`.hd-*`) before creating new ones. New components follow BEM (`.hd-block__part--variant`) and get documented in `docs/components.md`.
- **No people, no stock photos, no real patient/hospital data.** Data is fake; numbers are illustrative and replaced per use case (`<span class="hd-ph">[N]</span>` when the gap should be obvious).
- **Fonts:** Open Sans everywhere; Inter only inside phone/app mockups.
- **One headline size per film** (`--t-scene`); colour one phrase with `<em>`.
- **Partner brands** change only the accent slot (`HDBrand.apply(hex)`); text uses `--partner-ink`.
- **Animation is a pure function of time** (`render(t)` + `HD.player`). No CSS transitions or timers in scenes.
- **URL is heydoc.co.in.** Product name "HeyDoc AI", tagline "The Agentic Care OS".
- Government marks and partner screenshots are restricted (`docs/assets.md`).

## Starting points
- Static frame → copy `examples/starter-frame.html`
- Animated scene → copy `examples/starter-scene.html`
- Partner colour → `python3 scripts/brand.py "#HEX"`

## Before you finish
- `python3 scripts/check_tokens.py` passes.
- Open the result in a browser and capture key frames (`?t=` + `window.__render(t)`).
- Tell the user which numbers are illustrative.
