---
sidebar_position: 96
---

# graphrag/index/operations/summarize_descriptions/graph_intelligence_strategy.py

## Overview

Module to orchestrate the summarization of descriptions for graph intelligence workflows. This module provides two entry points that coordinate the summarization of input descriptions into a concise description suitable for graph intelligence tasks by leveraging a language model and a description summarizer. It supports direct summarization via a ChatModel and a graph intelligence strategy coordinated through a PipelineCache. Key exports: - run_summarize_descriptions - run_graph_intelligence Summary: Exposes two entry points that orchestrate the summarization process: one uses a ChatModel to perform direct summarization; the other coordinates the graph intelligence strategy using a cache and a strategy configuration. Functions: - run_summarize_descriptions(model: ChatModel, id: str | tuple[str, str], descriptions: list[str], args: StrategyConfig) -&gt; SummarizedDescriptionResult: Run the summarization process to convert descriptions into a summarized result using the provided chat model. - run_graph_intelligence(id: str | tuple[str, str], descriptions: list[str], cache: PipelineCache, args: StrategyConfig) -&gt; SummarizedDescriptionResult: Run the graph intelligence summarization strategy using a PipelineCache and the provided descriptions and strategy config.

## Functions

- [`run_summarize_descriptions`](../api/functions/graphrag-index-operations-summarize-descriptions-graph-intelligence-strategy-run-summarize-descriptions)
- [`run_graph_intelligence`](../api/functions/graphrag-index-operations-summarize-descriptions-graph-intelligence-strategy-run-graph-intelligence)

