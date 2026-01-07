"""Documentation generator for hierarchical documentation pipeline."""

import os
import re
from pathlib import Path


def load_repo_analysis(repo_name: str) -> str:
    """
    Load repository analysis YAML file and return as string.
    
    Args:
        repo_name: Name of the repository
        
    Returns:
        YAML string containing repo analysis (summary + modules)
        
    Raises:
        FileNotFoundError: If the analysis file doesn't exist
    """
    analysis_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
    
    if not analysis_path.exists():
        raise FileNotFoundError(f"Repository analysis not found at {analysis_path}")
    
    return analysis_path.read_text(encoding="utf-8")


def _build_function_lookup(extracted_code_elements: list[dict]) -> dict[str, dict]:
    """
    Build a dictionary for fast function lookup by node_id.
    
    Args:
        extracted_code_elements: List of file dicts from 2_node_extraction.yaml
        
    Returns:
        Dict mapping node_id -> function dict (with file_name added)
    """
    lookup = {}
    for extracted_element in extracted_code_elements:
        file_name = extracted_element["file_name"]
        for func in extracted_element.get("functions", []):
            node_id = func["node_id"]
            # Add file_name to function data for convenience
            func_with_file = func.copy()
            func_with_file["file_name"] = file_name
            lookup[node_id] = func_with_file
    return lookup


def _get_file_imports(extracted_code_elements: list[dict], file_name: str) -> list[dict]:
    """
    Get imports for a specific file.
    
    Args:
        extracted_code_elements: List of file dicts from 2_node_extraction.yaml
        file_name: Name of the file to find imports for
        
    Returns:
        List of import dicts
    """
    for extracted_element in extracted_code_elements:
        if extracted_element["file_name"] == file_name:
            return extracted_element.get("imports", [])
    return []


def _get_dependency_docs(
    node_id: str,
    function: dict,
    generated_docs: dict[str, dict],
    extracted_code_elements: list[dict]
) -> list[dict]:
    """
    Get documentation for functions that the current function depends on.
    
    Args:
        node_id: ID of the current function
        function: The function dict
        generated_docs: Dictionary of already generated docs
        extracted_code_elements: List of file dicts for lookup
        
    Returns:
        List of dependency documentation dicts
    """
    dependency_docs = []
    
    for call in function.get("calls", []):
        if call.get("type") == "internal":
            target = call["target"]
            if target in generated_docs:
                dep_doc = generated_docs[target]
                dependency_docs.append({
                    "node_id": target,
                    "name": dep_doc.get("name", ""),
                    "signature": dep_doc.get("signature", ""),
                    "docstring": dep_doc.get("docstring", "")
                })
    
    return dependency_docs


def _get_similar_function_docs(
    similar_functions: list[dict],
    generated_docs: dict[str, dict]
) -> list[dict]:
    """
    Get documentation for similar functions (from RAG).
    
    Args:
        similar_functions: List of similar function dicts from get_similar()
        generated_docs: Dictionary of already-generated docs (node_id -> doc entry)
        
    Returns:
        List of dicts with similar function documentation
    """
    similar_docs = []
    
    for similar in similar_functions:
        node_id = similar["node_id"]
        # Extract signature from code
        signature = _extract_signature_from_code(similar.get("code", ""))
        
        # Get docstring if already documented
        docstring = ""
        if node_id in generated_docs:
            docstring = generated_docs[node_id].get("docstring", "")
        
        similar_docs.append({
            "node_id": node_id,
            "file": similar.get("file", ""),
            "name": similar.get("name", ""),
            "signature": signature,
            "docstring": docstring,
            "code": similar.get("code", "")[:200]  # First 200 chars for context
        })
    
    return similar_docs


def _extract_signature_from_code(code: str) -> str:
    """
    Extract function signature (first line) from function code.
    
    Args:
        code: Full function source code
        
    Returns:
        Function signature string (first line, stripped)
    """
    if not code:
        return ""
    
    lines = code.strip().split("\n")
    if lines:
        return lines[0].strip()
    return ""


