---
sidebar_position: 106
---

# run_extract_claims

**File:** `graphrag/index/operations/extract_covariates/extract_covariates.py` (lines 84-137)

## Signature

```python
def run_extract_claims(
    input: str | Iterable[str],
    entity_types: list[str],
    resolved_entities_map: dict[str, str],
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    strategy_config: dict[str, Any],
) -> CovariateExtractionResult
```

## Description

Run the Claim extraction chain to derive covariates from input text.

Args:
    input: str | Iterable[str]
        The input text or collection of texts to process.
    entity_types: list[str]
        The entity types to consider when extracting claims.
    resolved_entities_map: dict[str, str]
        Mapping of resolved entities for the extraction process.
    callbacks: WorkflowCallbacks
        Callbacks used during model invocation and extraction.
    cache: PipelineCache
        Cache to use for model invocations.
    strategy_config: dict[str, Any]
        Strategy configuration for the extraction, including llm settings,
        prompts, and claim description.

Returns:
    CovariateExtractionResult
        The extraction result containing covariates derived from the claims.

Raises:
    ValueError
        If claim_description is missing from strategy_config (i.e., claim_description
        is required for claim extraction).

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/extract_covariates/claim_extractor.py::ClaimExtractor`
- `graphrag/index/operations/extract_covariates/extract_covariates.py::create_covariate`
- `graphrag/index/operations/extract_covariates/typing.py::CovariateExtractionResult`
- `graphrag/language_model/manager.py::ModelManager`

## Called By

This function is called by:

- `graphrag/index/operations/extract_covariates/extract_covariates.py::run_strategy`

