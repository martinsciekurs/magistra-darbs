---
sidebar_position: 209
---

# graphrag/query/structured_search/drift_search/state.py

## Overview

Drift search state management for structured search queries.

This module defines a graph-based representation of drift search actions using DriftAction nodes and a QueryState class to manage the graph. It provides functionality to add actions, relate follow-ups, serialize/deserialize the graph, compute token usage across actions, locate incomplete actions, and rank them.

Public objects:
- class QueryState: Represents the state of a drift search query as a graph of DriftAction nodes. This class is instantiated without external parameters and manages a directed graph of DriftAction nodes, enabling addition of actions, linking follow-ups, serialization/deserialization, and ranking of incomplete actions.

Public methods:
- action_token_ct(self) -&gt; dict[str, int]
  Return the token counts across all actions in the graph. Each node in the graph has metadata with keys 'llm_calls', 'prompt_tokens', and 'output_tokens'. Returns a dictionary with keys 'llm_calls', 'prompt_tokens', and 'output_tokens' mapping to the summed counts across all nodes.

- __init__(self)
  Initialize the drift query state with an empty graph.

- serialize(self, include_context: bool = True) -&gt; dict[str, Any] | tuple[dict[str, Any], dict[str, Any], str]
  Serialize the graph to a dictionary representation, optionally including contextual information for nodes.

- find_incomplete_actions(self) -&gt; list[DriftAction]
  Find all unanswered actions in the graph.

- add_action(self, action: DriftAction, metadata: dict[str, Any] | None = None)
  Add an action node to the graph with optional metadata.

- add_all_follow_ups(self, action: DriftAction, follow_ups: list[DriftAction] | list[str], weight: float = 1.0)
  Add all follow-up actions and link them to the given action.

- deserialize(self, data: dict[str, Any])
  Deserialize the dictionary back to a graph.

- relate_actions(self, parent: DriftAction, child: DriftAction, weight: float = 1.0)
  Relate two actions in the graph.

- rank_incomplete_actions(self, scorer: Callable[[DriftAction], float] | None = None) -&gt; list[DriftAction]
  Rank all incomplete actions in the graph, optionally by a scorer.

## Classes

- [`QueryState`](../api/classes/graphrag-query-structured-search-drift-search-state-querystate)

## Functions

- [`action_token_ct`](../api/functions/graphrag-query-structured-search-drift-search-state-action-token-ct)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-state-init)
- [`serialize`](../api/functions/graphrag-query-structured-search-drift-search-state-serialize)
- [`find_incomplete_actions`](../api/functions/graphrag-query-structured-search-drift-search-state-find-incomplete-actions)
- [`add_action`](../api/functions/graphrag-query-structured-search-drift-search-state-add-action)
- [`add_all_follow_ups`](../api/functions/graphrag-query-structured-search-drift-search-state-add-all-follow-ups)
- [`deserialize`](../api/functions/graphrag-query-structured-search-drift-search-state-deserialize)
- [`relate_actions`](../api/functions/graphrag-query-structured-search-drift-search-state-relate-actions)
- [`rank_incomplete_actions`](../api/functions/graphrag-query-structured-search-drift-search-state-rank-incomplete-actions)

