---
sidebar_position: 14
---

# graphrag/cli/prompt_tune.py

## Overview

Asynchronous prompt tuning orchestration for the GraphRag CLI.

Purpose
- This module exposes the prompt_tune coroutine which coordinates configuration loading, chunking overrides, logging initialization, and indexing-prompt generation for prompt tuning.

Key exports
- prompt_tune(root: Path, config: Path | None, domain: str | None, verbose: bool, selection_method: api.DocSelectionType, limit: int, max_tokens: int, chunk_size: int, overlap: int, language: str | None, discover_entity_types: bool, output: Path, n_subset_max: int, k: int, min_examples_required: int) -&gt; None
  Coroutine that loads the configuration, applies any chunking overrides, initializes the root logger according to the verbose flag, and generates indexing prompts. It writes the resulting prompts to the specified output directory if an output path is provided; otherwise it logs an error and skips writing. Returns None upon successful completion.

Summary
- The module centralizes the prompt-tuning workflow by combining configuration loading, logging setup, chunking adjustments, and prompt generation into a single entry point exposed as prompt_tune for asynchronous invocation.

## Functions

- [`prompt_tune`](../api/functions/graphrag-cli-prompt-tune-prompt-tune)

