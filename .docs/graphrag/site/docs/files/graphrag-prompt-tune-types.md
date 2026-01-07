---
sidebar_position: 181
---

# graphrag/prompt_tune/types.py

## Overview

Module that defines document selection strategies used in the prompt tuning workflow of GraphRAG.

Purpose:
    This module exposes four string-valued constants and an Enum describing strategies for selecting documents during prompt tuning:
    ALL, RANDOM, TOP, AUTO, and DocSelectionType.

Key exports:
    ALL (str): The "all" selection strategy.
    RANDOM (str): The "random" selection strategy.
    TOP (str): The "top" selection strategy.
    AUTO (str): The "auto" selection strategy.
    DocSelectionType: Enum with members ALL, RANDOM, TOP, AUTO and their corresponding string values.

__str__ behavior:
    The __str__ method on DocSelectionType returns the string representation of the enum member's value.

Brief summary:
    This module centralizes document selection strategies for prompt tuning and provides a consistent API for referring to these strategies.

Args:
    None: This module does not take any parameters.

Returns:
    None: This module does not return a value.

Raises:
    None: This module does not raise exceptions on import.

## Classes

- [`DocSelectionType`](../api/classes/graphrag-prompt-tune-types-docselectiontype)

## Functions

- [`__str__`](../api/functions/graphrag-prompt-tune-types-str)

