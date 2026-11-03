---
title: "Three Phone App Promo"
author: "AI CSS Animations (@SaaSgod)"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/mobile-app-three-phones"
license: "CC0"
collected: "2026-11-03"
---

# Three Phone App Promo

**Author:** AI CSS Animations (@SaaSgod)  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/mobile-app-three-phones](https://www.aicssanimations.com/directory/Motion-Prompts/mobile-app-three-phones)  
**License:** CC0

## Prompt

```
Make a 10-second mobile app promo with three original phones staggered in 3D on a soft blush backdrop: each phone runs a different live screen of a plant-care app, callouts with leader lines name each feature, and the camera drifts slowly around them.

<inputs>
- App: Mossback (fictional), a plant-care app. User: Sam.
- Left phone: "Today" care list that scrolls
- Center phone: plant detail with "Mark as watered" button
- Right phone: scanner that identifies a leaf
- Headline: "Keep every plant alive." Sign-off: Mossback wordmark.
</inputs>

<direction>
- three.js with ACESFilmic tone mapping, perspective 30deg vertical FOV.
- Phone bodies: rounded box 1.5x3.2x0.16 units, 0.22 corner radius, 0.04 edge bevel.
- MeshPhysicalMaterial with roughness 0.45 and clearcoat 0.3.
- Screens: 2D canvas 780x1688, redrawn every frame and uploaded as texture.
- Camera drifts from azimuth -9deg to +6deg over 8.6s.
Banned: real company names, real phone models' notches, spinning devices, particles, lens flares.
</direction>

<build>
One self-contained index.html, 1920x1080 stage, 60fps. three.js pinned through importmap from jsDelivr. window.seek(t) computes every visual from t alone.
</build>
```
