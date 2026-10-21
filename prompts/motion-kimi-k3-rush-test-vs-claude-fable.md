# Rolling the obelisk: 3D Egyptology physics explainer

[Source work](https://generative-ai.review/2026/07/kimi-k3-rush-test-vs-claude-fable/) · [Upstream prompt transcription](https://github.com/mikenevermiss/motionpromptgallery/blob/19ba3f6/data/items.json)

- **Source account:** Terry Lurie
- **Model:** Kimi K3 / Claude Fable 5 (directory reported; not independently confirmed for this work)
- **Category:** explainers-data
- **Prompt status:** Upstream transcription
- **Completeness:** Not independently assessed

Selected from the upstream prompt collection for its concrete creative direction. Prompt text is inherited from that collection; completeness is not independently assessed and any referenced inputs may be required; this import does not independently confirm the original post, model attribution, result fidelity or visual quality. Referenced files, music, images and project context are not bundled. Original upstream source notes are retained below. Upstream notes: Starting prompt verbatim from the article's appendix (the author says it was written by Google Gemini). Kimi K3 (free-tier K3 Max on kimi.com) got this one prompt only — an unrefined one-shot.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a complete, single-file HTML web application using Three.js (via CDN) that demonstrates a detailed 3D physics/engineering concept animation. 

CRITICAL VISUAL & PHYSICS REQUIREMENTS:
1. Dynamic Labels: Use THREE.CSS2DRenderer to create clear, legible HTML text labels that follow their respective 3D objects (e.g., "Heavy Load", "Wooden Raft", "Water Level", "Scaffolding"). Include a thin SVG or CSS line connector linking the label to its subject.
2. Rotational Detail: The rolling logs must have highly visible longitudinal stripes or a "barber pole" multi-material pattern so their rotation is perfectly obvious to the viewer.
3. Physics Alignment: Ensure strict geometric alignment. Rolling logs must be perfectly perpendicular (90 degrees) to the direction of the load's movement.
4. Rotational Accuracy: Logs must rotate in exact synchronization with the linear movement of the load ($rotation = position / radius$) to simulate true rolling without slipping.
5. Scale & Context (Humanoids): Include simple, low-poly humanoid figures (built from spheres, capsules, and cylinders) to represent workers. They should actively pose: pushing the load in Stage 0, pulling/towing lines in Stage 3, and standing on the platform.

Technical Infrastructure:
- Include OrbitControls for camera tracking.
- Implement a clean HTML/CSS overlay UI with a "Next Step" button and a text card describing the current physics phase.
- Use a robust state machine (`currentStage` 0 to 6) in the `requestAnimationFrame` loop to ensure smooth, unglitched transitions.
- Generate all textures procedurally using HTML Canvas (`CanvasTexture`) to avoid external image loading or CORS errors.

Animation Stages to Implement:

Stage 0: Load Rolling
- Setup: An empty wooden raft sits on the ground. A heavy block (the load) sits behind it on 4 striped cylindrical logs. Low-poly workers stand behind it in a pushing pose.
- Animation: The workers push, and the block moves forward onto the center of the raft. The logs roll perfectly beneath it, rotating in the correct direction. Once the load is centered, the logs roll away.

Stage 1: Wall Enclosure
- Animation: Thick wooden walls with external angled buttresses slide up from the ground, creating a tight, parallel, perpendicular, watertight enclosure around the raft.

Stage 2: Water Filling & Floating
- Animation: A semi-transparent blue water mesh slowly rises. As it hits the raft, the raft and load realistically float upward due to buoyancy, maintaining stable alignment. A label tracks the rising "Water Level".

Stage 3: Towing
- Animation: Humanoid figures stand at the edge of the pool holding lines. They pull, and the raft is towed horizontally across the water to the far edge/corner of the pool.

Stage 4: Scaffolding Construction
- Animation: A structured grid of thin beige scaffolding beams rapidly assembles/scales up directly underneath the elevated raft, filling the void between the pool floor and the raft.

Stage 5: Draining the Pool
- Animation: The water level drains back to zero. The raft and load remain perfectly stationary, their weight visibly transferring onto the newly built scaffolding platform.

Stage 6: Roll Off
- Animation: Striped logs appear on top of the scaffolding platform beneath the raft. The workers push the raft/load combination smoothly off the scaffolding structure and out of frame.

Provide the complete, self-contained `index.html` file with all CSS, JS, and Three.js logic included. Ensure shadows are enabled on all lights and meshes for depth and grounding.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
