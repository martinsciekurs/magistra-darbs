---
sidebar_position: 43
---

# graphrag/index/input/factory.py

## Overview

Factory for instantiating input data for pipelines.

This module exposes create_input, a function that instantiates input data for a pipeline by loading
data according to the provided InputConfig and using the given PipelineStorage to access the data. It
delegates to the appropriate loader (load_csv, load_json, load_text) based on the input configuration.

Key exports:
- create_input(config: InputConfig, storage: PipelineStorage) -&gt; pandas.DataFrame

Brief summary:
Given an InputConfig and a PipelineStorage, create_input loads the input data into a pandas.DataFrame using the
specified loader and returns it for downstream pipeline processing.

## Functions

- [`create_input`](../api/functions/graphrag-index-input-factory-create-input)

