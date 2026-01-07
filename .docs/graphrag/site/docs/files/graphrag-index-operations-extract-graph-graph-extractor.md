---
sidebar_position: 70
---

# graphrag/index/operations/extract_graph/graph_extractor.py

## Overview

Graph extraction from text to construct graphs using a language model.

Purpose
- Provide a GraphExtractor class and helpers to extract graph-structured information from natural language text by querying a language model with predefined prompts and assembling the results into a NetworkX graph. The extractor supports optional multi-step gleaning via continuation prompts when configured.

Key exports
- GraphExtractor: orchestrates graph extraction from text using prompts and a ChatModel
- _unpack_source_ids(data: Mapping[str, Any]) -&gt; list[str]: helper to extract source_id values from a mapping
- _unpack_descriptions(data: Mapping[str, Any]) -&gt; list[str]: helper to split a description field into lines
- DEFAULT_TUPLE_DELIMITER, DEFAULT_RECORD_DELIMITER, DEFAULT_COMPLETION_DELIMITER, DEFAULT_ENTITY_TYPES

Behavior and graph shape
- The extraction produces an undirected Graph (nx.Graph). Nodes represent entities; edges encode inferred relations derived from the prompts’ interpretation. The exact graph shape depends on the prompts and the model output.

Configuration and error handling
- Delimiters and prompt variable keys can be overridden via GraphExtractor constructor arguments or per-call prompt_variables.
- Language model errors, parsing issues, or unexpected output are surfaced via the on_error callback when provided; otherwise exceptions propagate to the caller. Internal logging records diagnostics.

API details
- _unpack_source_ids(data: Mapping[str, Any]) -&gt; list[str]
  - Returns all source_id strings found in data, or [] if absent or None.
- _unpack_descriptions(data: Mapping[str, Any]) -&gt; list[str]
  - Splits the description field into lines; returns [] if no description. Raises AttributeError if description exists but is not splittable.
- GraphExtractor.__init__(...) -&gt; None
  - Initializes with a ChatModel and optional keys for tuple/record delimiters, input text, entity types, and a completion delimiter, plus join_descriptions, max_gleanings, and on_error.
- GraphExtractor.__call__(texts: list[str], prompt_variables: dict[str, Any] | None = None) -&gt; GraphExtractionResult
  - Executes extraction on the given texts; returns a GraphExtractionResult containing results (per-document or aggregated). May raise exceptions from the model or processing steps.
- GraphExtractor._process_document(text: str, prompt_variables: dict[str, str]) -&gt; str
  - Processes a single document to accumulate intermediate results; returns a string payload for downstream parsing.
- GraphExtractor._process_results(results: dict[int, str], tuple_delimiter: str, record_delimiter: str) -&gt; nx.Graph
  - Parses the collected results and returns an undirected NetworkX graph.

Defaults
- DEFAULT_TUPLE_DELIMITER: "&lt;|&gt;"
- DEFAULT_RECORD_DELIMITER: "##"
- DEFAULT_COMPLETION_DELIMITER: "&lt;|COMPLETE|&gt;"
- DEFAULT_ENTITY_TYPES: ["organization", "person", "geo", "event"]

Notes
- The graph building behavior is driven by the prompt templates GRAPH_EXTRACTION_PROMPT, LOOP_PROMPT, and CONTINUE_PROMPT, along with the model_invoker. The final graph may be refined across gleanings if max_gleanings &gt; 0.

## Classes

- [`GraphExtractor`](../api/classes/graphrag-index-operations-extract-graph-graph-extractor-graphextractor)

## Functions

- [`_unpack_source_ids`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-unpack-source-ids)
- [`_unpack_descriptions`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-unpack-descriptions)
- [`__call__`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-call)
- [`_process_document`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-process-document)
- [`__init__`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-init)
- [`_process_results`](../api/functions/graphrag-index-operations-extract-graph-graph-extractor-process-results)

