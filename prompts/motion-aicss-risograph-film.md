# Risograph Film

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/risograph-film) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/risograph-film)

- **作者：** sevenevesai
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** music-audiovisual
- **作品发布时间：** 2026-09-22
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
## Print system

- Paper: warm cream `#F2EDE3`, cloudy mottling and fibre flecks, baked once, static.
- Inks: blue `#0078BF`, fluorescent pink `#FF48B0`, yellow `#FFE800`, green `#00A95C`, orange
  `#FF6C2F`, violet `#765BA7`, indigo `#2E3192`. Choose for the subject; no pair has a fixed
  role. Three or four inks per scene. No pure black: overprint for darks.
- Screen each plate at ~4–5 px pitch at 1080 with distinct angles (e.g. 15°, 45°, 75°, 0°).
  Gradients change dot size; mid-tones leave paper between dots.
- Fix each ink's 1–3 px registration offset per scene; the subject's own contours reveal it.
- Starvation, speckle and carved highlights where they describe form; grain and contour wobble
  stable over time. No uniformly smooth fills or mechanical outlines.
- Clear value hierarchy: paper, a screened middle, an overprint dark where depth needs it. Choose
  sparse or dense deliberately; give each image time to read at its real speed; follow the eye
  through a handoff instead of forcing it back to centre.

[…]

## Motion, sound and text

- Take transformations from the subject's material and action (deformation, unfolding, flow,
  occlusion, growth, fracture, reveal, drift, stillness). Ripple, iris, collision and bloom are
  options, not obligatory beats.
- Every paper hold or hard cut needs a purpose. Full-scene dissolves are not a fix for
  disconnected shots; design any ink transformation explicitly.
- Score with tempo, phrasing and timbre from the subject; no fixed BPM, note pair or ending chord.
  Build from the `── sound kit ──` in [studies/sound.html](../studies/sound.html), measure with
  `tools/audio.mjs` before any full render; the `riso-score` skill runs that stage.
- Text and signatures are optional; draw glyphs as paths ([lettering](drawing.md#text-in-the-frame)).
  Never append an inherited title card.
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
