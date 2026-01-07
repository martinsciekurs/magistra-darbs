---
sidebar_position: 180
---

# graphrag/prompt_tune/loader/input.py

## Overview

Utilities to load input documents and prepare text chunks for prompt tuning in GraphRAG.

Purpose
Provide helper routines to convert input documents into chunked base text units and to sample or embed chunks to meet a given selection strategy for prompt generation.

Key exports
- _sample_chunks_from_embeddings: samples k text chunks whose embeddings are closest to the embedding set center.
- load_docs_in_chunks: loads documents according to the configured input, converts to base text units with chunking configuration, and returns a list of chunk texts with braces escaped to prevent Python's str.format issues when parsing LaTeX in Markdown.

Brief summary
These helpers bridge the input layer and the prompt-tuning workflow by producing suitably sized batches of text chunks for downstream embedding or prompt construction.

## Functions

- [`_sample_chunks_from_embeddings`](../api/functions/graphrag-prompt-tune-loader-input-sample-chunks-from-embeddings)
- [`load_docs_in_chunks`](../api/functions/graphrag-prompt-tune-loader-input-load-docs-in-chunks)

