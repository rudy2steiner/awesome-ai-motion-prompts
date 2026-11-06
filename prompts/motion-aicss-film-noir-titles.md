# Film Noir Title Sequence

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/film-noir-titles) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/film-noir-titles)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** motion-studies
- **作品发布时间：** 2026-10-16
- **收集日期：** 2026-11-05
- **文本类型：** 作者公开完整可复用模板
- **参考素材：** 参见正文要求
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second opening title sequence in the style of a 1940s Hollywood film noir.

<inputs>
Studio: Greyhaven Pictures. Title: THE LATE WITNESS. Starring: Vivian Lorne, Dex Halloran. Director: Sol Brenner. Duration: 10s. If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: grayscale only, R = G = B in every pixel. Black #070707, unlit wall #1A1A1A, lit plaster #C8C8C8 at its brightest, type #EEEEEE.
Type: Instrument Serif 400 and italic, a condensed high-contrast serif like hand-lettered title cards. Presenter: "GREYHAVEN PICTURES" in caps at 42px tracked 0.32em over "presents" in italic at 34px. Title: "THE" at 54px tracked 0.5em over "LATE" and "WITNESS" at 168px, leading 0.92, tracking 0.02em, flush right at x 1740, block top at y 250. Credits: role words in italic lowercase at 34px, names in caps at 44px tracked 0.14em. Type is a white superimposition with a 2px soft halation at 25%, beneath the grain, and always on the unlit wall.
Set: a plaster office wall filling the frame (seeded value noise, +/-4% luminance). One hard light off frame left shines through venetian blinds: at rest, a soft-edged trapezoid over x 120-880, y 120-980 (60px falloff), cut into parallel bars tilted -14 degrees: 44px of light, 30px of shadow, the bars fanning 15% wider toward the right, penumbra 4px at the left growing to 10px at the right. At x 250-430, y 930-1000: an ashtray rim in silhouette with a resting cigarette, its ember a 7px white glow that slowly brightens and dims.
Smoke: one plume from the ember, a laminar thread for its first 120px that breaks into slow curls higher up, drifting right, gone by y 140. Its brightness is density * (0.12 + 0.88 * light at that pixel), so it glows inside the bars and nearly vanishes between them.
Texture: grain at +/-5% luminance and 6-14 dust specks, re-seeded per film frame, floor(t * 24); gate weave of +/-0.6px on the same cadence; projector flicker of +/-2%; an oval vignette down to 65% brightness in the corners.
Banned: color or sepia, typewriter fonts or reveals, lens flares, glitch, heavy scratches, camera shake, guns, blood, a visible face, flashing more than 3 times per second.
</direction>

<structure>
0.0-0.9s: a near-black wall; only the ember and a faint thread of smoke.
0.9-3.0s: the blinds' light slides in from beyond the left edge and eases to rest.
1.6-3.6s: the presenter lines dissolve in on the dark right side.
3.4-5.0s: the figure's shadow slides in from the left and stops centered.
4.2-5.4s: the title dissolves in.
5.6-6.6s: someone tilts the blinds open.
6.6-7.8s: "starring" and the two names dissolve in under the title.
7.8-8.8s: "directed by" and the director's name dissolve in beneath.
8.8-10.0s: hold; only smoke, ember, grain and the breathing sway continue.
</structure>

<build>
One self-contained index.html, CSS and JS inline. The stage is 1920x1080 (16:9), scaled to fit the window. Design for 60fps. window.seek(t), t in seconds, must compute every visual from t alone. Engine: Canvas. One WebGL canvas runs a fragment shader; the type is DOM above it. A top Canvas 2D adds grain, dust and vignette. No three.js.
</build>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
