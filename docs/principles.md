# Principles

Seven rules. If a design follows these, it reads as HeyDoc even before the logo appears.

## 1. White canvas, always
Every frame, slide and scene sits on white (`--bg-light`) or the soft title wash (`--bg-wash`). **No dark backgrounds anywhere**, no fades to black: transitions wipe or fade through white.
*Exception:* a phone lock screen may show a dark wallpaper, because that is the phone's content, not our canvas.

## 2. One soft shadow, generous radius
Surfaces are white cards with `--shadow-layered` (or `--shadow` for flat panels). Radii are large and consistent: panels 28, cards 24, inner 16, chips are pills. Never mix sharp and round corners in one view.

## 3. Blue carries meaning; colour is never decoration
Navy (`--navy`) for text. HeyDoc blue (`--blue`) marks the one phrase or number that matters (`<em>` in headlines). Sky and cyan are for lines, nodes and glow. Pastels group things (an agent, a segment), and each pastel always pairs with its own ink. Status colours (amber, red, mint) only ever mean status.

## 4. Partners borrow the accent, never the system
When a partner's product is on screen, its brand colour takes over the accent through the partner slot (`docs/accent-system.md`). Type, layout, radius, shadow and motion stay HeyDoc. When the partner section ends, the accent hands back to HeyDoc blue.

## 5. No people, no photos, no real data
- No people, illustrations of people, stock photos or real patient or hospital footage. Use mockups, cards, maps, dots and counters.
- All data is fake and clearly fake. Anything that stands in for a real number uses the placeholder style `[N]` (`.hd-ph`) until it's confirmed (`docs/content.md`).
- Partner screenshots and government marks need sign-off before anything is published (`docs/assets.md`).

## 6. One shape, many states
Motion is continuous: the pulse becomes a phone, the phone widens into a panel, the panel folds into a tile, tiles shrink to dots on a map. Prefer **morphing an element you already have** over cutting to a new one. Content blurs in as the shape settles and blurs out before it changes. See `docs/motion.md`.

## 7. Clear before clever
One idea per frame. One headline size across a whole film (`--t-scene`, 60px). Headlines are short, plain and specific. If a viewer needs to read twice, cut words.
