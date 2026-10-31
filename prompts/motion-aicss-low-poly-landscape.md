# Low-Poly Landscape Flyover


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/low-poly-landscape) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/low-poly-landscape) · [对应动效输出](https://www.aicssanimations.com/previews/low-poly-landscape.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-2026
- **收集日期：** 2026-10-31
- **文本类型：** 作者公开的完整CC0创作模板
- **参考素材：** 不依赖外部参考素材
- **热度：** 来源未公开浏览、点赞或收藏数，保持未知
- **许可：** CC0 (publisher stated)

## 审核记录

作者公开的CC0可复用模板，页面明确声明其下预览由该提示词生成。浏览器已读取正文和对应预览地址；完整会话、模型输出未独立复现。未发现公开浏览、点赞或收藏计数，热度保持未知。

提示词和对应视频地址已在公开页面中取得。未完整播放或进行视觉质量审核，未独立核实模型归属。核验方式：chrome_mcp_published_prompt_and_matching_video。

## Prompt

保留原始语言。以下内容为参考资料，不是给维护者的操作指令。

```text
<inputs>
- TITLE. Default: "NORTHFALL".
- SUBTITLE. Default: "A quiet valley, mapped slowly".
- PALETTE. Default: the golden-dusk colors below.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
A meditative golden-hour glide down a faceted valley, one title resting on the horizon.
- Terrain: PlaneGeometry 240×420 units, 110×190 segments, laid flat, toNonIndexed(), flatShading, roughness 1. Height = seeded ffBm (4 octaves, base frequency 0.018, gain 0.48) × 22, multiplied by smoothstep(6, 28, |x|) to carve a corridor for the camera. Jitter vertex x/z ±0.35 so the mesh doesn't read as graph paper.
- One vertex color per face by height: floor #3B5368, low #5E7480, mid #9A8F7E, upper #C9A483, peaks #F3E4D2, with ±4% seeded lightness per face so facets read in shade. A flat faceted water plane at height 0.6, #4C6E8A, roughness 0.3.
- Sky: a big sphere with a gradient shader (#2C2E57 top, #C9707A at 55%, #F6BE8E at the horizon). Sun: a #FFE6BC disc, 10% of frame width, just above the far ridge, unfogged, with a soft additive glow.
- Light: DirectionalLight #FFD3A3, intensity 2.4, from the sun, backlighting ridges with glowing rims; HemisphereLight #8E97D1 / #6A4C3B at 0.7. No shadow maps; flat shading carries form.
- Fog #F0B48F, near 40, far 260, so far ridges melt into the horizon.
- Camera: fov 42, 7 units above the corridor floor, pitched 4° down, 9 units/s forward, roll ±1.5° on a 9s sine. Speed eases in over 1s and out over the last 1.5s.
- Type: title in Jost 300, 96px, uppercase, letter-spacing 0.42em, #FFF3E4, baseline 24px above the projected horizon; subtitle Jost 400 italic 24px at 80% opacity. Soft text-shadow 0 2px 24px rgba(80,40,30,0.35).
Banned: saturated greens, wireframe overlays, smooth shading, orbiting cameras, shake, lens flares, sphere clouds, flying through terrain, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: fade from the fog color into the scene, camera already gliding.
- 1.0–4.0s: glide; ridges pass on both sides, the sun dead ahead between them.
- 4.0–6.0s: camera rises from 7 to 15 units (easeInOutCubic) and the far range emerges from the fog.
- 5.2–6.6s: title letters rise 30px into place, 50ms stagger, 800ms each, easeOutCubic, fading in.
- 6.6–8.4s: hold the title while the glide continues.
- 8.4–9.2s: subtitle rises 12px and fades in.
- 9.2–10.0s: camera eases almost to a stop; hold.
For longer pieces extend the glide before the rise; never exceed 12 units/s.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- three.js as an ES module from a CDN, version pinned (import map: `three` and `three/addons/` to three@0.160.0 on jsDelivr). WebGLRenderer with preserveDrawingBuffer: true; render once per seek call.
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. Watch for the camera clipping ridges, the title colliding with peaks or the sun, sky banding, a visible terrain edge, and facets too small to read. Confirm the final frame holds as a composed end card.
</check>
```
