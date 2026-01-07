---
sidebar_position: 127
---

# graphrag/index/workflows/factory.py

## Overview

GraphRag workflows factory for building pipelines of workflow functions.

This module coordinates registration and construction of pipelines composed of workflow functions for GraphRag-based indexing workflows. It maintains a class-level registry of named WorkflowFunction callables and can assemble these into reusable Pipeline objects that process GraphRag data.

Public API
- PipelineFactory: Class that coordinates registration and construction of pipelines composed of workflow functions. Maintains a class-level registry of named WorkflowFunction callables and can assemble these into Pipeline objects.
- register(cls, name: str, workflow: WorkflowFunction): Register a custom workflow function.
- register_all(cls, workflows: dict[str, WorkflowFunction]): Register a dict of custom workflow functions.
- create_pipeline(cls, config: GraphRagConfig, method: IndexingMethod | str = IndexingMethod.Standard) -&gt; Pipeline: Create a pipeline for executing a sequence of workflows. Returns a Pipeline. Raises: KeyError if any workflow name is missing.
- register_pipeline(cls, name: str, workflows: list[str]): Register a new pipeline method as a list of workflow names.

## Classes

- [`PipelineFactory`](../api/classes/graphrag-index-workflows-factory-pipelinefactory)

## Functions

- [`register`](../api/functions/graphrag-index-workflows-factory-register)
- [`register_all`](../api/functions/graphrag-index-workflows-factory-register-all)
- [`create_pipeline`](../api/functions/graphrag-index-workflows-factory-create-pipeline)
- [`register_pipeline`](../api/functions/graphrag-index-workflows-factory-register-pipeline)

