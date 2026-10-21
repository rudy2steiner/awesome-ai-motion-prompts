# Ultra-high-speed sprint motion previs

[Original work](https://x.com/Kashiko_AIart/status/2094182215894831283) · [Prompt source](https://x.com/Kashiko_AIart/status/2094182215894831283)

- **Creator:** @Kashiko_AIart
- **Model:** GPT-6 Astra (directory-reported)
- **Model attribution:** directory_reported
- **Category:** motion-studies
- **Prompt status:** Original-post text matched
- **Source check:** 2026-10-21, Chrome MCP.

The full original-language prompt and native video attachment were matched on the creator’s X page through Chrome MCP. Playback quality has not been independently reviewed. The original post does not name the coding model. GPT-6 Astra is attributed by the LuxRealGrowth directory; this model attribution is not independently confirmed.

References and prior project assets mentioned in the prompt are not bundled.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Remotionで超高速疾走モーションコンテを作ってください。フレーム単位で実際に動く3Dドローン追従型のcontrol MP4を出力。
固定された一つの3Dワールドとして構築し、床グリッド、左右の壁線、一定間隔のゲート、空間中の光跡を配置する。背景をループさせるのではなく、十分に長い一本道を実際に前進させる。
キャラクターは疾走するキャラクターをやや斜め後ろから追従する。
人物とグリッドは必ず同じ3D座標系とカメラ投影を使用してください。2D素材を拡大縮小するだけの疑似カメラにはしないでください。

【人物proxy】
全員、次の2要素だけで表現する。
1. 円形の頭
2. 傾きや回転が可能な一本の縦長胴体

【疾走速度】
見かけだけの速度表現ではなく、root座標を毎フレーム実際に前進させる。

【敵と接触frame】
敵は接触frameを決定してコース上へ固定配置する。
キャラクターは流れるような体術で3体を進行軸の外へ弾き、そのまま走り抜ける。
カメラは接触の前後だけ、短いイージングで別アングルへ移行し、接触後は必ず後方追従へ戻す。

【クリーンcontrol画面】
映像内には人物proxy、空間、接触アクセントだけを表示する。
```

[Discovery source](https://github.com/mikenevermiss/motionpromptgallery/blob/19ba3f6/data/items.json)

[Model attribution source](https://github.com/LuxRealGrowth/awesome-astra-video-prompts/blob/11de7ec/README.md)

Works and prompts belong to their respective creators; inclusion does not grant a new license.
