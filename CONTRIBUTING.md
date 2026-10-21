# Submissions welcome!

**Add your motion directly under a category in [README.md](README.md#prompt-library), then open a pull request.** All models, platforms and creators are welcome.

## Where do I edit?

1. Open [README.md in the GitHub editor](https://github.com/rudy2steiner/awesome-ai-motion-prompts/edit/main/README.md). GitHub will help you fork the repository if needed.
2. Find the matching heading under **Prompt library**, such as **Product & Brand** or **Typography & Motion Studies**.
3. Add your motion at the end of that category, above its `Add new ... motions above this line` comment. Open a PR with a short note about your work.

Copy this format and replace the placeholders:

```markdown
- **[Your motion title](https://your-video-or-demo-url)** — by [@creator](https://creator-or-original-post-url) · Model name · [Prompt](https://your-prompt-or-skill-url)
```

Add a short GIF preview below your entry so readers can see the motion without leaving GitHub. Link the preview to your in-repository prompt card when you have one:

```markdown
  [<img src="https://your-preview-image-url" width="280" alt="Your motion title" />](https://your-video-or-demo-url)
```

If your prompt is not hosted elsewhere, copy [`examples/_template.md`](examples/_template.md) to `examples/your-motion-name.md`, add the prompt, and link that file from your README entry.

**You do not need to edit JSON files or run a build to submit a motion.** The README is community-maintained; the build script does not overwrite it. Maintainers handle structured metadata separately.

## What to include

A playable preview, the prompt or skill, creator credit and the model used. Keep descriptions in English and prompts in their original language. Mention required references, tools and important follow-up prompts when relevant. Credit the original creator when recommending someone else's work.

There is no follower, view or star threshold. One work per PR keeps discussion focused. If no category fits, suggest a new heading in the same PR. Continue updating that PR if reviewers request changes.

## For maintainers

After reviewing an entry, optionally add its structured record to `data/motion-prompts.json`, provenance to `data/provenance.json`, and its primary category to `data/categories.json`. Keep the README entry in place. Incomplete research can remain in `data/candidates.json`.

Run `python3 scripts/build.py` and `python3 scripts/validate.py` when changing structured data. Neither command replaces the README. See the [data contract](docs/DATA_FORMAT.md) and [verification rules](docs/SOURCING.md).

For corrections or removals, open an issue or PR identifying the work and requested change. Third-party works retain their creators' rights; see [third-party content](THIRD_PARTY.md).
