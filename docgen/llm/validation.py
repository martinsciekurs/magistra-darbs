"""Output validation helpers (quality + robustness).

These functions are intentionally lightweight and best-effort:
- Validate YAML-structured outputs (repo analysis and synthesis docs)
- Perform basic docstring sanity checks and parameter consistency checks
"""

from __future__ import annotations

import re
from typing import Any

import yaml


def _safe_load_yaml(text: str) -> tuple[Any | None, list[str]]:
    if not text or not text.strip():
        return None, ["Empty YAML"]
    try:
        return yaml.safe_load(text), []
    except Exception as e:
        return None, [f"Invalid YAML: {e}"]


def validate_repo_analysis_yaml(text: str) -> tuple[bool, list[str], dict | None]:
    """Validate YAML schema for `4_llm_summary.yaml` content."""
    data, errors = _safe_load_yaml(text)
    if errors:
        return False, errors, None
    if not isinstance(data, dict):
        return False, ["Repo analysis must be a YAML mapping/dict"], None

    schema_errors: list[str] = []
    if "summary" not in data:
        schema_errors.append("Missing key: summary")
    if "modules" not in data:
        schema_errors.append("Missing key: modules")
    elif not isinstance(data.get("modules"), list):
        schema_errors.append("modules must be a list")
    else:
        for i, mod in enumerate(data["modules"]):
            if not isinstance(mod, dict):
                schema_errors.append(f"modules[{i}] must be a dict")
                continue
            for k in ("name", "description", "files"):
                if k not in mod:
                    schema_errors.append(f"modules[{i}] missing key: {k}")
            if "files" in mod and not isinstance(mod.get("files"), list):
                schema_errors.append(f"modules[{i}].files must be a list")

    ok = len(schema_errors) == 0
    return ok, schema_errors, data if ok else None


def _parse_python_params_from_signature(signature: str) -> list[str]:
    """Best-effort parse of parameter names from a `def ...(...):` signature line."""
    if not signature:
        return []
    # Most of your signatures are the first line of the function code.
    m = re.search(r"\bdef\s+\w+\s*\((.*)\)\s*:", signature)
    if not m:
        return []

    inner = m.group(1).strip()
    if not inner:
        return []

    params: list[str] = []
    for raw in inner.split(","):
        part = raw.strip()
        if not part:
            continue
        # remove annotations/defaults and star prefixes
        part = part.lstrip("*").strip()
        name = part.split(":", 1)[0].split("=", 1)[0].strip()
        if name:
            params.append(name)

    # ignore common implicit params
    params = [p for p in params if p not in ("self", "cls")]
    return params


def validate_docstring(docstring: str, signature: str) -> tuple[bool, list[str]]:
    """Basic sanity + parameter consistency checks for generated docstrings."""
    issues: list[str] = []
    if not docstring or not docstring.strip():
        return False, ["Empty docstring"]

    if "```" in docstring:
        issues.append("Docstring contains code fences (```), expected plain text")
    if "`" in docstring:
        # prompts ask for no backticks; keep this as a soft issue
        issues.append("Docstring contains backticks (`), expected none")

    params = _parse_python_params_from_signature(signature)
    lower = docstring.lower()
    mentions_args_section = ("args:" in lower) or ("parameters" in lower)
    if params and mentions_args_section:
        # If the model chooses to include an args/parameters section, it should not invent names.
        invented: list[str] = []
        for line in docstring.splitlines():
            m = re.match(r"^\s*[-*]?\s*([A-Za-z_]\w*)\s*:", line)
            if not m:
                continue
            name = m.group(1)
            if name not in params:
                invented.append(name)
        if invented:
            issues.append(f"Docstring mentions parameter(s) not in signature: {sorted(set(invented))}")

    # Missing-params is a soft check: encourage mentioning params when present.
    if params and not any(p in docstring for p in params):
        issues.append("Docstring does not mention any parameter names from the signature")

    ok = len(issues) == 0
    return ok, issues


def validate_code_example_syntax(code: str) -> tuple[bool, list[str]]:
    """
    Validate code example syntax using AST parser.
    
    This is Stage 1 validation - fast and definitive.
    
    Args:
        code: The code example to validate
        
    Returns:
        Tuple of (is_valid, list of issues)
    """
    import ast
    
    issues: list[str] = []
    
    if not code or not code.strip():
        return False, ["Empty code example"]
    
    # Clean up common LLM artifacts
    code = code.strip()
    
    # Remove markdown code blocks if present
    if code.startswith("```"):
        lines = code.split("\n")
        # Remove first line (```python or ```)
        lines = lines[1:]
        # Remove last line if it's closing ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        code = "\n".join(lines)
    
    # Try to parse
    try:
        ast.parse(code)
    except SyntaxError as e:
        line_info = f" (line {e.lineno})" if e.lineno else ""
        issues.append(f"Syntax error{line_info}: {e.msg}")
        return False, issues
    
    return True, []


def validate_code_example_basic(code: str, function_name: str) -> tuple[bool, list[str]]:
    """
    Basic validation checks for code example (before LLM validation).
    
    Args:
        code: The code example to validate
        function_name: The function being documented
        
    Returns:
        Tuple of (is_valid, list of issues)
    """
    issues: list[str] = []
    
    # Check if it references the function
    if function_name not in code:
        issues.append(f"Example doesn't reference '{function_name}'")
    
    # Check for obvious test artifacts
    test_artifacts = [
        ("assert ", "Contains 'assert' statement"),
        ("pytest", "Contains pytest reference"),
        ("unittest", "Contains unittest reference"),
        ("Mock(", "Contains Mock() call"),
        ("@patch", "Contains @patch decorator"),
        ("@pytest", "Contains @pytest decorator"),
    ]
    
    for artifact, message in test_artifacts:
        if artifact in code:
            issues.append(message)
    
    return len(issues) == 0, issues


