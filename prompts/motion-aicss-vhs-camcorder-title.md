# VHS Camcorder Home Video Title

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/vhs-camcorder-title) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/vhs-camcorder-title)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** motion-studies
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-05
- **文本类型：** 作者公开完整可复用模板
- **参考素材：** 参见正文要求
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second home-video title as if shot on a 1989 VHS camcorder and played back on a VCR.

<inputs>
Title: "SUMMER AT" / "LAKE TAMSIN". Subtitle: "THE MERRIN FAMILY". Date stamp: "AUG 12 1989" over "4:32 PM". Scene: a lake at golden hour seen from a wooden dock, with a red canoe tied at the end. Duration: 10s. If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Frame: a 4:3 picture, 1440x1080, centered between black #000000 pillars 240px wide.
Two layers, two rules. The scene, the burned-in date stamp, the zoom bar and the camcorder title are drawn together into a 480x360 buffer and degraded as one recorded signal. The VCR's own overlay ("PLAY" with a play triangle, and a tape counter) is drawn afterward at full resolution, crisp and untouched by the tape.
Scene, in the buffer: sky #8EC1E6 fading to #F4D29C at the horizon, a low sun disc #FFE7B0, a dark tree line #2C4527, water #4C7C9E with drifting horizontal glints, dock planks #8A6A44 in one-point perspective, the red canoe #C8352B at the dock's end.
Tape degradation: convert to YIQ; blur Y horizontally over 2px; blur I and Q over 8px and shift them 3px right; lift blacks to #101010 and clip whites at 92%; add luma noise of +/-4%; add 0-3 dropouts; jitter the bottom 8 lines sideways by up to 12px.
Type: the VCR overlay in VT323, 64px, white. The camcorder title and date stamp are drawn into the buffer in Press Start 2P and degraded with the picture.
Banned: RGB split or offset color copies, datamosh, pixel sorting, CRT curvature, real camera or tape brand names, 16:9 footage, emoji, full-frame flashes.
</direction>

<structure>
0.0-0.8s: VCR blue #1A2FD0 fills the picture; the PLAY overlay appears at 0.2s.
0.8-1.8s: the picture locks in: a 100px band of tracking noise rolls from bottom to top.
1.8-3.0s: the lake, handheld, the date stamp already burned in.
3.0-4.8s: the title writes on, centered in two lines.
4.8-6.6s: the camera zooms slowly toward the canoe (1.0 -> 1.3).
6.6-7.1s: one tracking wobble.
7.1-8.4s: the subtitle writes on beneath the title.
8.4-10.0s: hold.
</structure>

<build>
One self-contained index.html, CSS and JS inline. The stage is 1920x1080 (16:9). Engine: Canvas 2D. Draw the scene into the 480x360 buffer, run the YIQ pass, upscale, then draw the VCR overlay. No three.js.
</build>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
