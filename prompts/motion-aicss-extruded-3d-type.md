# Extruded 3D Type

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/extruded-3d-type](https://www.aicssanimations.com/directory/Motion-Prompts/extruded-3d-type)
- **Collected:** 2026-11-08

## Prompt

```
<inputs>
If I don't give you something, use the default and don't ask.
- Word: default "FORMA" (3–7 letters read best)
- Tagline: default "Built to hold its shape."
- Brand line: default "FORMA WORKS · STUDIO OBJECTS"
- Colors: default face #F3EFE6, sides #E4472B, studio #CFC8BD
- Length: default 10 seconds
</inputs>

<direction>
Letters as products: solid, chunky objects on a seamless studio sweep, lit like a still-life shoot.

Setup: three.js pinned to one version (e.g. three@0.160.0) through an import map from a CDN, with FontLoader, TextGeometry and RoomEnvironment from that version's addons and helvetiker_bold.typeface.json from its examples/fonts folder.

Geometry: one mesh per letter. Size 1, extrusion 0.35–0.45 (named height or depth, by version), curveSegments 12, bevel thickness 0.035, bevel size 0.025, 5 bevel segments. Center each letter on its own origin; space by measured bounding boxes plus 0.06.

Materials: two-tone through the geometry's material groups: faces MeshStandardMaterial in the face color (roughness 0.45), sides in the side color (roughness 0.35), metalness 0. A low-intensity RoomEnvironment via PMREMGenerator for soft bevel highlights.

Set and light: a large floor with ShadowMaterial (opacity 0.18); background and fog in the studio color so the floor melts into the sweep. Warm key from upper left with soft shadows (PCFSoftShadowMap), a low cool hemisphere fill, a cool rim spotlight from behind right. ACES filmic tone mapping, sRGB output.

Motion: letters rotate into place; they don't fly. Each starts edge-on (rotation.y ±90°, alternating), lifted 0.3 and set back 0.6, and swings to rest over 0.9–1.1 s with easeOutBack (overshoot at most 4°), staggered 0.12 s. One slow camera arc, yaw 28° → 8° (easeInOutSine), ending low, looking up 6°, so the word feels monumental. The tagline holds at least 1.5 s.

Authentic: visible side color, soft contact shadows, bevel highlights, weighty motion. Cheap: a black void with no floor.

Banned: chrome or rainbow materials, lens flares, bloom, MeshBasicMaterial, continuous spinning, camera shake, anything flashing more than 3 times per second.
</direction>

<structure>
Default 10 s:
- 0.0–1.0: empty sweep; key light ramps 30% → 100% (easeOutSine).
- 1.0–3.6: letters rotate in left to right, each landing its shadow.
- 3.6–6.0: camera arcs toward front-on; the rim highlight slides across the bevels.
- 6.0–7.4: camera settles low, word about 60% of frame width, a sliver of side showing.
- 7.4–8.4: tagline and brand line rise 16 px into place below: HTML overlay, Space Grotesk 500, tracking 0.08em, #2A2620.
- 8.4–10.0: hold; nothing moves from 9.0.

Other lengths: scale stagger and arc; keep a final hold of at least 1.2 s.
</structure>

<build>
- One self-contained index.html, no libraries (three.js from a CDN only when a style truly needs 3D); a 1920×1080 (16:9) stage scaled to fit the window; designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames. Any randomness comes from a seeded PRNG keyed to the frame.
- No ?render in the URL: drive seek from requestAnimationFrame so it plays in a browser. With ?render: don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Use preserveDrawingBuffer: true; seek sets every transform and light from t, then renders once. Load the typeface JSON before assigning seek.
</build>

<check>
Before showing me, step through one frame per second and look at each. Fix overlaps, clipped or cramped text and anything off-style. Check every letter casts a shadow and none clips a neighbor mid-swing. Confirm the final frame holds.
</check>
```
