# OSideMedia: A florist trims, wraps and transfers one bouquet across three stages

[Source work](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/templates/seedance/omni-reference-2-5.md#filled-example) · [Author’s prompt / method](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/templates/seedance/omni-reference-2-5.md#filled-example)

- **Source account:** @OSideMedia / higgsfield-ai-prompt-skill contributors
- **Model:** Seedance 2.5 (template target; generation not confirmed)
- **Category:** explainers-data
- **Prompt status:** Published production example; rendered output not confirmed

Public production template, not a confirmed generated film or original model-run conversation. Full fenced source prompt preserved. For facial acting, fill duration, expression/AU beats, dialogue and visual fields, and consult the linked FACS reference; code-based expression control and rendering reliability are not independently validated. For the florist example, supply four image references and the stem-trimming/ribbon-tying motion video; its three stages count as one workflow, not three cases. The named model is the template target, not observed generation provenance. No rendered result is supplied by this document. Source read through Chrome MCP; generation, playback, facial accuracy, identity continuity and visual quality were not tested.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
[Characters]
<Florist> corresponds to @Image 1. Use only the appearance, hairstyle, and dark green apron.
<Assistant> corresponds to @Image 2. Use only the appearance, hairstyle, and clothing.
Do not interchange these characters' appearances, clothing, actions, positions, or dialogue.

[Props]
<Wrapped Bouquet> corresponds to @Image 3 and belongs only to <Florist> until Stage 3.
Use only the structure, flower types, and ribbon color.

[Scenes]
<Shop Workbench> references @Image 4. Use only the spatial layout, timber surfaces, and
window light. Do not use the people in the image.

[Motion and Audio]
@Video 1 defines the pacing of trimming stems and tying a ribbon. Do not use the person's
identity, clothing, or scene from the video.

[Generation Goal]
Generate an observational documentary clip. The central subject is <Florist>, and the primary
event is packing a single order from loose stems to a finished bouquet on the pickup shelf.

[Stage 1]
Initial state: <Florist> stands behind <Shop Workbench>. Loose stems, scissors, and wrapping
paper lie on the tabletop.
Primary event: <Florist> arranges the stems and trims them to length.
End state: <Florist> holds the bouquet in the left hand; the scissors are back on the right
side of the workbench.

[Stage 2]
Continue from the previous stage: both characters keep the same identities and clothing,
<Florist> still holds the bouquet, and <Assistant> already holds the wrapping paper open flat
on the workbench.
Primary event: <Florist> wraps the bouquet in the paper and ties it with the ribbon — the
bouquet goes from loose to wrapped.
End state: <Wrapped Bouquet> lies flat in the center of the workbench, ribbon bow facing camera.

[Stage 3]
Primary event: <Assistant> lifts <Wrapped Bouquet> and sets it on the pickup shelf.
End state: the bouquet is centered on the pickup shelf; both characters stand behind the
workbench looking at the finished order.

[Visual Style]
Overcast morning window light from frame-left, no fill from the camera side. Muted greens and
raw timber, one saturated accent in the ribbon. Real skin texture, visible paper grain.

[Camera]
Open on a medium shot of the workbench at chest height, hold through Stage 1, push in slowly
to the ribbon knot across Stage 2, then a single lateral move to follow the bouquet to the
shelf in Stage 3. 47° diagonal field of view throughout, no drift mid-segment.

[Audio]
Room tone, scissor snips, paper rustle, the ribbon pulling tight. <A shop bell rings once,
distant> NO BGM.

[Maintain Consistency]
Keep <Florist> and <Assistant>'s identities and clothing, the workbench orientation, the
scissors' position, and bouquet ownership consistent throughout.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
