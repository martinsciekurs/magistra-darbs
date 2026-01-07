---
sidebar_position: 3
---

# Quick Start

This Quick Start guide provides a practical tour to install and begin using GraphRAG, covering setup, indexing, prompt tuning, and querying workflows. It is designed to get you from zero to an actionable index and query flow as quickly as possible.

Prerequisites
- Python 3.10–3.12
- uv (the task runner) for dependency management and workflow orchestration

1) Install dependencies
```
uv sync
```

2) Initialize a project/workspace
This creates a settings file and environment configuration. Replace [path] with your working directory.
```
graphrag init --root [path] --force
```

3) Prepare your dataset
Create a folder with input text files, e.g. a simple example:
```
[path]/input/book.txt
```
You can adapt this to your private dataset; the indexing engine will process documents into TextUnits and extract entities/relationships.

4) Configure a backend (OpenAI or Azure OpenAI)
- OpenAI: set GRAPHRAG_API_KEY in the generated .env.
- Azure OpenAI: configure chat and embedding model blocks in settings.yaml (api_base, api_version, deployment_name, etc.).

5) Run the indexing workflow
```
graphrag index --root [path]
```
Or, depending on your setup, you may see project-specific commands via uv/poethepoet integration.

6) Prompt tuning (optional but recommended for best results)
```
uv run poe prompt_tune --root [path]
```

7) Query the index
```
uv run poe query --root [path] --query "What are the top themes in this dataset?"
```

8) Next steps
- Inspect the output directory for graph data and parquet artifacts.
- Try different query modes (global, local, DRIFT, or basic) to compare results.
- Use the Unified Search Demo UI (if available) for interactive exploration.

For hands-on examples and a walkthrough, see the Getting Started guide in the docs.
