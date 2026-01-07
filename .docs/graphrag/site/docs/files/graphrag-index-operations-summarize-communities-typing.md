---
sidebar_position: 93
---

# graphrag/index/operations/summarize_communities/typing.py

## Overview

Typing definitions for the summarize_communities operation.

Purpose:
    Defines typing constructs used by the summarize_communities workflow, including
    common data type aliases, an enumeration of strategies for generating community
    reports, and a callable type for strategies. The module references PipelineCache
    and WorkflowCallbacks for related types.

Key exports:
    ExtractedEntity: dict[str, Any]
    StrategyConfig: dict[str, Any]
    RowContext: dict[str, Any]
    EntityTypes: list[str]
    Claim: dict[str, Any]
    CommunityReportsStrategy: Callable[...]
    CreateCommunityReportsStrategyType: Enum describing the strategies for creating community reports
        in the summarize_communities operation. The enum members provide their identity via their
        name and a string representation via __repr__.

Brief summary:
    This module collects typing primitives used by the summarize_communities operation to
    annotate data structures and strategy logic, enabling type checking and clearer API
    contracts within the Graphrag codebase.

## Classes

- [`CreateCommunityReportsStrategyType`](../api/classes/graphrag-index-operations-summarize-communities-typing-createcommunityreportsstrategytype)

## Functions

- [`__repr__`](../api/functions/graphrag-index-operations-summarize-communities-typing-repr)

