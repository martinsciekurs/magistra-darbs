---
sidebar_position: 29
---

# _prompt_tune_cli

**File:** `graphrag/cli/main.py` (lines 289-410)

## Signature

```python
def _prompt_tune_cli(
    root: Path = typer.Option(
        Path(),
        "--root",
        "-r",
        help="The project root directory.",
        exists=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        autocompletion=ROOT_AUTOCOMPLETE,
    ),
    config: Path | None = typer.Option(
        None,
        "--config",
        "-c",
        help="The configuration to use.",
        exists=True,
        file_okay=True,
        readable=True,
        autocompletion=CONFIG_AUTOCOMPLETE,
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Run the prompt tuning pipeline with verbose logging.",
    ),
    domain: str | None = typer.Option(
        None,
        "--domain",
        help=(
            "The domain your input data is related to. "
            "For example 'space science', 'microbiology', 'environmental news'. "
            "If not defined, a domain will be inferred from the input data."
        ),
    ),
    selection_method: DocSelectionType = typer.Option(
        DocSelectionType.RANDOM.value,
        "--selection-method",
        help="The text chunk selection method.",
    ),
    n_subset_max: int = typer.Option(
        N_SUBSET_MAX,
        "--n-subset-max",
        help="The number of text chunks to embed when --selection-method=auto.",
    ),
    k: int = typer.Option(
        K,
        "--k",
        help="The maximum number of documents to select from each centroid when --selection-method=auto.",
    ),
    limit: int = typer.Option(
        LIMIT,
        "--limit",
        help="The number of documents to load when --selection-method={random,top}.",
    ),
    max_tokens: int = typer.Option(
        MAX_TOKEN_COUNT,
        "--max-tokens",
        help="The max token count for prompt generation.",
    ),
    min_examples_required: int = typer.Option(
        2,
        "--min-examples-required",
        help="The minimum number of examples to generate/include in the entity extraction prompt.",
    ),
    chunk_size: int = typer.Option(
        graphrag_config_defaults.chunks.size,
        "--chunk-size",
        help="The size of each example text chunk. Overrides chunks.size in the configuration file.",
    ),
    overlap: int = typer.Option(
        graphrag_config_defaults.chunks.overlap,
        "--overlap",
        help="The overlap size for chunking documents. Overrides chunks.overlap in the configuration file.",
    ),
    language: str | None = typer.Option(
        None,
        "--language",
        help="The primary language used for inputs and outputs in graphrag prompts.",
    ),
    discover_entity_types: bool = typer.Option(
        True,
        "--discover-entity-types/--no-discover-entity-types",
        help="Discover and extract unspecified entity types.",
    ),
    output: Path = typer.Option(
        Path("prompts"),
        "--output",
        "-o",
        help="The directory to save prompts to, relative to the project root directory.",
        dir_okay=True,
        writable=True,
        resolve_path=True,
    ),
) -> None
```

## Description

Generate custom graphrag prompts for a project using provided configuration and options.

Args:
    root: The project root directory.
    config: The configuration to use.
    verbose: Run the prompt tuning pipeline with verbose logging.
    domain: The domain your input data is related to. If not defined, a domain will be inferred from the input data.
    selection_method: The text chunk selection method.
    n_subset_max: The number of text chunks to embed when --selection-method=auto.
    k: The maximum number of documents to select from each centroid when --selection-method=auto.
    limit: The number of documents to load when --selection-method=&#123;random,top&#125;.
    max_tokens: The max token count for prompt generation.
    min_examples_required: The minimum number of examples to generate/include in the entity extraction prompt.
    chunk_size: The size of each example text chunk. Overrides chunks.size in the configuration file.
    overlap: The overlap size for chunking documents. Overrides chunks.overlap in the configuration file.
    language: The primary language used for inputs and outputs in graphrag prompts.
    discover_entity_types: Discover and extract unspecified entity types.
    output: The directory to save prompts to, relative to the project root directory.

Returns:
    None

## Dependencies

This function calls:

- `graphrag/cli/prompt_tune.py::prompt_tune`

