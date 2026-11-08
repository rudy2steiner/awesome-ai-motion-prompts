# Card Pack Opening

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/card-pack-opening](https://www.aicssanimations.com/directory/Motion-Prompts/card-pack-opening)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second 3D booster pack opening: a foil pack tears open, its cards fan out and flip face up one by one, and a holographic legendary flips last with a burst and a rarity banner.

<inputs>
If I don't give you something, use the default and don't ask.
- Game: Tidewild (fictional), booster "Series 3 · Moonwake", 6 cards per pack.
- Cards in order (name, rarity, type, rules line): Brine Fox, Common, Creature · Fox, "Slips past the first blocker each turn." · Gull Courier, Common, Creature · Bird, "When played, draw a card." · Kelp Warden, Uncommon, Creature · Plant, "Gains 1 defense for each tide you control." · Saltglass Lantern, Rare, Relic, "Reveal the top card of your deck." · Moonwake Shoal, Rare, Tide, "Return two creatures to their owners' hands." · The Tide Sovereign, Legendary, Creature · Whale, "Each turn, the tide rises by one."
- Banner: "LEGENDARY", then "The Tide Sovereign · 1 of 6 in Moonwake"
- Kicker: "OPENING · MOONWAKE BOOSTER"
- Length: 10 seconds.
</inputs>

<direction>
- Look: a tabletop product film of a real pack opening: crinkled foil that catches a softbox, a jagged tear with white foil fibers, crisp printed cards with thickness and rounded corners, a fan that lands with a tap, and one card whose holographic foil throws shifting spectral bands. Tactile and bright, never a flat UI animation.
- Palette: playmat aubergine felt #33183A with a stitched border #4A2652 and stitching #C77A9A; pack print tangerine #FF7A3D to raspberry #E5336B with cream #FFF1DC art and silver foil showing through at its seals; card frames cream #F3E9D6 with ink #22182A and a mid line color #7A6A80; card backs aubergine #3E1E46 with a cream wave-and-compass emblem; rarity gems common slate #8A8FA3, uncommon sea green #4FB89A, rare teal blue #3E8FD6, legendary tangerine gold #FFB23E; burst tangerine, cream and raspberry; banner tangerine #FF8A3D with aubergine type and cream rules. Tangerine and raspberry pop against aubergine; the holo is the only place the full spectrum appears.
- The pack (1 unit = 1 cm): 7.2 × 12.6, pillowed to 0.8 thick at its center and flat at two crimped seals 1.2 tall at top and bottom, the crimps as fine vertical ridges in geometry with a matching normal map; a tear notch at the upper right just under the top seal. Its print, a CanvasTexture drawn after the fonts load: the tangerine-to-raspberry ground, a cream moon over three stylized waves, "TIDEWILD" in Rowdies 700, "SERIES 3 · MOONWAKE" and "6 CARDS". Material: MeshPhysicalMaterial, metalness 0.9 over the print, roughness 0.28, clearcoat 0.5, and a seeded crinkle normal map (long soft creases plus fine wrinkles) so highlights break and slide as it moves.
- The tear: starting at the notch, a jagged line (seeded noise, ±0.15) runs right to left just below the top seal in 0.5 s, the foil parting behind it with a ragged white fiber edge; the strip curls back over 0.3 s (bent along its length by a vertex shader), then flips away off frame to the left with a tumble; eight tiny foil flakes drift down and settle on the felt.
- Cards: 6.3 × 8.8 × 0.03 with 0.3 corner radii (ExtrudeGeometry of a rounded rectangle), a cream edge, and fronts and backs as CanvasTextures (1024 × 1430) drawn after the fonts load: an art window across the top 52% with a thin ink border; the name in Alegreya SC 700 on a name bar; the type line in Alegreya Sans 600 with the rarity gem at its right (a circle, diamond, star or sun in its color); the rules line in Alegreya Sans 500 in a text box; a cost gem top left and a set number bottom right ("03/120" style, all fictional). Art is flat, bold, illustrated shapes in the palette's colors: a fox on dunes at dusk; a gull over waves; kelp stalks with light shafts; a lantern on a rock; a school of fish in a moon's path; and for the legendary, a whale arching over a crescent moon above layered waves. Card fronts are satin (roughness 0.45, clearcoat 0.3), so the softbox lays a soft sheen across them.
- The holo, on the legendary only: a ShaderMaterial over its front. Foil areas (the frame and the art's sky and sea, from a mask drawn with the art) show a diffraction grating: hue from the dot product of the view-reflected light direction and a radial grating direction centered on the moon, mapped through a smooth spectrum, at about 60% over the print, plus a fine seeded micro-texture so the bands have grain; the whale, the type and the text box stay printed and matte. As the card tilts, bands of color sweep across it; flat to the camera it stays mostly cream and silver, never a solid rainbow sheet.
- Fan: five cards leave the stack one at a time and travel 0.45 s each on cubic-bezier(0.3, 0, 0.2, 1) to slots on an arc (rotations −24°, −12°, 0°, +12°, +24° about a pivot 24 units below the fan's center), flipping face up as they go (rotating 180° about their long axis), landing flat on the felt with a 1.5% bounce and a soft contact shadow; as each lands its rarity gem pings: a ring in the gem's color expands from it to 60px and fades. The legendary stays face down above the fan's center, a tangerine light leaking from its edges and pulsing ±15% on a 1.2 s sine.
- The burst: when the legendary finishes its flip, a flat shock ring expands across the felt to 1,400px, 260 sparks (tangerine, cream and raspberry streaks) fly on closed-form ballistic paths with drag and fade over 0.8 s, 24 soft light rays rotate slowly behind the card and fade, and the fan cards nudge 0.3 outward and settle back. Average frame brightness never rises more than 20% within 0.33 s.
- Banner (inline SVG over the canvas): a tangerine ribbon 720 × 96 with notched, folded-back ends and cream rules, unfurling from its center outward over 0.4 s with a slight ripple, "LEGENDARY" in Rowdies 700, 64px, aubergine, tracked 0.08em; beneath it the line in Alegreya Sans 600, 26px, cream. Kicker "OPENING · MOONWAKE BOOSTER" in Alegreya Sans 700, 20px, tracked 0.16em, #C77A9A, at (120, 1000).
- Light: a softbox RectAreaLight #FFFFFF above front (4 × 2, intensity 6, with RectAreaLightUniformsLib); a key DirectionalLight #FFF3E6 at 2.0 from the upper left with soft shadows (PCFSoftShadowMap, 2048); a HemisphereLight #FFE9F2 / #33183A at 0.8; RoomEnvironment through PMREMGenerator at envMapIntensity 0.8 for the foil. ACESFilmic, exposure 1.1. Card text is legible at full contrast and the felt reads as deep aubergine, never black.
- Camera: fov 30. It opens close on the pack standing tilted 12° toward the light (about 780px tall, centered); pulls back and tilts to a 50° three-quarter view as the cards come out, so the fan fills the lower two-thirds; then eases toward the legendary as it rises, ending with it about 620px tall centered at (960, 470), the fan visible on both sides behind it and the banner below at y 830–926. Moves on cubic-bezier(0.45, 0, 0.2, 1); no shake.
- Premium: crinkled metal foil, a tear with fibers, cards with thickness, sheen and crisp print, landings you can feel, and holo bands that move with the angle. Cheap: flat rectangles sliding on a plain background, a pack that vanishes, a rainbow gradient pasted on a card, a white flash.
- Banned: real card games, brands, logos, card frames or artwork, hands, glitter clouds, white or full-frame flashes, lens flares, motion blur, camera shake, a rainbow on any card but the legendary, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the pack slides up into frame and stands tilted toward the light, rocking ±6° so highlights slide along its creases; the kicker rises in.
- 1.2–2.3s: the tear runs from the notch across the top (1.3–1.8 s), the strip curls back and tumbles away to the left (1.8–2.3 s), foil flakes drifting down.
- 2.3–3.0s: the stack rises out of the pack's mouth; the pack slides down out of frame; the camera pulls back and tilts toward the fan view.
- 3.0–5.4s: the five cards fan out one by one, leaving at 3.1, 3.55, 4.0, 4.45 and 4.9 s, flipping face up as they go and landing with a tap and a gem ping (bigger rings for the two rares); the face-down legendary waits above the center, its edges leaking tangerine light.
- 5.4–6.0s: settled: the 6.0 s frame is the full five-card fan face up, every card legible, with the glowing face-down legendary over its center.
- 6.0–7.3s: the legendary rises toward the camera (6.0–6.5 s) and flips over 1.0 s (6.3–7.3 s) with a slight tilt, holo bands sweeping across its face as it turns; the camera eases in.
- 7.3–8.4s: the burst: shock ring, sparks and rays; the fan nudges outward and settles; the banner unfurls under the card (7.5–7.9 s) and its line rises in (8.0 s).
- 8.4–10.0s: hold: the legendary rocks ±4° on a slow 3 s sine so its holo bands shift; the last sparks settle onto the felt.
For other lengths, change the spacing of the fan; keep the tear, the legendary flip at 1.0 s and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- The tear front, strip curl, card travel and flips, ping rings, the legendary's rise, flip and rock, sparks, rays and the camera are closed-form functions of t; the crinkle and crimp normal maps, the card and pack textures and the holo mask are generated once at load (card and pack textures after the fonts load). The banner and kicker are HTML and SVG over the canvas.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the pack reads as crinkled metallic foil with crimped seals and tears along a jagged line with a white fiber edge, every card has thickness, rounded corners and legible text and art, the cards land in the fan without overlapping each other's names, the order is common, common, uncommon, rare, rare, legendary, only the legendary shows holo and its bands move with its tilt, the burst never washes the frame out (log mean luminance from 7.0 to 8.0 s), the felt never reads as black, the banner clears the card, and the 6.0 s and final frames are complete. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
