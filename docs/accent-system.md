# Accent system: HeyDoc + Partner

HeyDoc works *inside* other companies' journeys, so frames often show a partner's product. The rule: **the partner borrows our accent slot; everything else stays HeyDoc.**

## Two states

| State | Accent | When |
|---|---|---|
| **HeyDoc** | Fixed blues: `--blue`, `--sky`, `--pale`, `--tint`, `--orb`, `--grad` | Default. Problem, platform, scale, vision, end card |
| **Partner** | `--partner` + derived shades | While a partner's product is the subject (their app on the phone, their operations) |

What switches to the partner colour: the orb, ripples, highlight rings, connector lines, active chips and agent glow, progress fills, the lit dots in a crowd, and the `<em>` phrase in headlines (using `--partner-ink`).
What never switches: text colour, type, layout, radius, shadow, motion, status colours (amber/rose/mint), the HeyDoc logo.

## One hex in, every shade out

Give the system one brand colour; it derives the rest. Same rules in `js/brand.js` (browser) and `scripts/brand.py` (CLI).

| Token | Rule | Use |
|---|---|---|
| `--partner` (base) | the brand hex | Fills: orb core, buttons, lit dots |
| `-deep` | 20% toward black | Orb shadow side, pressed |
| `-light` | same hue/saturation, +16 lightness (max 82%) | Gradient end, orb highlight |
| `-pale` | 62% toward white | Halos, soft strokes |
| `-line` | 80% toward white | Borders |
| `-tint` | 90% toward white | Light fills, placeholder chips |
| `-dot` | 86% toward #eceff1 | Unlit dots in a crowd |
| `-ink` | darkened in 5% steps until ≥ 3:1 on white | **Text** in the brand colour |
| `-on` | white if the base passes 3:1, else navy | Text placed on a base fill |
| `-orb`, `-grad` | radial deep → base → light; linear base → light | Ready-made backgrounds |

```bash
python3 scripts/brand.py "#FFCD05"
# base #ffcd05 (1.50:1) … ink #b39004 (3.04:1) · on #012b44
```

```js
HDBrand.apply('#246B45');                 // whole page
HDBrand.apply('#FFCD05', sectionEl);      // just one section
```

## Hand-offs

Switch accents over ~0.6s at a story beat, on the element that carries the story (the orb shrinking into the next section, the crowd converging). Blend with `HD.hueMix(from, to, p)`: it travels round the hue wheel, so green → yellow goes through a fresh lime instead of a muddy olive.

## Worked examples (from the film)

| Partner | Brand hex | Ink (text) | Where |
|---|---|---|---|
| Habuild | `#246B45` | `#246B45` (passes as-is) | Act 2, 16–34s |
| Pathkind | `#FFCD05` | `#B39004` (darkened for contrast) | Act 3, 34–54s |

The film keeps these as slots `partner1` and `partner2` (`source/gen/brand.py`, `PARTNERS`), so any company can be swapped in by changing one hex, or live in the film's Edit mode.
