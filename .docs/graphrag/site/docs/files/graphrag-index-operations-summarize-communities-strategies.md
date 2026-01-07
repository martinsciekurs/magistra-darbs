---
sidebar_position: 88
---

# graphrag/index/operations/summarize_communities/strategies.py

## Overview

Strategies for graph intelligence summarization of communities.

Purpose
Implements the extraction strategy used to produce CommunityReport objects from input text for a given community by leveraging a language model and the CommunityReportsExtractor. It coordinates model interaction, caching, and callback hooks as part of the summarization workflow.

Key exports
- _run_extractor(model: ChatModel, community: str | int, input: str, level: int, args: StrategyConfig) -&gt; CommunityReport | None
  Run the CommunityReportsExtractor to produce a CommunityReport from the given input.

- run_graph_intelligence(community: str | int, input: str, level: int, callbacks: WorkflowCallbacks, cache: PipelineCache, args: StrategyConfig) -&gt; CommunityReport | None
  Run the graph intelligence entity extraction strategy.

Brief summary
The module encapsulates the graph intelligence strategy for summarizing communities by extracting structured reports from text. It relies on CommunityReportsExtractor along with language-model, caching, and callback infrastructure to generate a CommunityReport at the specified level, or None if extraction yields no report.

## Functions

- [`_run_extractor`](../api/functions/graphrag-index-operations-summarize-communities-strategies-run-extractor)
- [`run_graph_intelligence`](../api/functions/graphrag-index-operations-summarize-communities-strategies-run-graph-intelligence)

