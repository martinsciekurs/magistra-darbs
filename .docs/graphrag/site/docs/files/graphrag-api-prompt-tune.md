---
sidebar_position: 2
---

# graphrag/api/prompt_tune.py

## Overview

Utilities to generate indexing prompts for GraphRAG prompt tuning.

This module exposes a single public entry point, generate_indexing_prompts, which constructs indexing prompts by coordinating multiple prompt-generation components (domain content, entity types, entity relationships, community report prompts, and persona guidance) using configuration from graphrag_config_defaults and MAX_TOKEN_COUNT. It relies on the GraphRagConfig model and related utilities to tailor prompts for a given domain and language.

Key exports
- generate_indexing_prompts(config: GraphRagConfig, chunk_size: PositiveInt = graphrag_config_defaults.chunks.size, overlap: Annotated[int, annotated_types.Gt(-1)] = graphrag_config_defaults.chunks.overlap, limit: PositiveInt = 15, selection_method: DocSelectionType = DocSelectionType.RANDOM, domain: str | None = None, language: str | None = None, max_tokens: int = MAX_TOKEN_COUNT, discover_entity_types: bool = True, min_examples_required: PositiveInt = 2, n_subset_max: PositiveInt = 300, k: PositiveInt = 15, verbose: bool = False) -&gt; tuple[str, str, str]
  Generate indexing prompts. Parameters ---------- config: GraphRagConfig The GraphRag configuration. chunk_size: PositiveInt The chunk token size to use for input text units. overlap: Annotated[int, annotated_types.Gt(-1)] The number of tokens to overlap between consecutive chunks (must be greater than -1). limit: PositiveInt The limit of chunks to load. selection_method: DocSelectionType The method to select chunks. domain: str | None Optional domain to focus the prompts on. language: str | None Optional language to adapt prompts to. max_tokens: int Maximum token budget for prompts. discover_entity_types: bool Whether to generate prompts for discovering entity types. min_examples_required: PositiveInt Minimum number of examples per entity type. n_subset_max: PositiveInt Maximum number of prompt subsets. k: PositiveInt Number of examples or prompts to select per subset. verbose: bool Verbose logging.

Returns: tuple[str, str, str] The three generated prompts used for indexing.

Raises: pydantic.ValidationError if input arguments fail validation.

## Functions

- [`generate_indexing_prompts`](../api/functions/graphrag-api-prompt-tune-generate-indexing-prompts)

