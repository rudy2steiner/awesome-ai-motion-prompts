---
title: "Volcano Explainer Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/volcano-cross-section"
license: "CC0"
collected: "2026-11-03"
---

# Volcano Explainer Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/volcano-cross-section](https://www.aicssanimations.com/directory/Motion-Prompts/volcano-cross-section)  
**License:** CC0

## Prompt

```
Make a 10-second geology explainer: a stratovolcano in cutaway builds layer by layer, magma rises from its chamber, and the eruption column climbs, with every part labeled.

<inputs>
If I don't give you something, use the default and don't ask.
- Series: "Fieldnotes on the Earth · 04", from Brindle Learning (fictional).
- Title: "Inside a stratovolcano"
- Captions, in order: "Each eruption adds a layer of lava and ash." · "Magma collects in a chamber about 6 km down." · "As it rises, falling pressure lets gas bubbles grow." · "The gas tears the magma apart and drives the column up."
- Labels: Layers of lava and ash · Magma chamber · Dike · Sill · Conduit · Crater · Eruption column · Ash cloud · Side vent · Lava flow.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a geology textbook plate brought to life: a block diagram whose front face is cut through the volcano's axis, flat fills carrying the patterns of a geological section, and thin ink linework. It is not to scale, and it says so.
- Palette: paper #F1ECE2; ink #2B2622; older rock #B9AE9C with a granite pattern of small crosses; bedded rock #CFC3AE with horizontal dashes; lava layers #7A5A4A with sparse vesicle dots; ash layers #CDBB95 stippled with dots; magma #E8532B to a hot core #FFB13B, crusted #9E3A22 at its edges (the only gradient); gas bubbles outlined in #FFE2A8; the block's top surface #C9C29A; the column lit #C7C0B6, mid #A39C93, shade #6F6862; lava flow #E8532B under a crust #3A2A24; label dots and kicker #C2412A; secondary text #6E655C.
- Layout: the block's front face spans x 340–1460, y 520–900; its top face recedes 80px right and 50px up, and its right side face is a darker strip, so it reads as a solid block. The cone rises from the front face's top edge at y 520 to the crater rim at y 300, about 900px wide at its base, on the axis x = 900. The magma chamber is an ellipse 380 × 110px centered at (900, 820). Labels sit in columns at x 90–310 and x 1570–1830; captions at the bottom on baseline y 1000; the key at the bottom right.
- Section, true to how a stratovolcano is built: 16 alternating layers (8 lava, 8 ash) that dip outward parallel to the slopes, each a little higher than the last, all cut by the central conduit (34px wide) running from the chamber to the crater floor. A dike branches diagonally off the conduit to a side vent with a small parasitic cone on the right flank; a second dike rises on the left and stops inside the layers; a sill spreads horizontally through the bedded rock on the left at y 700. Behind the cut, the back half of the cone shows a sliver of its outer slope with fine downhill hachures.
- Magma: as it climbs the conduit, bubbles rise with it and grow (radius 2px at the chamber to 14px near the top, as the pressure falls); just below the crater they crowd into foam and break into angular fragments that feed the column.
- Eruption column, in three parts: a dense, narrow gas-thrust jet at the vent; a convective column of cauliflower lobes that widen as they rise (each lobe born at the vent, slowing from 600 to 80px/s, its radius 20 + 0.42 × its height); and an umbrella cloud that spreads at y 100–220 and drifts right with the wind to x 1540, trailing fine streaks of falling ash on its right side. Each lobe takes three flat tones lit from the upper left. Draw every lobe once with a 3px ink stroke, then every lobe filled on top, so only the column's outer silhouette keeps an outline.
- Lava flow: from the side vent down the right flank, its glowing front advancing at 30px/s under a darkening crust, coming to rest by 8.0 s.
- Type: kicker in IBM Plex Mono 500, 20px, tracked 0.14em, #C2412A, at (120, 96); title IBM Plex Serif 600, 56px, ink, beneath; captions IBM Plex Sans 500, 28px, ink, one line each, crossfading with a 10px rise; labels IBM Plex Sans 500, 22px, ink, wrapping to two lines within 200px, each on a 1px ink leader ending in a 6px #C2412A dot on the exact part it names; the key in IBM Plex Sans 500, 20px: four 22px pattern swatches (Lava, Ash, Magma, Older rock) and "Not to scale".
- Motion: calm and explanatory. Lava layers drape from the crater down both flanks over 0.11 s each; ash layers settle evenly from above (a 6px drop as they fade in). Magma fills on cubic-bezier(0.45, 0, 0.2, 1). Leaders draw over 0.25 s, then their text fades in over 0.3 s, rising 6px. Nothing bounces, and no more than four labels arrive in any one second.
- Premium: real anatomy (layers that follow the slopes, dikes that cut across them, a sill between beds, bubbles that grow on the way up, a column with a jet, billows and an umbrella), leaders that land on exact parts, textbook patterns. Cheap: a brown triangle with a red stripe and orange circles flying out of the top.
Banned: faces, smoke rings, lava bombs drawn as circles, volcanic lightning, drop shadows, gradients outside the magma, dark backgrounds, labels without leaders, labels overlapping each other or the column, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: paper; the block's outline and its bedded and older rock draw on; the kicker and title rise in.
- 0.8–2.6s: the cone builds: the 16 layers drape on bottom-up, lava and ash alternating, 0.11 s apart, the conduit left open; caption 1; the label "Layers of lava and ash".
- 2.6–3.8s: the chamber fills with glowing magma, then the dikes and the sill fill from it; caption 2; labels "Magma chamber", "Dike" and "Sill".
- 3.8–4.8s: magma rises up the conduit, bubbles swelling as they climb; caption 3; the label "Conduit".
- 4.8–5.8s: the foam breaks apart at the crater and the column shoots up to full height, the umbrella starting to spread; caption 4.
- 5.8–7.6s: the umbrella spreads right with ash falling from it; the side vent opens and the lava flow creeps down the right flank; labels "Crater", "Eruption column", "Ash cloud", "Side vent" and "Lava flow" arrive at 6.1, 6.4, 6.7, 7.0 and 7.3 s.
- 7.6–8.6s: the key fades in; the lava flow comes to rest.
- 8.6–10.0s: hold: only the column billows and ash keeps falling.
For other lengths, stretch each beat proportionally; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: inline SVG, setting attributes, paths and transforms from seek, with <pattern> fills for the rock patterns; no other libraries (no three.js: this style is flat).
- Column lobes, bubbles and ash streaks are closed-form functions of t from their seeded birth times.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every layer follows the slope and is cut by the conduit, bubbles grow as they rise, every leader dot sits on the part it names, no label overlaps another label, the column or a caption, the umbrella stays left of x 1540, and each caption fits on one line. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
