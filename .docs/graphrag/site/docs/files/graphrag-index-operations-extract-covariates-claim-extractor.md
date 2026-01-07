---
sidebar_position: 67
---

# graphrag/index/operations/extract_covariates/claim_extractor.py

## Overview

Module for claim extraction within the covariates extraction workflow.

Overview: This module defines the ClaimExtractor class which orchestrates the extraction of claims from input documents by invoking a ChatModel-driven prompt workflow, parsing the results into structured dictionaries, and updating claim objects with resolved entity identifiers. It supports configurable delimiters for tuples, records, and completion markers and relies on default configuration and prompt components defined elsewhere in the project.

Key exports:
- ClaimExtractor: Class that coordinates the extraction process using configurable prompts, delimiters, and error handling.
- _clean_claim, _process_document, _parse_claim_tuples: Internal helper methods used by ClaimExtractor to update claims, process documents, and parse claim tuples.
- DEFAULT_TUPLE_DELIMITER, DEFAULT_RECORD_DELIMITER, DEFAULT_COMPLETION_DELIMITER: Delimiter constants used to parse and delineate claim data.

Notes:
- Depends on graphrag_config_defaults and prompts CONTINUE_PROMPT, EXTRACT_CLAIMS_PROMPT, and LOOP_PROMPT.
- Updates claim objects with resolved entity identifiers via a provided resolved_entities mapping.
- Supports an optional on_error callback to handle errors during processing.

Raises:
- Exceptions raised by the underlying ChatModel invocations, parsing logic, or the error handler (if provided).

## Classes

- [`ClaimExtractor`](../api/classes/graphrag-index-operations-extract-covariates-claim-extractor-claimextractor)

## Functions

- [`_clean_claim`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-clean-claim)
- [`_process_document`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-process-document)
- [`_parse_claim_tuples`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-parse-claim-tuples)
- [`__init__`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-init)
- [`pull_field`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-pull-field)
- [`__call__`](../api/functions/graphrag-index-operations-extract-covariates-claim-extractor-call)

