# Documentation Evaluation Tools

Tools for evaluating generated documentation quality.

## Tools

### combine_docs.py

Combine all markdown docs into a single JSON file for analysis or export.

```bash
python combine_docs.py <repo_name>    # Combine docs for specific repo
python combine_docs.py --all          # Combine docs for all repos
python combine_docs.py --list         # List available repos
```

Output: `.docs/<repo>/combined_docs.json`

### combine_docs_for_wikibench.py

Convert documentation to [CodeWikiBench](https://github.com/CodeWikiBench/CodeWikiBench) format.

```bash
python combine_docs_for_wikibench.py
```

Output:
```
data/<repo>/my_custom_docs/
├── docs_tree.json         # Documentation tree structure
└── structured_docs.json   # Flattened documentation content
```

### evaluate_docs.py

LLM-as-a-judge evaluation for documentation quality.

```bash
python evaluate_docs.py <repo_name>              # Evaluate 10 random samples
python evaluate_docs.py <repo_name> --sample 20  # Custom sample size
python evaluate_docs.py <repo_name> --section guide  # Specific section only
python evaluate_docs.py <repo_name> --compare <other_repo>  # Compare versions
python evaluate_docs.py <repo_name> --output results.json
```

**Evaluation Criteria (1-5 scale):**
- **Clarity**: Is it clear and easy to understand?
- **Completeness**: Does it cover functionality, parameters, returns, usage?
- **Accuracy**: Does it accurately reflect the code?
- **Structure**: Is it well-organized?
- **Usefulness**: Would it help developers?

Requires `KIMI_API_KEY` environment variable.

## CodeWikiBench Integration

To run the CodeWikiBench benchmark:

```bash
# 1. Generate docs
docgen <repo_url>

# 2. Combine docs
python eval/combine_docs.py <repo_name>

# 3. Convert to benchmark format
python eval/combine_docs_for_wikibench.py

# 4. Copy to CodeWikiBench repo and run evaluation
```

## result_analysis/

Additional analysis scripts for processing evaluation results.
