# Blueprint and Paper Explainer Film

- **Author:** its_Irissss
- **Model:** Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/blueprint-paper-explainer-film](https://www.aicssanimations.com/directory/Motion-Prompts/blueprint-paper-explainer-film)
- **Collected:** 2026-11-08

## Prompt

```
Turn a topic into a **film**: roughly 30 seconds at 24 fps, every event on a **beat grid** (bpm → beats → frames), every stroke and every audio sample computed in plain browser JavaScript. The deliverable is `dist/<slug>.html` (a self-contained player) plus `exports/<slug>.mp4` and its phone and preview transcodes.

[…]

| | **drawn** (default) | **photo-doodle** | **retro** |
|---|---|---|---|
| What is on screen | every pixel computed: hand-inked **paper plate** shots cut against navy **blueprint plate** shots | a background-removed **photograph** per shot, standing on tinted paper, with animated doodles drawn over and around it | pixel art on the NES palette, shown sharp or on an optional old TV |
| Frame | vertical 1080×1920 | square 1080×1080 | 1920×1080 at 60 fps, drawn at 320×180 |
| Subject | explaining something real: a life cycle, a process, how a thing works | a story staged on ordinary objects, where each photo becomes a set (a clock becomes a bed, a pine cone becomes a mountain) | a story told as a side-scrolling pixel scene |
| Assets | none at all | photographs you source, licence and cut out yourself | none at all |
| Extra steps | — | 1b source the photographs, 3b write the cast | 3c draw the cast sheet |
| Extra files | — | `src/photos.js` (generated), `src/props.js`, `src/cast.js`, `assets/` | `src/pixel.js`, `src/chip.js`, `src/crt.js` (from `retro/`), `src/sprites.js` |
```
