---
sidebar_position: 202
---

# graphrag/query/structured_search/base.py

## Overview

Abstract base module for structured searches using a language model and contextual builders.

Purpose
Provide the abstract BaseSearch class that defines the interface and shared configuration for structured searches that operate with a ChatModel, a context builder, and an optional tokenizer. It also maintains optional parameter dictionaries for the model and the context builder.

Exports
- BaseSearch: Abstract base class for structured searches using a language model and contextual builders.

Summary
This module serves as the foundational contract for concrete search implementations, enabling asynchronous search and optional streaming of results with pluggable contexts and tokenization.

## Classes

- [`BaseSearch`](../api/classes/graphrag-query-structured-search-base-basesearch)

## Functions

- [`search`](../api/functions/graphrag-query-structured-search-base-search)
- [`stream_search`](../api/functions/graphrag-query-structured-search-base-stream-search)
- [`__init__`](../api/functions/graphrag-query-structured-search-base-init)

