# Pop-Up Book


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/pop-up-book) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/pop-up-book) · [对应动效输出](https://www.aicssanimations.com/previews/pop-up-book.mp4)

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
Make a 10-second pop-up book animation: a book opens and paper layers stand up into a scene, then a page turns and a second scene rises.

<inputs>
- Title: Bryony and the Lighthouse (Paperhare Press).
- Scene 1, dusk pines and a lit cabin: "Bryony walked all night through the tall pines,"
- Scene 2, a lighthouse above waves: "until she saw the lighthouse, still awake."
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Set: an oak table #C49466, a dusty teal wall #6E9BA2, window light from the left casting soft shadows.
Book: a board book (front cover, one stiff leaf, back cover; 2.2 × 2.8 units) on one spine. Cover: navy cloth #2F4B6E, a cream label with the title in Young Serif. Pages cream #F6EFDF.
Pieces are 0.006-thick cards cut to silhouettes from canvases: flat inks, 4% grain, a 3px white uncut border, skies in 3–4 flat bands. Dusk: sky #F2C38B to #D9876A, mountains #6B7FA6, pines #2E5E4E, cabin #B5533C. Night: sky #22305A, sea #1F4E79, lighthouse #F4EBDD banded #C8463A.
Mechanism is the point: every standing piece is a V-fold driven only by its spread angle α (0° closed, 180° open): a card folded on a center crease, its bottom edges glued along hinges meeting the gutter at angle β, opening toward the reader. Gutter along y, reader at −y: the fixed hinge is h_R = (sin β, −cos β, 0); h_L is its mirror on the moving page, rotated with it. The crease is c = normalize(h_R × h_L), upward sign; each half's points are P0 + u·h + v·c. Pieces rise as the spread opens and fold flat as it closes, nothing stretching.
Three V-folds per scene at different points along the gutter; one β per scene (60°, then 66°) keeps them parallel, so they never collide. Each line prints along the right page's foot in Young Serif, at least 28px on stage. Scene 2's beam is a paper fan on a hidden wheel.
Motion: the cover opens over 2.4s (easeInOutCubic). The turn is the rigid leaf rotating 180° about the spine over 2.2s (easeInOutSine): spread 1 closes as spread 2 opens. No piece has its own timer.
Camera: fov 30, reader's side, 40° up, the spread filling 72% of the width; it starts close on the cover.
Premium is paper engineering you can believe: pieces rising only because pages open, layered shadows, crisp cut edges. Cheap is cut-outs fading or scaling out of the page.
Banned: stretching or intersecting pieces, motion independent of the page angle, fades, glossy paper, gradients on paper, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: the closed book; the camera hangs close over the cover.
- 1.0–3.4s: the cover opens; mountains, pines and cabin stand up in depth order, shadows sweeping the page.
- 3.4–4.8s: scene 1 complete; the camera settles and drifts in.
- 4.8–7.0s: the page turns; the forest folds flat beneath it as lighthouse, rocks and waves rise.
- 7.0–8.4s: scene 2 complete; the paper beam swings 30° across the sky.
- 8.4–10s: hold.
Other lengths: scale the opening and the turn together; hold at least 1.2s.
</structure>

<build>
One self-contained index.html, inline CSS and JS, on a 1920×1080 (16:9) stage scaled to fit the window, built for 60fps. Google Fonts via <link>, awaited with document.fonts.load() before seek exists.
window.seek(t) sets every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Every piece's pose is solved from its spread angle, a pure function of t.
Without ?render in the URL, drive seek from requestAnimationFrame; with ?render, don't start that loop.
three.js as an ES module pinned to three@0.160.0 via a jsDelivr import map (`three`, `three/addons/`); preserveDrawingBuffer: true; one render per seek. No image, model or typeface files beyond Google Fonts.
</build>

<check>
Before showing me, step through one frame per second (0–10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style or Banned. Look for a piece standing further than its spread allows, layers touching each other or the turning leaf, illegible printed lines, a cropped spread. Confirm the final frame holds.
</check>
```
