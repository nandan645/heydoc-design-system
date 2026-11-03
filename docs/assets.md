# Assets

| Folder | Contents | Status |
|---|---|---|
| `assets/logos/` | HeyDoc (colour, white) and partner logos as WebP | ⚠️ Raster extracts. **Vector (SVG) masters needed**, see `open-items.md` |
| `assets/maps/` | India and Maharashtra outlines (SVG + raw path), land points for the dot globe (`[lat×10, lon×10, region]`) | ⚠️ Boundaries are approximate. Check against the official Survey of India map before any public use |
| `assets/product-screens/` | HeyDoc's own product screenshots (company brain) | Client branding painted out; user name replaced with "Admin" |
| `assets/partner-screens/` | Habuild app screens, Pathkind "Tests" screen | 🔒 **Restricted**: supplied by partners for the explainer film only |
| `icons/` | 38 HeyDoc stroke icons | Free to use in any HeyDoc work |

Broader brand library (deck illustrations, hero images, flags, partner logos): **github.com/nandan645/heydoc-assets**.

## Logos

| File | Use | Rules |
|---|---|---|
| `heydoc.webp` | On white | Minimum height 32px on screen; clear space = height of the "hey" |
| `heydoc_white.webp` | On navy / photos only | The system is white-only, so this is rarely needed |
| Partner logos | Logo ring, partner sections | Always on a white `.hd-logotile`, height-matched; never recolour, stretch or crop |

**Government of Maharashtra seal and NHA mark** need **written approval** before any public release.

## Partner screenshots

- Use only inside phone/window mockups, at the size they were cropped for (660×1428 for phones).
- Text inside screenshots that we overlay (chat messages, the upsell card) is HTML, so it can be edited and translated.
- Don't use them outside HeyDoc–partner material without the partner's OK.

## Adding an asset

1. Prefer SVG; otherwise PNG/WebP at 2× the largest use.
2. Name it `kebab-case`, put it in the right folder, add a row here with its status.
3. Strip third-party branding, real names and real data from screenshots before committing.
