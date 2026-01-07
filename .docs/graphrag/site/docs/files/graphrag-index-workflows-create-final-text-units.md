---
sidebar_position: 123
---

# graphrag/index/workflows/create_final_text_units.py

## Overview

Utilities to transform input text units into final text units by incorporating entities, relationships, and optional covariates, and to orchestrate storage I/O for the final dataset.

Purpose
Provide the core transformation logic and workflow orchestration to produce the final_text_units table by merging text units with their related entities, relationships, and covariates, and persisting the result to storage.

Key exports
- create_final_text_units(text_units, final_entities, final_relationships, final_covariates)
  Transforms input text units and their associations into the final text units DataFrame.

- run_workflow(config, context)
  Load inputs from storage, build the final text units using the entities, relationships, and optional covariates, and write the result back to storage.

Brief summary
Defines internal helpers (_covariates, _entities, _join, _relationships) to compute mappings and assembles the final text units DataFrame, then provides a workflow function to execute the transformation within a configured storage context.

## Functions

- [`_covariates`](../api/functions/graphrag-index-workflows-create-final-text-units-covariates)
- [`_entities`](../api/functions/graphrag-index-workflows-create-final-text-units-entities)
- [`_join`](../api/functions/graphrag-index-workflows-create-final-text-units-join)
- [`_relationships`](../api/functions/graphrag-index-workflows-create-final-text-units-relationships)
- [`create_final_text_units`](../api/functions/graphrag-index-workflows-create-final-text-units-create-final-text-units)
- [`run_workflow`](../api/functions/graphrag-index-workflows-create-final-text-units-run-workflow)

