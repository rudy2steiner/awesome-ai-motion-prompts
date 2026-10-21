# Contributing

Submit one source-backed work per contribution. All models and platforms are welcome. Documentation and descriptions should be in English; preserve the original language of published prompts.

Include the creator, original work URL, prompt URL, reported model, categories, preview dimensions, reference requirements and production dependencies. Explain what makes the motion worth studying. Link any public source code or skill. Do not download full video libraries or add unrelated application code.

Add complete records to `data/motion-prompts.json`, their prompt cards to `examples/`, and evidence to `data/provenance.json`. Put incomplete research in `data/candidates.json`; do not fill gaps with invented claims. See [the data contract](docs/DATA_FORMAT.md) and [verification rules](docs/SOURCING.md).

Run:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

For corrections or removals, open an issue with the record ID, original source and requested change. Credit the original creator and keep third-party licensing separate from repository maintenance code.
