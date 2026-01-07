---
sidebar_position: 118
---

# graphrag/index/workflows/create_base_text_units.py

## Overview

Module to generate base text units for GraphRAG indexing.

Purpose
This module provides utilities to convert input documents into base text units by grouping texts, chunking them into smaller units, and applying optional metadata preprocessing. It also exposes an entry point to run the workflow that loads documents, chunks them, and writes the resulting text units back to storage.

Exports
- chunker(row: pd.Series) -&gt; Any: Chunk a row into text chunks, optionally prepending metadata to each chunk. Relies on outer-scope configuration such as prepend_metadata, size, overlap, encoding_model, strategy, and callbacks.
- chunker_with_logging(row: pd.Series, row_index: int) -&gt; Any: Log chunker progress for a row during chunking. Executes the chunker on the given row and logs progress using total_rows from the surrounding scope.
- create_base_text_units(documents: pd.DataFrame, callbacks: WorkflowCallbacks, group_by_columns: list[str], size: int, overlap: int, encoding_model: str, strategy: ChunkStrategyType, prepend_metadata: bool = False, chunk_size_includes_metadata: bool = False) -&gt; pd.DataFrame: Converts input documents into base text units by grouping, chunking, and optional metadata preprocessing.
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput: Runs the base text units workflow to transform documents into base text units by loading documents from storage, chunking them, and writing the resulting text units back to storage.

Summary
This module coordinates chunking logic, encoding strategies, and storage utilities to produce base text units ready for downstream GraphRAG processing.

## Functions

- [`chunker`](../api/functions/graphrag-index-workflows-create-base-text-units-chunker)
- [`chunker_with_logging`](../api/functions/graphrag-index-workflows-create-base-text-units-chunker-with-logging)
- [`create_base_text_units`](../api/functions/graphrag-index-workflows-create-base-text-units-create-base-text-units)
- [`run_workflow`](../api/functions/graphrag-index-workflows-create-base-text-units-run-workflow)

