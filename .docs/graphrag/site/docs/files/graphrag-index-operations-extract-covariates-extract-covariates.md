---
sidebar_position: 68
---

# graphrag/index/operations/extract_covariates/extract_covariates.py

## Overview

Utilities to extract covariates from text within the GraphRAG indexing workflow.

Overview
This module implements helpers to construct covariate objects from raw data, merge covariate information into claim-derived rows, and orchestrate covariate extraction from input text using a strategy, with support for asynchronous processing, caching, and workflow callbacks. It defines a default set of entity types and exposes the primary extraction routines used by the covariate extraction pipeline.

Key exports
- DEFAULT_ENTITY_TYPES: List of default entity types used when extracting covariates. Values: ["organization", "person", "geo", "event"]
- create_covariate(item: dict[str, Any]) -&gt; Covariate: Create a Covariate instance from the provided item. Reads keys such as subject_id, object_id, type, status, start_date, end_date, description, source_text, record_id, and id.
- create_row_from_claim_data(row, covariate_data: Covariate, covariate_type: str): Create a row from claim data and the input row by merging in covariate fields and covariate_type.
- run_extract_claims(
    input: str | Iterable[str],
    entity_types: list[str],
    resolved_entities_map: dict[str, str],
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    strategy_config: dict[str, Any],
  ) -&gt; CovariateExtractionResult: Run the claim extraction chain to derive covariates from input text.
- run_strategy(row): Run the strategy on a single input row to asynchronously extract covariates from text.
- extract_covariates(
    input: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    column: str,
    covariate_type: str,
    strategy: dict[str, Any] | None,
    async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types: list[str] | None = None,
    num_threads: int = 4,
  )
  : Process a DataFrame by applying covariate extraction to the text in a specified column for each row, returning covariate rows as a DataFrame.

## Functions

- [`create_covariate`](../api/functions/graphrag-index-operations-extract-covariates-extract-covariates-create-covariate)
- [`create_row_from_claim_data`](../api/functions/graphrag-index-operations-extract-covariates-extract-covariates-create-row-from-claim-data)
- [`run_extract_claims`](../api/functions/graphrag-index-operations-extract-covariates-extract-covariates-run-extract-claims)
- [`run_strategy`](../api/functions/graphrag-index-operations-extract-covariates-extract-covariates-run-strategy)
- [`extract_covariates`](../api/functions/graphrag-index-operations-extract-covariates-extract-covariates-extract-covariates)

