---
sidebar_position: 51
---

# graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py

## Overview

Validators for noun-phrase extraction components used when building a noun graph.

Purpose
This module provides small, stateless validators to assist in NP extraction:
- detection of hyphenated compound tokens
- validation of token length constraints
- validation of entity validity relative to a token sequence

Public API
- is_compound(tokens: list[str]) -&gt; bool
    Return True if any token in the provided list is a hyphenated compound token.
    Args: tokens: List[str] - The list of tokens to inspect.
    Returns: bool - True if at least one token contains a hyphen, has length greater than 1 after stripping whitespace, and splits into more than one part when split by hyphen; otherwise False.
    Raises: None
- has_valid_token_length(tokens: list[str], max_length: int) -&gt; bool
    Check if all tokens have valid length.
    Args: tokens: List of tokens to validate lengths for. max_length: Maximum allowed length for any token.
    Returns: bool: True if all tokens have length &lt;= max_length, otherwise False.
    Raises: None
- is_valid_entity(entity: tuple[str, str], tokens: list[str]) -&gt; bool
    Check if the given entity is valid with respect to the provided tokens.
    Args: entity: tuple[str, str] - The entity as (text, label). The label indicates the category of the entity, e.g., CARDINAL or ORDINAL.
          tokens: list[str] - The tokens associated with the entity used to determine validity.
    Returns: bool - True if the entity is valid according to the validation rules; otherwise False.
    Raises: None

Brief summary
The functions are pure validators used by higher-level noun-phrase processing to enforce
hyphenation rules, length constraints, and consistency between entities and token sequences.

## Functions

- [`is_compound`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-np-validator-is-compound)
- [`has_valid_token_length`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-np-validator-has-valid-token-length)
- [`is_valid_entity`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-np-validator-is-valid-entity)

