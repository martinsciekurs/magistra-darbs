---
sidebar_position: 6
---

# CLI Reference

GraphRAG ships a Command-Line Interface (CLI) that drives indexing, prompt tuning, and querying workflows. The CLI is designed to orchestrate project initialization, index construction and updates, knowledge-graph queries, and prompt tuning workflows, integrating configuration, storage, logging, and the API.

Key concepts
- Typer-based command structure for a clean, scriptable interface.
- Commands to initialize a project, run the indexer, tune prompts, and query the index from the command line.

Common commands (examples)
- Initialize a project and config:
```
graphrag init --root ./christmas --force
```

- Run the indexing workflow for a dataset:
```
graphrag index --root ./christmas
```

- Tune prompts for a dataset:
```
uv run poe prompt_tune --root ./christmas
```

- Execute a query against the index:
```
uv run poe query --root ./christmas --query "What are the top themes in this dataset?"
```

Note: The CLI relies on the underlying workflow orchestration configured in settings.yaml and uses the same modular components as the API layer. For more detailed command semantics and available options, see the CLI documentation pages in docs/cli.md and the source files listed under graphrag/graphrag/cli/.*.
