---
sidebar_position: 182
---

# graphrag/query/context_builder/builders.py

## Overview

Module for constructing DRIFT context used to prime downstream search actions for a given query. This module defines an abstract interface and concrete builders that assemble the context required by DRIFT-based search processes. It relies on pandas for context representation (DataFrame) and on the ConversationHistory type to optionally incorporate prior dialogue when building the context.

Public API
- DRIFTContextBuilder: Abstract base class defining the contract for building the DRIFT context.
- BasicContextBuilder: Concrete implementation that builds the minimal context for the basic search mode, combining the user query with optional conversation history.
- GlobalContextBuilder: Concrete implementation that builds the context for the global search mode.
- LocalContextBuilder: Abstract base class for building the local-context used in local search mode.

Notes
- All build_context methods return a ContextBuilderResult, a structured result type defined elsewhere in the codebase that encapsulates the built context (typically including a DataFrame of items and any associated metrics).

Dependencies
- pandas (as pd)
- ConversationHistory (from graphrag.query.context_builder.conversation_history)

## Classes

- [`DRIFTContextBuilder`](../api/classes/graphrag-query-context-builder-builders-driftcontextbuilder)
- [`BasicContextBuilder`](../api/classes/graphrag-query-context-builder-builders-basiccontextbuilder)
- [`GlobalContextBuilder`](../api/classes/graphrag-query-context-builder-builders-globalcontextbuilder)
- [`LocalContextBuilder`](../api/classes/graphrag-query-context-builder-builders-localcontextbuilder)

## Functions

- [`build_context`](../api/functions/graphrag-query-context-builder-builders-build-context)
- [`build_context`](../api/functions/graphrag-query-context-builder-builders-build-context)
- [`build_context`](../api/functions/graphrag-query-context-builder-builders-build-context)
- [`build_context`](../api/functions/graphrag-query-context-builder-builders-build-context)

