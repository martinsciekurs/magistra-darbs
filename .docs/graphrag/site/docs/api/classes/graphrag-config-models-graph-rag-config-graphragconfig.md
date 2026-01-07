---
sidebar_position: 42
---

# GraphRagConfig

**File:** `graphrag/config/models/graph_rag_config.py`

## Overview

GraphRagConfig is a Pydantic-based configuration model that aggregates and validates GraphRag's diverse configuration options.

Args:
- None: This model is constructed via Pydantic from internal fields representing sub-configs; there are no explicit __init__ parameters exposed.

Returns:
- GraphRagConfig: The same instance after initialization and internal validation.

Raises:
- ValueError: If a configuration value is invalid or required paths are missing.
- FileNotFoundError: If a required root_dir or other directory does not exist.
- LanguageModelConfigMissingError: If a default language model is not configured when required.

Key attributes:
- Sub-config models such as BasicSearchConfig, CacheConfig, ChunkingConfig, ClusterGraphConfig, CommunityReportsConfig, DRIFTSearchConfig, EmbedGraphConfig, ClaimExtractionConfig, ExtractGraphConfig, ExtractGraphNLPConfig, GlobalSearchConfig, InputConfig, LanguageModelConfig, LocalSearchConfig, PruneGraphConfig, ReportingConfig, SnapshotsConfig, StorageConfig, SummarizeDescriptionsConfig, TextEmbeddingConfig, UmapConfig, VectorStoreConfig.
- Factories RateLimiterFactory and RetryFactory used for validating rate limiting and retry strategies.

Summary:
GraphRagConfig acts as the centralized, validated container for the GraphRag configuration, coordinating multiple sub-configs and providing utilities for path normalization, model validation, and access to vector store and language model configurations.

## Methods

### `_validate_input_base_dir`

```python
def _validate_input_base_dir(self) -> None
```

### `_validate_rate_limiter_services`

```python
def _validate_rate_limiter_services(self) -> None
```

### `_validate_reporting_base_dir`

```python
def _validate_reporting_base_dir(self) -> None
```

### `_validate_factories`

```python
def _validate_factories(self) -> None
```

### `_validate_model`

```python
def _validate_model(self)
```

### `_validate_output_base_dir`

```python
def _validate_output_base_dir(self) -> None
```

### `_validate_retry_services`

```python
def _validate_retry_services(self) -> None
```

### `__str__`

```python
def __str__(self)
```

### `get_vector_store_config`

```python
def get_vector_store_config(self, vector_store_id: str) -> VectorStoreConfig
```

### `_validate_vector_store_db_uri`

```python
def _validate_vector_store_db_uri(self) -> None
```

### `_validate_input_pattern`

```python
def _validate_input_pattern(self) -> None
```

### `_validate_multi_output_base_dirs`

```python
def _validate_multi_output_base_dirs(self) -> None
```

### `get_language_model_config`

```python
def get_language_model_config(self, model_id: str) -> LanguageModelConfig
```

### `__repr__`

```python
def __repr__(self) -> str
```

### `_validate_models`

```python
def _validate_models(self) -> None
```

### `_validate_update_index_output_base_dir`

```python
def _validate_update_index_output_base_dir(self) -> None
```

### `_validate_root_dir`

```python
def _validate_root_dir(self) -> None
```

