# Apple-Style Kinetic Recap

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/apple-style-kinetic-recap) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/apple-style-kinetic-recap)

- **作者：** Damir
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** product-brand
- **作品发布时间：** 2026-09-28
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
# apple-motion

Every default here is measured, not guessed: six Apple recap videos (1107 s, 33,187 frames) went
through a forensic pipeline (OCR text tracking, spring fitting, optical flow, beat tracking,
loudness), and the pipeline itself was calibrated on renders with known springs and fonts.
Not affiliated with Apple.

[…]

- **Pace.** Median shot 56.5 frames (1.9 s); p10 13.0, p90 173.5 frames; 3.24 cuts per 10 s (median video). Transitions: cut 92%, whip 5%, scale through 1%, dissolve 1%.
- **Typography is an accent, not the bed.** Designer-set type appears 0.78 times per 10 s (median video); most on-screen text is UI inside product shots. Hold 33.0 frames median (p10 10.0, p90 80.6).
- **Size.** Cap height median 6.67% of frame height (p10 3.25%, p90 20.23%). Lines: 1 84%, 2 10%, 4 4%. Alignment: center 60%, right 19%, left 15%.
- **Entries.** cut on 25%, slide 21%, fade 18%, scale down from large 9%, per-letter 7%. Animated entries are visibly done in 8.0 frames (median). Spring (calibrated): damping 15.35, stiffness 115.0, mass 1 - use it without durationInFrames.
- **Exits.** cut off 59%, slide out 13%, fade out 10%, blur out 7%; median 0.0 frames.
- **Sound.** 118.8 BPM median (p10 91.9, p90 131.3); -17.4 LUFS integrated, -2.0 dBTP true peak; voice-over at 3.04 words/s. Cuts are not locked to the beat: 134/400 within +-2 frames vs 124.8 expected by chance (p=0.1586) - the edit follows the voice and picture.
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
