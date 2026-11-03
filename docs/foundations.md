# Foundations

All values live in `css/tokens.css` (and `tokens/tokens.json`). Never hard-code a value that has a token.

## Colour

### Brand
| Token | Value | Use |
|---|---|---|
| `--navy` | `#012b44` | Headings, body text, dark fills (buttons, chips) |
| `--blue` | `#0873ba` | Primary: key numbers, `<em>` phrases, links |
| `--sky` | `#139bf5` | Lines, nodes, ripples |
| `--pale` | `#8fcdf8` | Soft strokes, halos, inactive tracks |
| `--tint` | `#eef7fd` | Light fills, pressed states, placeholder wells |
| `--line` | `#d6e7f4` | Hairlines, card borders |
| `--muted` | `#5b6b78` | Secondary text |
| `--grey` | `#f4f6f8` | Neutral fills, dividers |
| `--white` | `#ffffff` | Canvas, cards |
| `--cyan` | `#3fd4f6` | Gradient end, glow |
| `--teal` | `#2ce9d5` | Feature gradient end |

### Pastels and inks
Pastels are surfaces for grouping (an agent, a segment, an icon well). **Anything placed on a pastel uses that pastel's ink**, never navy or blue.

| Token | Value | Use |
|---|---|---|
| `--aqua` | `#caf4f3` |  |
| `--sun` | `#fff2cd` |  |
| `--peach` | `#ffdeaf` |  |
| `--mint` | `#cbefd1` |  |
| `--rose` | `#fde0da` |  |
| `--lav` | `#cad4f4` |  |
| `--aqua-ink` | `#0f8a85` |  |
| `--sun-ink` | `#a87508` |  |
| `--peach-ink` | `#bd6512` |  |
| `--mint-ink` | `#1f8a43` |  |
| `--rose-ink` | `#c8394f` |  |
| `--lav-ink` | `#4a5bc4` |  |

### Data and status
Only for status and charts: amber = attention, rose = problem, mint = good.

| Token | Value | Use |
|---|---|---|
| `--d-rose` | `#ea5c72` |  |
| `--d-mint` | `#3be6a2` |  |
| `--d-blue` | `#3fa1f8` |  |
| `--d-violet` | `#7f7be6` |  |
| `--d-amber` | `#feb64f` |  |

### Semantic roles
Prefer these in components so a palette change flows through.

| Token | Value | Use |
|---|---|---|
| `--c-primary` | `var(--blue)` |  |
| `--c-primary-deep` | `var(--navy)` |  |
| `--c-secondary` | `var(--sky)` |  |
| `--c-accent` | `var(--cyan)` |  |
| `--c-success` | `var(--mint-ink)` |  |
| `--c-success-soft` | `var(--mint)` |  |
| `--c-success-data` | `var(--d-mint)` |  |
| `--c-amber` | `var(--d-amber)` |  |
| `--c-amber-ink` | `var(--sun-ink)` |  |
| `--c-amber-soft` | `var(--sun)` |  |
| `--c-red` | `var(--d-rose)` |  |
| `--c-red-ink` | `var(--rose-ink)` |  |
| `--c-red-soft` | `var(--rose)` |  |
| `--c-text` | `var(--navy)` |  |
| `--c-text-2` | `var(--muted)` |  |
| `--c-text-3` | `#9aabb8` |  |

### Backgrounds and gradients
White-only system. `--bg-wash` is reserved for title frames and end cards. `--grad` is the "agent / active" gradient (buttons, active chips, progress); `--orb` is the pulse core.

| Token | Value | Use |
|---|---|---|
| `--bg-light` | `#ffffff` |  |
| `--bg-light-2` | `var(--tint)` |  |
| `--bg-wash` | `linear-gradient(160deg,#fff 0%,#fff 45%,#e9f8fb 70%,#c9f1f4 100%)` |  |

| Token | Value | Use |
|---|---|---|
| `--grad` | `linear-gradient(90deg,#1789f2,#3fd4f6)` |  |
| `--grad-teal` | `linear-gradient(135deg,#72c2ff 0%,#5adcfd 55%,#2ce9d5 100%)` |  |
| `--orb` | `radial-gradient(circle at 28% 18%,#0a84e8 0%,#2ba7f5 55%,#43d0f2 100%)` |  |

### Partner slot
Default is HeyDoc blue; a partner brand replaces it at runtime. See `accent-system.md`.

| Token | Value | Use |
|---|---|---|
| `--partner` | `#0873ba` |  |
| `--partner-deep` | `#065c95` |  |
| `--partner-light` | `#1ea0f5` |  |
| `--partner-pale` | `#a1cae5` |  |
| `--partner-line` | `#cee3f1` |  |
| `--partner-tint` | `#e6f1f8` |  |
| `--partner-dot` | `#ccdee9` |  |
| `--partner-ink` | `#0873ba` |  |
| `--partner-on` | `#ffffff` |  |
| `--partner-rgb` | `8,115,186` |  |
| `--partner-orb` | `radial-gradient(circle at 30% 22%,#065c95 0%,#0873ba 55%,#1ea0f5 100%)` |  |
| `--partner-grad` | `linear-gradient(90deg,#0873ba,#1ea0f5)` |  |

