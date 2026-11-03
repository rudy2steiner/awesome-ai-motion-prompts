---
title: "Fantasy Map"
author: "AI CSS Animations (@SaaSgod)"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/fantasy-map-drawing"
license: "CC0"
collected: "2026-11-03"
---

# Fantasy Map

**Author:** AI CSS Animations (@SaaSgod)  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/fantasy-map-drawing](https://www.aicssanimations.com/directory/Motion-Prompts/fantasy-map-drawing)  
**License:** CC0

## Prompt

```
Make a 10-second hand-inked fantasy map that draws itself: coastlines, water lining, mountains, forests, rivers, roads, sea serpents, a compass rose with rhumb lines, lettering and a cartouche.

<inputs>
- Realm: the Saltmarch Isles (fictional).
- Cartouche: "A Chart of the Saltmarch Isles" . "drawn for the Wayfarers' Guild, in the year 412"
- Islands: Saltmarch, Greyholm and the Lantern Isles.
- Features: the Thornfell Mountains, the Whisperwood, Hollowmere, the river Wend, Cape Wistful.
</inputs>

<direction>
- Look: a chart drawn with a dip pen in iron-gall ink on pale oyster rag paper.
- Palette: paper #EFEAE0; iron-gall ink #2B2420; Prussian blue #2C4F7C; verdigris #7FB0A2; ochre #D9BE84; vermilion #C2442E; gold ink #B88A36.
- Pen line: every stroke is a filled shape with width profile 1.2-3.2px, swelling on downstrokes.
- Water lining: four lines echoing every coast at 7, 16, 28 and 44px, extracted as iso-lines of a distance field.
- Symbols: ~18 mountain peaks, ~120 tiny trees, two sea serpents, a two-masted ship, 16-point compass rose.
Banned: parchment textures, real places, fire-breathing dragons, clip-art icons, drop shadows, glow, 3D terrain.
</direction>

<build>
One self-contained index.html, 1920x1080 stage, 60fps. Inline SVG for all line work; paper and washes are canvases rendered once at load under the SVG.
</build>
```
