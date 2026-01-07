---
sidebar_position: 115
---

# graphrag/index/utils/string.py

## Overview

Module utilities for sanitizing inputs into safe, display-ready strings for graphrag index processing.

Exports:
  clean_str

Functions:
  clean_str(input: Any) -&gt; str
    Sanitize an input by unescaping HTML entities, removing control characters and other undesired characters, and returning a string when possible.

    Args:
      input: Any
        The value to sanitize. If the value is not a string, it is returned unchanged.

    Returns:
      str or Any
        The sanitized string if the input is a string; otherwise, the original value is returned unchanged.

    Notes:
      HTML handling: HTML entities in the input are unescaped using the html module (e.g., &amp; becomes &). No HTML tags are stripped by this function.

    Raises:
      None

    Examples:
      clean_str("Hello &amp; World") -&gt; "Hello & World"
      clean_str(123) -&gt; 123

## Functions

- [`clean_str`](../api/functions/graphrag-index-utils-string-clean-str)

