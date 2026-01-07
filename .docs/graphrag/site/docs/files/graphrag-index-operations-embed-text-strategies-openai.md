---
sidebar_position: 66
---

# graphrag/index/operations/embed_text/strategies/openai.py

## Overview

OpenAI-based embedding strategy implementation for embedding text inputs within the graphrag pipeline.

Overview: This module defines internal helpers and the entry point to generate vector embeddings for input texts. It coordinates tokenization, text splitting, and batching under model constraints, performing asynchronous embedding calls through an EmbeddingModel and integrating with PipelineCache and WorkflowCallbacks used by the graphrag pipeline. The main entry point is run(...), which orchestrates the workflow and returns a TextEmbeddingResult.

Args:
  None: The module does not define top-level parameters. Use run(input, callbacks, cache, args) to perform embedding with provided inputs.

Returns:
  TextEmbeddingResult: The run function returns a TextEmbeddingResult containing the embeddings and related metadata.

Raises:
  Exceptions raised by the embedding model or I/O operations may propagate to the caller.

Key exports:
  _reconstitute_embeddings: Reconstitute embeddings into the original input texts.
  _prepare_embed_texts: Prepare a flat list of text snippets and per-input sizes.
  _create_text_batches: Create batches of texts respecting batch constraints.
  embed: Async helper to embed a batch of text chunks with concurrency control.
  _get_splitter: Build a TokenTextSplitter configured for the model config.
  _execute: Async orchestration to embed batches with a concurrency semaphore.
  run: Entry point to execute the embedding workflow given inputs, callbacks, cache, and args.

## Functions

- [`_reconstitute_embeddings`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-reconstitute-embeddings)
- [`_prepare_embed_texts`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-prepare-embed-texts)
- [`_create_text_batches`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-create-text-batches)
- [`embed`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-embed)
- [`_get_splitter`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-get-splitter)
- [`_execute`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-execute)
- [`run`](../api/functions/graphrag-index-operations-embed-text-strategies-openai-run)

