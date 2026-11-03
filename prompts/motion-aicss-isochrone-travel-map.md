---
title: "Isochrone Map"
author: "AI CSS Animations (@SaaSgod)"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/isochrone-travel-map"
license: "CC0"
collected: "2026-11-03"
---

# Isochrone Map

**Author:** AI CSS Animations (@SaaSgod)  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/isochrone-travel-map](https://www.aicssanimations.com/directory/Motion-Prompts/isochrone-travel-map)  
**License:** CC0

## Prompt

```
Make a 10-second animated isochrone map: travel-time bands spread from one square across a fictional city, racing out along tram lines, squeezing through bridges and opening an island around a far rail station.

<inputs>
- City: Esterholt (fictional). Origin: Tolhurst Square.
- Bands: every 5 minutes up to 30. Residents: 0-5 min 18,000; 5-10 31,000; 10-15 42,000; 15-20 47,000; 20-25 41,000; 25-30 35,000 (214,000 in all).
</inputs>

<direction>
- Palette: land #ECEAE4, streets #FFFFFF, river #B8D1DB, rail #6F6B66. Accent coral #EE5A3C for tram lines.
- Bands: dark to light teal: 0-5 #0D5C5D through to 25-30 #CDE7D9.
- City generated from seeded PRNG: river, three bridges, old town grid rotated 8deg, newer grid -4deg.
- Travel time: Dijkstra over 4px grid; bands follow real routes, not circles.
- Drawing: basemap on 2D canvas; bands on WebGL2 canvas with mix-blend-mode: multiply; front line by marching squares.
Banned: circles or buffer rings, rainbow ramps, glow, 3D tilt, teardrop pins, map libraries.
</direction>

<build>
One self-contained index.html, 1920x1080 stage, 60fps. Canvas: basemap and overlay on 2D canvases, bands on one WebGL2 canvas.
</build>
```
