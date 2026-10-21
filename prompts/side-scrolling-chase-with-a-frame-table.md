# Side-scrolling parkour with exact frame timing

[Original work](https://x.com/Kashiko_AIart/status/2093692302745383041) · [Prompt source](https://x.com/Kashiko_AIart/status/2093692302745383041)

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
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

[Discovery source](https://github.com/mikenevermiss/motionpromptgallery/blob/19ba3f6/data/items.json)

[Model attribution source](https://github.com/LuxRealGrowth/awesome-astra-video-prompts/blob/11de7ec/README.md)

Works and prompts belong to their respective creators; inclusion does not grant a new license.
