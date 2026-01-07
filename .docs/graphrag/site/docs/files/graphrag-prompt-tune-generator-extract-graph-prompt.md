---
sidebar_position: 177
---

# graphrag/prompt_tune/generator/extract_graph_prompt.py

## Overview

Module for generating extract-graph prompts used in GraphRAG prompt tuning.

Purpose
- Provide utilities to assemble prompts for graph-based entity extraction by combining input documents, example demonstrations, and language constraints using predefined templates and an optional tokenizer.

Exports
- create_extract_graph_prompt: Build an extract-graph prompt from documents, examples, and configuration options. The function returns the constructed prompt as a string and can optionally write the result to disk if output_path is provided. Detailed parameter/return/exception behavior is documented in the function's own docstring.
- EXTRACT_GRAPH_FILENAME: Default filename 'extract_graph.txt' used when storing prompts to disk.

Overview
- The module centralizes prompt construction logic for GraphRAG's graph-extraction workflows, relying on templates from graphrag.prompt_tune.template.extract_graph and tokenizer utilities from graphrag.tokenizer.

Notes
- EXTRACT_GRAPH_FILENAME is a constant whose value is fixed in this module and does not depend on inputs. The actual behavior for how outputs are written to disk is determined by the function's implementation and its parameters.

## Functions

- [`create_extract_graph_prompt`](../api/functions/graphrag-prompt-tune-generator-extract-graph-prompt-create-extract-graph-prompt)