def extract_relevant_file_context(
    file_source: str,
    start_line: int | None = None,
    end_line: int | None = None,
    *,
    max_chars: int = 6000,
    context_lines: int = 35,
) -> str:
    """Extract a small, relevant subset of file context for LLM prompting.

    Goal: avoid feeding the full file (costly + noisy) while still providing:
    - imports
    - top-level constants/config
    - nearby lines around the target definition
    """
    if not file_source:
        return ""

    lines = file_source.splitlines()

    # Imports and top-level constants are often useful.
    import_lines: list[str] = []
    const_lines: list[str] = []
    for i, line in enumerate(lines[:300]):  # cap scan
        s = line.strip()
        if s.startswith("import ") or s.startswith("from "):
            import_lines.append(line)
            continue
        # Heuristic: ALL_CAPS assignments near the top are likely config/constants
        if i < 200 and s and not s.startswith("#"):
            if s[:1].isupper() and "=" in s and "==" not in s:
                const_lines.append(line)

    nearby: list[str] = []
    if start_line and start_line > 0:
        # your analyzer is 1-based; convert to 0-based indices
        start_idx = max(0, start_line - 1 - context_lines)
        end_idx = min(len(lines), (end_line or start_line) - 1 + context_lines)
        snippet = lines[start_idx:end_idx]
        nearby = [f"{start_idx+1+i}: {l}" for i, l in enumerate(snippet)]

    parts: list[str] = []
    if import_lines:
        parts.append("Imports:\n" + "\n".join(import_lines))
    if const_lines:
        parts.append("Top-level constants/config:\n" + "\n".join(const_lines))
    if nearby:
        parts.append("Nearby code (line-numbered):\n" + "\n".join(nearby))

    out = "\n\n".join(parts).strip()
    if len(out) > max_chars:
        out = out[:max_chars] + "\n...[truncated]"
    return out


def _group_functions_by_class(function_docs: list[dict]) -> dict[str, list[dict]]:
    """
    Group functions by class based on node_id pattern.
    
    Pattern: file.py::ClassName.method_name -> class is file.py::ClassName
    
    Args:
        function_docs: List of documented function dicts
        
    Returns:
        Dictionary mapping class_id -> list of method dicts
    """
    classes = {}
    standalone_functions = []
    
    for func_doc in function_docs:
        node_id = func_doc["node_id"]
        # Check if it's a method (has ::ClassName.method pattern)
        # Pattern: file.py::ClassName.method_name
        match = re.match(r"^(.+::[^.]+)\.(.+)$", node_id)
        
        if match:
            class_id = match.group(1)  # file.py::ClassName
            method_name = match.group(2)  # method_name
            
            if class_id not in classes:
                classes[class_id] = []
            
            classes[class_id].append(func_doc)
        else:
            # Standalone function (not a method)
            standalone_functions.append(func_doc)
    
    return classes


def _group_by_file(items: list[dict], key_field: str = "file") -> dict[str, list[dict]]:
    """
    Group items by file name.
    
    Args:
        items: List of dicts with a file field
        key_field: Name of the field containing the file name (default: "file")
        
    Returns:
        Dictionary mapping file_name -> list of items
    """
    grouped = {}
    
    for item in items:
        file_name = item.get(key_field)
        if file_name:
            if file_name not in grouped:
                grouped[file_name] = []
            grouped[file_name].append(item)
    
    return grouped


def _format_imports(imports: list[dict]) -> str:
    """
    Format imports list as a readable string.
    
    Args:
        imports: List of import dicts with module, name, alias fields
        
    Returns:
        Formatted string representation, or empty string if no imports
    """
    if not imports:
        return ""
    
    lines = []
    for imp in imports:
        if isinstance(imp, dict):
            module = imp.get("module", "")
            name = imp.get("name")
            alias = imp.get("alias")
            
            if name:
                # "from X import Y" style
                line = f"from {module} import {name}"
                if alias:
                    line += f" as {alias}"
            else:
                # "import X" style
                line = f"import {module}"
                if alias:
                    line += f" as {alias}"
            lines.append(f"  {line}")
        else:
            lines.append(f"  {imp}")
    
    return "\n".join(lines) if lines else ""


def _format_called_by(called_by: list[dict]) -> str:
    """Format called_by list as a readable string."""
    if not called_by:
        return ""
    
    callers = []
    for caller in called_by:
        if isinstance(caller, dict):
            source = caller.get("source", "")
            if source:
                callers.append(f"  - {source}")
        else:
            callers.append(f"  - {caller}")
    
    return "\n".join(callers) if callers else ""


def _extract_usage_snippets(
    function_name: str,
    called_by: list[dict],
    func_lookup: dict[str, dict],
    max_snippets: int = 2,
) -> list[str]:
    """Extract real usage snippets from caller functions.
    
    Args:
        function_name: Name of the function being documented
        called_by: List of caller dicts with 'source' keys
        func_lookup: Dict mapping node_id -> function dict
        max_snippets: Maximum number of snippets to extract
        
    Returns:
        List of usage snippet strings
    """
    snippets = []
    
    for caller in called_by[:max_snippets * 2]:  # Check more than we need
        if len(snippets) >= max_snippets:
            break
            
        source = caller.get("source", "") if isinstance(caller, dict) else str(caller)
        if not source or source not in func_lookup:
            continue
        
        caller_func = func_lookup[source]
        caller_code = caller_func.get("code", "")
        if not caller_code:
            continue
        
        # Find lines that call the function
        for line in caller_code.split("\n"):
            if function_name in line and "def " not in line:
                snippet = line.strip()
                if len(snippet) < 120 and snippet not in snippets:
                    snippets.append(snippet)
                    break
    
    return snippets
