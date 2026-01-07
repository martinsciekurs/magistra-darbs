---
sidebar_position: 97
---

# graphrag/index/operations/summarize_descriptions/summarize_descriptions.py

## Overview

Summarizes descriptions for graph entities and relationships using a language model.

Overview
This module provides utilities to load a summarization strategy by type, execute a summarization on descriptions for graph nodes and edges, and coordinate the overall workflow with concurrency control and progress reporting. It relies on the graph intelligence strategy to augment results and integrates with a pipeline cache and workflow callbacks.

Exports
load_strategy(strategy_type: SummarizeStrategyType) -&gt; SummarizationStrategy
    Load the summarization strategy callable for the given strategy_type.

do_summarize_descriptions(
        id: str | tuple[str, str],
        descriptions: list[str],
        ticker: ProgressTicker,
        semaphore: asyncio.Semaphore,
    )
    Run a summarization strategy on the provided descriptions for a given id or pair of ids.

get_summarized(
        nodes: pd.DataFrame, edges: pd.DataFrame, semaphore: asyncio.Semaphore
    )
    Summarize descriptions for nodes and edges and return summary dataframes.

summarize_descriptions(
        entities_df: pd.DataFrame,
        relationships_df: pd.DataFrame,
        callbacks: WorkflowCallbacks,
        cache: PipelineCache,
        strategy: dict[str, Any] | None = None,
        num_threads: int = 4,
    )
    High-level function to summarize entity and relationship descriptions from an entity graph, using a language model.

Notes
- Integrates with components such as graph_intelligence_strategy.run_graph_intelligence and progress_ticker.
- Supports concurrency via asyncio.Semaphore and progress reporting via ProgressTicker.

This module exposes the primary orchestration functions used to perform description summarization across a graph dataset.

## Functions

- [`load_strategy`](../api/functions/graphrag-index-operations-summarize-descriptions-summarize-descriptions-load-strategy)
- [`do_summarize_descriptions`](../api/functions/graphrag-index-operations-summarize-descriptions-summarize-descriptions-do-summarize-descriptions)
- [`get_summarized`](../api/functions/graphrag-index-operations-summarize-descriptions-summarize-descriptions-get-summarized)
- [`summarize_descriptions`](../api/functions/graphrag-index-operations-summarize-descriptions-summarize-descriptions-summarize-descriptions)

