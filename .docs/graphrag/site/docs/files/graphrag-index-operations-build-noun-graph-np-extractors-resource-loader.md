---
sidebar_position: 53
---

# graphrag/index/operations/build_noun_graph/np_extractors/resource_loader.py

## Overview

Resource loader for NLTK resources used by noun graph extraction.

Purpose:
    Provide a minimal helper to ensure required NLTK resources are available by
    checking for their presence and downloading them if they are not already
    installed. This helps prevent failures during noun-graph extraction due to missing data.

Exports:
    - download_if_not_exists(resource_name: str) -&gt; bool

Summary:
    The function returns True when the requested resource is already present locally
    and no download was necessary; returns False when the resource was missing and
    had to be downloaded. If the download operation fails, the function may raise
    an exception from the underlying NLTK downloader (e.g., network-related errors).

Usage:
    from graphrag.index.operations.build_noun_graph.np_extractors.resource_loader import download_if_not_exists
    if download_if_not_exists("punkt"):
        print("Resource available.")
    else:
        print("Resource downloaded.")

Notes:
    - Resource names should follow NLTK's data naming conventions (e.g., "punkt",
      "averaged_perceptron_tagger").
    - The function may perform network I/O and write to the NLTK data directory.

## Functions

- [`download_if_not_exists`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-resource-loader-download-if-not-exists)

