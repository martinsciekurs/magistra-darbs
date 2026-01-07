---
sidebar_position: 266
---

# tests/unit/utils/test_encoding.py

## Overview

Tests for encoding/tokenizer utilities (get_tokenizer) used by graphrag.

Purpose
- Validate that get_tokenizer selects the correct tokenizer backend based on the provided model_config and its encoding_model attribute, ensuring a tiktoken-based tokenizer is used when appropriate, and verifying token counts for inputs.

Inputs
- This module contains two tests: test_encode_basic and test_num_tokens_empty_input. They call get_tokenizer with different configurations but do not accept input parameters themselves.

Returns
- None. Tests return None on success; they raise AssertionError if an assertion fails.

Raises
- AssertionError: if tokenizer selection or token counts do not match expectations.

Key exports
- test_encode_basic
- test_num_tokens_empty_input

Summary
- The tests exercise the tokenizer selection logic (distinguishing tiktoken-based paths when model_config is None or encoding_model is set) and verify that empty input yields zero tokens.

## Functions

- [`test_encode_basic`](../api/functions/tests-unit-utils-test-encoding-test-encode-basic)
- [`test_num_tokens_empty_input`](../api/functions/tests-unit-utils-test-encoding-test-num-tokens-empty-input)