### Contrast rules
- Body text: navy on white (14.7:1) or muted on white (5.5:1). Never sky (3.0:1) or pale for body text.
- Accent text (headline `<em>`, big numbers): `--blue` on white (5.0:1). For partner colours use `--partner-ink`, which is darkened until it reaches at least 3:1 (large text).
- White text only on navy, blue or `--grad`; on a light partner colour use `--partner-on`.

## Typography

**Open Sans** everywhere. **Inter** (`--font-ui`) only inside phone and app mockups, so the UI reads as "an app" and not as our voice. Numbers are tabular.

| Token | Value | Use |
|---|---|---|
| `--font` | `'Open Sans',system-ui,sans-serif` |  |
| `--font-ui` | `'Inter','SF Pro Text',system-ui,sans-serif` |  |

| Token | Value | Use |
|---|---|---|
| `--t-hero` | `84px` | Title frames, end card |
| `--t-title` | `56px` | Slide headline |
| `--t-lead` | `30px` | Subline |
| `--t-body` | `28px` | Body on frames |
| `--t-small` | `22px` | Captions, lower thirds |
| `--t-kicker` | `19px` | Kicker (caps, 3px tracking) |
| `--t-cap` | `20px` | Labels |
| `--t-mega` | `280px` | Full-screen counter |
| `--t-scene` | `60px` | Every on-screen headline in a film (one size) |

| Token | Value | Use |
|---|---|---|
| `--w-regular` | `400` |  |
| `--w-semi` | `600` |  |
| `--w-bold` | `700` |  |
| `--w-black` | `800` |  |

Type styles (`.hd-kicker`, `.hd-headline`, `.hd-headline--xl`, `.hd-subline`, `.hd-statline`, `.hd-caption`, `.hd-lower`) are in `components.md`. Headlines: 700, line-height 1.18, tracking −0.8px, `text-wrap: balance`.

## Space

8-point scale. Frame margins are 120px (`--s-10`); card padding is 24–32px; gaps between cards 16–24px.

| Token | Value | Use |
|---|---|---|
| `--s-1` | `4px` |  |
| `--s-2` | `8px` |  |
| `--s-3` | `12px` |  |
| `--s-4` | `16px` |  |
| `--s-5` | `24px` |  |
| `--s-6` | `32px` |  |
| `--s-7` | `48px` |  |
| `--s-8` | `64px` |  |
| `--s-9` | `96px` |  |
| `--s-10` | `120px` |  |

## Shape and stroke

| Token | Value | Use |
|---|---|---|
| `--r-pill` | `999px` |  |
| `--r-panel` | `28px` |  |
| `--r-card` | `24px` |  |
| `--r-plate` | `22px` |  |
| `--r-inner` | `16px` |  |
| `--r-sm` | `12px` |  |
| `--r-xs` | `8px` |  |

| Token | Value | Use |
|---|---|---|
| `--border` | `2px` | Card and chip borders |
| `--stroke-icon` | `2.2` | All icons |
| `--stroke-line` | `3` | Connector lines |
| `--stroke-route` | `6` | Map routes |

## Shadow

One soft shadow family, always navy-tinted, never grey or black.

| Token | Value | Use |
|---|---|---|
| `--shadow` | `0 10px 32px rgba(1,43,68,.07)` | Flat panels |
| `--shadow-layered` | `0 1px 2px rgba(1,43,68,.05),0 4px 12px rgba(1,43,68,.05),0 10px 32px rgba(1,43,68,.07)` | Default for cards and floating UI |
| `--shadow-float` | `0 2px 6px rgba(1,43,68,.06),0 18px 48px rgba(1,43,68,.14)` | Elements lifted above others (pings, popovers) |
| `--shadow-glow` | `0 12px 30px rgba(23,137,242,.30)` | Active agent, primary button |
| `--shadow-amber` | `0 0 0 3px var(--d-amber),0 0 40px rgba(254,182,79,.45)` | Alert state |

## Motion tokens

| Token | Value | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(.22,1,.36,1)` | Entrances, count-ups |
| `--ease-in` | `cubic-bezier(.55,0,1,.45)` | Exits |
| `--ease-in-out` | `cubic-bezier(.65,0,.35,1)` | Moves, camera, swaps |
| `--ease-spring` | `cubic-bezier(.34,1.56,.64,1)` | Pops, badges, pins |
| `--ease-linear` | `linear` | Progress, loops |

| Token | Value | Use |
|---|---|---|
| `--dur-xs` | `150ms` | Taps, flashes |
| `--dur-s` | `300ms` | Pops, fades |
| `--dur-m` | `600ms` | Standard entrance |
| `--dur-l` | `1200ms` | Count-ups, map reveals |
| `--dur-xl` | `2400ms` | Camera moves, long morphs |
| `--stagger` | `60ms` | Between siblings |

How to use them is in `motion.md`.

## Grid and canvas

- Canvas 1920×1080 (16:9). Safe area: 120px left/right, 84px top, 92px bottom (headline baseline zone).
- Board/slide grid: 12 columns, 32px gutters.
- Phone mockup: `--phone-w` 300–360px in scenes; it scales everything inside.
