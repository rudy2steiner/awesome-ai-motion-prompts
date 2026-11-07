# Bookshelf

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/bookshelf-reveal) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/bookshelf-reveal)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second 3D film of a bookshelf: lettered books slide out along an oak shelf, then one is drawn out, turns to face us and opens on its title page.

<inputs>
If I don't give you something, use the default and don't ask.
- Publisher: Larkholm Press (fictional).
- Kicker: "LARKHOLM PRESS · THE AUTUMN LIST"
- Spines, left to right (18 books, all fictional): The Salt Road, I. Marchetti · Small Hours, Ione Varga · A Field Guide to Fog, Tomas Brecken · Copper and Rain, Lise Annand · The Ninth Orchard, H. W. Pallister · Letters to a Lighthouse, Mirela Szent · Winter Kitchens, June Albery · The Glass Allotment, R. Calloway · A Lamp for Wintering, Edda Lowrie · Notes on Moss, Ada Penhale · The Quiet Engine, Felix Dunmore · Harbour Weather, Agnes Toll · The Kestrel Year, Owen Tarrant · Paper Gardens, Sunniva Holt · Supper at Eleven, C. M. Ferro · Under the Walnut, Petra Vales · A Short History of Rain, Bram Okoro · Night Ferry, Isolde Marr.
- Hero book: the ninth, A Lamp for Wintering by Edda Lowrie.
- Title page: "A LAMP FOR WINTERING" · "a novel" · "EDDA LOWRIE" · "LARKHOLM PRESS" · "1934"
- Length: 10 seconds.
</inputs>

<direction>
- Look: a warm, quiet library shot: cloth-bound hardbacks on an oak shelf against a deep green wall, lit as if by a reading lamp off frame, filmed with a slow, steady camera.
- Palette: wall #2E4A3E with a soft #3F6152 pool of lamplight behind the shelf (a radial gradient painted into the wall's texture); oak #A8784C with grain #8A5E3A; book cloths oxblood #7A2A2A, navy #24365E, ochre #C8902E, sage #8DA584, plum #5A3550, teal #2F6E6E, cream #E8DDC4, rust #B5532E, charcoal #3A3A3C, mustard #D4A93A; gilt #E2C27A; cream ink #F1E6CC; dark ink #2A2522; paper #F3EAD8 with page edges #E9DDC6; one red #9E2F2A on the title page.
- The shelf: one long oak shelf in a bay with side uprights, its front lip rounded, a back panel in the wall green, and the shelf above cropped by the top of the frame (its underside and a few book bottoms) for depth.
- Books, each built like a real hardback (1 unit = 10 cm): heights 2.0–2.6, depths 1.3–1.5, thicknesses 0.22–0.55, seeded; boards 0.03 thick that overhang the text block by 0.03 at head, tail and fore-edge (the squares); a rounded spine slightly proud of the boards; a slight groove where each board hinges; striped headbands at head and tail; a text block of cream pages whose edges show fine page lines. Cloth is a fine woven CanvasTexture used for color variation and bump (roughness 0.85). A few books lean or sit unevenly, and one gap holds a small brass bookend.
- Spines: CanvasTextures drawn after the fonts load (about 2,048px tall), in real book-typography layouts: titles running down the spine (readable with your head tipped right) or stacked across it, the author, and a small lark device at the foot; two spines carry gilt bands, one a dark label panel, one a printed paper jacket with a small pattern. Faces vary by book: Libre Caslon Display, Bodoni Moda, Josefin Sans, Oswald and Lora, each sized to fill its spine's width with a margin, in gilt, cream or dark ink to suit the cloth.
- The hero book: navy cloth, 2.4 × 1.6 and 0.42 thick; the front cover carries a gilt lamp emblem and the title (a gilt CanvasTexture with a slight emboss through a bump map); marbled endpapers (a procedural combed marble in navy, ochre and cream); a white flyleaf; a tissue guard; then the title page.
- Light, warm and clear: a key DirectionalLight #FFE6C4 at 2.2 from the upper left (elevation 40°) with soft shadows (PCFSoftShadowMap, 2048) so books shade their neighbors softly; a HemisphereLight #FFF2E0 / #24382F at 0.7; RoomEnvironment through PMREMGenerator at envMapIntensity 0.25 so the gilt catches the light. ACESFilmic, exposure 1.1. Every spine is readable from the first frame, and the shelf's ends fall off gently into the green, never to black.
- The wave: books slide out by being pulled forward 0.45 units over 0.35 s on cubic-bezier(0.3, 0, 0.2, 1), held 0.2 s and pushed back over 0.3 s, every second book left to right, 0.22 s apart, while the camera dollies along the shelf at 0.55 units/s (fov 32, 6° above the shelf, 5.5 units back).
- The reveal: the hero slides fully out over 0.9 s, rotates 90° to show its front cover and rises to center at (960, 520) on cubic-bezier(0.45, 0, 0.2, 1), while the shelf behind dims to about 55% as its light lowers and a soft fill keeps the book bright. Then it opens: the front board hinges at its groove over 0.9 s (rotating 165°, its marbled endpaper showing), the flyleaf follows 0.1 s behind, then the tissue, and the title page settles flat. Each page is a subdivided plane bent along a smooth curve that relaxes as it lands, and the right-hand side shows the text block's page edges.
- Title page, set like a real one (a 2,048px-wide CanvasTexture): "A LAMP FOR / WINTERING" in Libre Caslon Display 400, letterspaced 0.08em; a short rule; "a novel" in Libre Caslon Text italic, in red; "EDDA LOWRIE" in Libre Caslon Text 400, tracked 0.2em; at the foot, the lamp emblem, "LARKHOLM PRESS" and "1934" in small caps. Its lines ink in top to bottom, each from 0 to full over 0.3 s, 0.15 s apart.
- Overlay type (HTML): only the kicker, in Josefin Sans 600, 20px, tracked 0.2em, gilt, top-left at (120, 96), fading in over 0.6 s. Nothing covers the book.
- Premium: books with boards, squares, headbands and readable spines, warm light, a cover that hinges from its groove and pages that bend. Cheap: colored boxes with stretched text images, a book that opens like a flat lid.
Banned: 3D text geometry, flat boxes without boards or page edges, mirrored or stretched lettering, lorem ipsum, real book titles or publishers, depth-of-field blur, dust particles, bloom, hands, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: the camera glides along the shelf from the left, spines lit and readable; the kicker fades in.
- 1.0–3.6s: the wave: every second book slides out and back, 0.22 s apart, as the dolly travels.
- 3.6–4.6s: the dolly eases to a stop in front of the hero, which slides fully out.
- 4.6–5.6s: it turns to show its cover and rises to center; the shelf dims behind it.
- 5.6–6.4s: it holds closed: the 6.0 s frame is the navy cover with its gilt title, centered and still, the shelf soft behind.
- 6.4–7.6s: the cover hinges open; the endpaper, flyleaf and tissue turn.
- 7.6–8.6s: the title page inks in, line by line.
- 8.6–10.0s: hold on the open book.
For other lengths, stretch the wave; keep the reveal and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Every book's transform, the cover hinge and each page's bend are closed-form functions of t; spine, cover, endpaper and title-page CanvasTextures are drawn once after the fonts load.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every spine reads cleanly (no stretched or mirrored lettering), books show boards, squares, headbands and page edges, the cover hinges at its groove without cutting into the text block, pages never pass through each other, the title page is fully legible at the end, and the 6.0 s frame is a still, centered closed book. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
