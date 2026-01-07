---
sidebar_position: 52
---

# ClaimExtractor

**File:** `graphrag/index/operations/extract_covariates/claim_extractor.py`

## Overview

ClaimExtractor

Class responsible for orchestrating claim extraction from input texts using configurable prompts and parsing the results into structured dictionaries. It updates claim objects with resolved entity identifiers and supports customizable delimiters and error handling.

Args:
  model_invoker: ChatModel
    The model invoker used to run prompts.
  extraction_prompt: str | None
    Custom prompt for extraction. If None, defaults to EXTRACT_CLAIMS_PROMPT.
  input_text_key: str | None
    Key in the inputs for the input text.
  input_entity_spec_key: str | None
    Key for the entity specifications.
  input_claim_description_key: str | None
    Key for the claim description.
  input_resolved_entities_key: str | None
    Key for the resolved entities used to update claims.
  tuple_delimiter_key: str | None
    Key for the tuple delimiter used when parsing claims.
  record_delimiter_key: str | None
    Key for the record delimiter used when parsing claims.
  completion_delimiter_key: str | None
    Key for the completion delimiter used to signal end of extraction.
  max_gleanings: int | None
    Maximum number of gleanings (iterations) to perform during extraction.
  on_error: ErrorHandlerFn | None
    Optional error handler callback invoked on errors.

Returns:
  None
    Initializes the instance; no return value is produced.

Raises:
  Exception
    Exceptions raised during initialization or by underlying components may be propagated unless handled by on_error.

## Methods

### `_clean_claim`

```python
def _clean_claim(
        self, claim: dict, document_id: str, resolved_entities: dict
    ) -> dict
```

### `_process_document`

```python
def _process_document(
        self, prompt_args: dict, doc, doc_index: int
    ) -> list[dict]
```

### `_parse_claim_tuples`

```python
def _parse_claim_tuples(
        self, claims: str, prompt_variables: dict
    ) -> list[dict[str, Any]]
```

### `__init__`

```python
def __init__(
        self,
        model_invoker: ChatModel,
        extraction_prompt: str | None = None,
        input_text_key: str | None = None,
        input_entity_spec_key: str | None = None,
        input_claim_description_key: str | None = None,
        input_resolved_entities_key: str | None = None,
        tuple_delimiter_key: str | None = None,
        record_delimiter_key: str | None = None,
        completion_delimiter_key: str | None = None,
        max_gleanings: int | None = None,
        on_error: ErrorHandlerFn | None = None,
    )
```

### `pull_field`

```python
def pull_field(index: int, fields: list[str]) -> str | None
```

### `__call__`

```python
def __call__(
        self, inputs: dict[str, Any], prompt_variables: dict | None = None
    ) -> ClaimExtractorResult
```

