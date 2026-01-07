---
sidebar_position: 102
---

# graphrag/index/text_splitting/text_splitting.py

## Overview

Text splitting utilities for token-based chunking in Graphrag.

Purpose
This module defines a small API for splitting text into chunks that fit token/length constraints, leveraging a Tokenizer. It provides a base abstract splitter, a no-op splitter, and a concrete TokenTextSplitter that uses a Tokenizer to perform chunking. It also exposes common type aliases used by token encoding/decoding.

Exports
- EncodedText = list[int]
- DecodeFn = Callable[[EncodedText], str]
- EncodeFn = Callable[[str], EncodedText]
- LengthFn = Callable[[str], int]
- TokenTextSplitter: splits input text into chunks using a tokenizer
- TextSplitter: abstract base class for text splitting
- NoopTextSplitter: returns input unchanged

Summary
The module provides a shared interface and concrete implementations to split text into chunks suitable for downstream processing (e.g., embeddings), with support for token-based splitting via a Tokenizer and optional progress tracking through a ProgressTicker.

## Classes

- [`TokenTextSplitter`](../api/classes/graphrag-index-text-splitting-text-splitting-tokentextsplitter)
- [`TextSplitter`](../api/classes/graphrag-index-text-splitting-text-splitting-textsplitter)
- [`NoopTextSplitter`](../api/classes/graphrag-index-text-splitting-text-splitting-nooptextsplitter)

## Functions

- [`num_tokens`](../api/functions/graphrag-index-text-splitting-text-splitting-num-tokens)
- [`split_multiple_texts_on_tokens`](../api/functions/graphrag-index-text-splitting-text-splitting-split-multiple-texts-on-tokens)
- [`split_text`](../api/functions/graphrag-index-text-splitting-text-splitting-split-text)
- [`__init__`](../api/functions/graphrag-index-text-splitting-text-splitting-init)
- [`split_single_text_on_tokens`](../api/functions/graphrag-index-text-splitting-text-splitting-split-single-text-on-tokens)
- [`split_text`](../api/functions/graphrag-index-text-splitting-text-splitting-split-text)
- [`split_text`](../api/functions/graphrag-index-text-splitting-text-splitting-split-text)
- [`__init__`](../api/functions/graphrag-index-text-splitting-text-splitting-init)

