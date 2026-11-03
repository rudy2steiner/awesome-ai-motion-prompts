---
title: "Dot Density Map"
author: "AI CSS Animations (@SaaSgod)"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/dot-density-map"
license: "CC0"
collected: "2026-11-03"
---

# Dot Density Map

**Author:** AI CSS Animations (@SaaSgod)  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/dot-density-map](https://www.aicssanimations.com/directory/Motion-Prompts/dot-density-map)  
**License:** CC0

## Prompt

```
Make a 10-second dot density map: 38,400 dots, one per person, spread evenly over a fictional island nation, then flow to where people really live, clustering into towns and a bright capital.

<inputs>
- Country: Skerra, an island nation (fictional).
- Places: Holmvik (capital) 14,200; Saltby 6,300; Skarn 3,900; villages and farms 14,000.
</inputs>

<direction>
- Palette, a night atlas: sea #0A0F1C, land #131B2B, coastline #3B4A66. Dots #FFE8C4 with additive blending.
- Island: hand-authored outline roughened by seeded midpoint displacement.
- Dots: 1.4px radius, 55% opacity with additive blending. Drawn in one WebGL points pass.
- Flow: each dot moves from even start to home on curved path, easeInOutCubic over 1.4s.
Banned: choropleth fills, heat-map gradients, glow or bloom halos, dots larger than 2px, real coastlines.
</direction>

<build>
One self-contained index.html, 1920x1080 stage, 60fps. Canvas: map and type on 2D canvases, dots in one WebGL canvas pass.
</build>
```
