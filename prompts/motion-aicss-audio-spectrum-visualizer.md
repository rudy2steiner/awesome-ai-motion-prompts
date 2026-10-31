# Audio Visualizer


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/audio-spectrum-visualizer) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/audio-spectrum-visualizer) · [对应动效输出](https://www.aicssanimations.com/previews/audio-spectrum-visualizer.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** music-audiovisual
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
Make a 10-second audio visualizer: a short track synthesized in code drives a radial spectrum that pulses on the beat.

<inputs>
- Artist: Okra Lights. Track: "Glasshouse". Label line: "New single".
- Tempo and key: 128 BPM, A minor.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: coral ground #F2552C, lifting to #FF7445 behind the center and deepening to #D9401F at the corners; bars cream #FFF3E2; bar tips butter #FFD25A; center disc ink #22121F; type cream on the disc and ink #22121F on the ground.
Type: Unbounded 700 for the track title (64px, on the disc), Unbounded 400 for the artist (28px, on the disc), Manrope 600 for the label line and a time counter (22px, uppercase, tracked 0.14em), set at the top left (96, 72) and bottom left (96, 1000).
The sound is real, computed at load: synthesize 10s of mono audio at 22,050 Hz into a Float32Array (a seeded PRNG for noise; nothing is played, since the preview is silent). Beats fall at t = 0.75 + k × 60/128 s. Parts: a pad, A minor 9 (A3 C4 E4 G4 B4), two slightly detuned saws per note through a one-pole low-pass opening from 400 Hz to 2.5 kHz over the first 2s; a kick on every beat (a sine sweeping 150 → 45 Hz in 0.12s, decay τ 0.16s); a bass on eighth notes (A1 A1 C2 G1, two beats each, a saw through a 300 Hz low-pass); from beat 4, claps on the second and fourth beat of each bar (noise band-passed at 1–3 kHz, 0.14s) and closed hats on the off-beats (high-passed noise, 30ms); from beat 8, a sixteenth-note arpeggio of the pad notes an octave up. On beat 16 (8.25s) everything plays one accented hit and stops; the pad tail is silent by 8.9s.
Analysis, once at load: every 1/60 s, a 2,048-sample Hann-windowed FFT; bins grouped into 64 log-spaced bands from 40 Hz to 10 kHz; magnitudes to dB, mapped −70…0 dB to 0…1; then smoothed in time with a fast attack (0.6) and a slow release (0.12) in one pass. seek(t) reads this table and interpolates between frames; nothing is random at draw time.
Visual, centered at (960, 540): an ink disc 360px across, scaling by up to 4% with the kick's envelope. Around it, starting at radius 240, 128 bars: the 64 bands mirrored left and right, lows at the bottom, highs at the top; each bar is 7px wide with round caps and 8 + 200 × level px long, its outer 20% in butter. Between disc and bars, a 2px cream ring traces the current 40ms of the waveform, ±12px. A 3px progress arc (radius 480, cream at 40%) grows with the track's position. On each bar's downbeat (every fourth beat) one thin cream ring expands from the disc edge to radius 520 and fades over 0.9s.
Everything that moves is driven by the sound, apart from the opening build. Bars never move unless the audio does, and the opening filter visibly lights the mid bands before the drums arrive.
The real thing is honest: kicks you can see in the low bars, hats in the highs, stillness where the music stops. The cheap version is random bars bouncing to nothing under a neon glow.
Banned: random or sine-faked bar heights, neon glow, rainbow hue cycling, beat strobes or screen flashes, camera shake, particles, real artists, labels or streaming platforms, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.75s: coral ground; the disc scales up from 0 (0.5s, cubic-bezier(0.16, 1, 0.3, 1)); title and artist rise 12px into it; from 0.4s the bars grow out of the disc edge in a sweep from the bottom, already reading the pad.
0.75–2.6s: kick and bass enter: the low bars punch on every beat, the disc breathes with the kick, and the first downbeat ring expands.
2.6–4.5s: claps and hats arrive: the upper-middle bars snap on the backbeats and the top bars tick on the off-beats; the label line and time counter fade up.
4.5–8.25s: the arpeggio fills the high bands; the spectrum is at its fullest.
8.25–8.9s: the last hit lands with one final ring; every bar decays to its 8px minimum as the pad tail dies.
8.9–10.0s: hold on the still circle: title on the disc, progress arc complete, counter stopped at the track's end.
For other durations, keep the tempo, add or remove whole four-beat bars before the final hit, and keep at least 1s of silent hold.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries (no three.js, no audio libraries). Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the CSS size × devicePixelRatio. Canvas won't fetch fonts itself: await document.fonts.load() for each face, then define window.seek. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.
window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. The synthesis, FFTs and smoothing run once at load at a fixed 1/60 s step (well under 2s of work); seek(t) only reads the results.
Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Seek to a kick (t = 0.75 + k × 0.46875) and to just between two kicks to confirm the low bars rise and fall with them; confirm the high bars stay low before 2.6s, the bars never touch the labels, the waveform ring stays clear of the disc and bars, and every bar rests at its minimum after 8.9s. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
