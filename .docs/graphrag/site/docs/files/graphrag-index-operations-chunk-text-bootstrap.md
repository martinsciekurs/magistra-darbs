---
sidebar_position: 55
---

# graphrag/index/operations/chunk_text/bootstrap.py

## Overview

Bootstrap initialization for NLTK resources used by the chunk_text operations.

This module provides a one-time bootstrap sequence that downloads and prepares the
required NLTK data on the first call to bootstrap() and loads WordNet via the wn alias
(from nltk.corpus import wordnet as wn). A module-level flag initialized_nltk tracks
whether the bootstrap has already run; after initialization, subsequent calls to
bootstrap() are effectively no-ops.

Exports:
- bootstrap() -&gt; None: One-time initializer for NLTK resources. Returns None. May raise
  network/IO-related exceptions if resources cannot be downloaded.
- initialized_nltk -&gt; bool: Flag indicating initialization status (True after successful bootstrap).

Notes:
- WordNet is exposed in this module via the wn alias (from nltk.corpus import wordnet as wn).
- The listed resources are illustrative; the actual resources downloaded may vary by environment.
- If initialization fails, callers may retry or handle the error as appropriate.

Resource list (illustrative):
punkt, punkt_tab, averaged_perceptron_tagger, averaged_perceptron_tagger_eng,
maxent_ne_chunker, maxent_ne_chunker_tab, words, ...

## Functions

- [`bootstrap`](../api/functions/graphrag-index-operations-chunk-text-bootstrap-bootstrap)

