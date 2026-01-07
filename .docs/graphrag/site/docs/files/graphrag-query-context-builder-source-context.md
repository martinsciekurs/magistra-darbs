---
sidebar_position: 189
---

# graphrag/query/context_builder/source_context.py

## Overview

Utilities to build source context for system prompts from text units in Graphrag.

This module provides helpers to count how many relationships of a given entity relate to a text unit and to assemble a context table built from text units for generating system prompts in Graphrag.

Functions:
  count_relationships(entity_relationships: list[Relationship], text_unit: TextUnit) -&gt; int
    Returns the number of relationships for the selected entity that relate to the given text unit.
    Args:
      entity_relationships: The relationships for the selected entity.
      text_unit: The text unit to evaluate.
    Returns:
      int: The number of relationships in entity_relationships that are associated with text_unit.

  build_text_unit_context(text_units: list[TextUnit], tokenizer: Tokenizer | None = None, column_delimiter: str = "|", shuffle_data: bool = True, max_context_tokens: int = 8000, context_name: str = "Sources", random_state: int = 86) -&gt; tuple[str, dict[str, pd.DataFrame]]
    Builds a textual context from text units suitable for inclusion in system prompts.
    Args:
      text_units: Text units to include in the context.
      tokenizer: Tokenizer used to count tokens; if None, a tokenizer is retrieved with get_tokenizer().
      column_delimiter: Delimiter used to separate fields in the context rows.
      shuffle_data: Whether to shuffle the rows before building the context.
      max_context_tokens: Maximum total tokens allowed in the context.
      context_name: Label used for the context section in the prompt.
      random_state: Seed for deterministic shuffling when shuffle_data is True.
    Returns:
      tuple[str, dict[str, pd.DataFrame]]: The constructed context string and a mapping of DataFrames with context data.

Raises:
  TypeError: If an argument is of an unexpected type.
  ValueError: If numeric parameters have invalid values or if values are incompatible.
  Exception: Propagates exceptions from tokenizer retrieval or data handling.

## Functions

- [`count_relationships`](../api/functions/graphrag-query-context-builder-source-context-count-relationships)
- [`build_text_unit_context`](../api/functions/graphrag-query-context-builder-source-context-build-text-unit-context)

