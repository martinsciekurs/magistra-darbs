---
sidebar_position: 259
---

# tests/unit/indexing/verbs/helpers/mock_llm.py

## Overview

Test utilities for constructing mock language models used in unit tests.

This module exposes helpers to create deterministic mock ChatModel instances that yield a predefined sequence of responses, enabling reliable testing of code paths that interact with an LLM without contacting a real model. Mock models are created or retrieved via ModelManager to align with the project's model-management approach.

Exports:
- create_mock_llm(responses, name="mock"): ChatModel
  Creates and returns a mock ChatModel configured to yield the provided responses.

Functions:
- create_mock_llm(responses: list[str | BaseModel], name: str = "mock") -&gt; ChatModel
  Creates a mock LLM that returns the given responses in the specified order.
  Args:
    responses: The responses to be returned by the mock LLM. Each element may be a string or a Pydantic BaseModel instance.
    name: The name assigned to the mock LLM. Defaults to "mock".
  Returns:
    ChatModel: A mock ChatModel configured to return the provided responses in order.
  Raises:
    Exception: If an error occurs while creating or retrieving the mock chat model via ModelManager.

Brief summary:
- Used by tests under tests/unit/indexing/verbs/helpers to simulate LLM behavior without relying on a real language model.

## Functions

- [`create_mock_llm`](../api/functions/tests-unit-indexing-verbs-helpers-mock-llm-create-mock-llm)

