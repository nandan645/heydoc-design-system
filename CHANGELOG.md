# Changelog

All notable changes to the HeyDoc Design System. Format: [Keep a Changelog](https://keepachangelog.com), versions: [SemVer](https://semver.org).

## [Unreleased]

## [1.1.1] · 2026-11-05
### Added
- `examples/futurek-member-journey-film.html`: futureK × HeyDoc AI client film (2:14), built on the 1.1.0 bundle.

## [1.1.0] · 2026-11-03
### Added
- `dist/heydoc.bundle.css` (incl. `.hd-brandmark` HeyDoc logo) and `dist/heydoc.bundle.js`: single-file bundles for artifacts; `scripts/bundle.py` builds them, `build.sh` runs it.
- Claude skill: `skill/heydoc-design-system/SKILL.md`.

## [1.0.2] · 2026-11-03
### Changed
- Numbers in examples are illustrative by design (replaced per use case); docs updated.
- No Figma library: the repository is the source of truth.
- README: how to publish to GitHub.

## [1.0.1] · 2026-11-03
### Removed
- White HeyDoc logo (`assets/logos/heydoc_white.webp`): the system has no dark backgrounds.
### Changed
- Docs: HeyDoc logo is raster-only (no SVG master); size guidance added.

## [1.0.0] · 2026-11-03
### Added
- Tokens (`css/tokens.css`, `tokens/tokens.json`): brand, pastel + ink, data, semantic, background, gradient, type (incl. `--font-ui`, `--t-scene`), space, radius, stroke, shadow, motion, partner slot.
- Components (`css/components.css`): atoms, type styles, surfaces, phone/app UI, pulse, crowd, counters, agent cards, camera tiles, route map, segments, logo ring, end card, journey (kept vs lost, journey stack, today vs with HeyDoc, channels).
- Scene kit (`css/scene.css`, `js/motion.js`): deterministic `render(t)` player, easing and springs, recipes, shape-morph shell, hue-path colour blend.
- Partner accent system (`js/brand.js`, `scripts/brand.py`): one brand hex → full shade set with contrast-safe ink.
- 38 icons (SVG, sprite, JSON); logos; India/Maharashtra maps; globe land points.
- Element board, explainer film (reference), starter frame, starter scene.
- Docs: principles, foundations, components, motion, accent system, content, assets, film, open items; `AGENTS.md` for AI assistants.
### Removed
- Dark-mode variants (system is white-only).
