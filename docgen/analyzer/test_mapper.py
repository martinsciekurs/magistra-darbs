"""Test mapper - discovers test files and maps them to functions they test."""

import re
import yaml
from pathlib import Path

from docgen.analyzer.code_parser import CodeParser


def _is_in_test_directory(file_path: Path) -> bool:
    """Check if a file is inside a tests/ or test/ directory."""
    parts = file_path.parts
    return "tests" in parts or "test" in parts


def _contains_test_functions(file_path: Path) -> bool:
    """Check if a file contains actual pytest test functions (def test_...)."""
    try:
        content = file_path.read_text(encoding="utf-8")
        # Look for function definitions starting with test_
        return bool(re.search(r'^\s*def\s+test_', content, re.MULTILINE))
    except Exception:
        return False


def find_test_files(repo_path: Path) -> list[Path]:
    """
    Find all test files in the repository.
    
    Args:
        repo_path: Path to the repository root
        
    Returns:
        List of test file paths
    """
    # Files in test directories are always considered test files
    test_dir_patterns = [
        "**/tests/**/*.py",
        "**/test/**/*.py",
    ]
    
    # Files matching test naming patterns need verification
    # (they might be utility modules like test_mapper.py)
    test_name_patterns = [
        "**/test_*.py",
        "**/*_test.py",
    ]
    
    test_files = set()
    
    # Add all files from test directories
    for pattern in test_dir_patterns:
        test_files.update(repo_path.glob(pattern))
    
    # Add files matching naming patterns only if they contain test functions
    # or are already in a test directory
    for pattern in test_name_patterns:
        for f in repo_path.glob(pattern):
            if _is_in_test_directory(f) or _contains_test_functions(f):
                test_files.add(f)
    
    # Filter out __init__.py, conftest.py, and other non-test files
    excluded_names = {"__init__.py", "conftest.py", "setup.py"}
    test_files = [
        f for f in test_files 
        if f.name not in excluded_names and f.is_file()
    ]
    
    return sorted(test_files)


def _extract_calls_and_imports(parser: CodeParser, content: str) -> set[str]:
    """
    Extract all function calls and imported names from a file using tree-sitter.
    
    Returns a set of function/method names that are called or imported.
    """
    referenced_names = set()
    
    try:
        parsed = parser.parse_file(content)
        
        # Collect imported names (from x import name)
        for imp in parsed.get("imports", []):
            if imp.get("name"):
                # "from module import name" - add the name
                referenced_names.add(imp["name"])
            elif imp.get("module"):
                # "import module" - add the module name parts
                # e.g., "import foo.bar" -> add "foo", "bar"
                for part in imp["module"].split("."):
                    referenced_names.add(part)
        
        # Collect all function calls from all functions in the file
        for func in parsed.get("functions", []):
            for call in func.get("calls", []):
                # call can be "func_name" or "obj.method_name"
                # Extract the actual function/method name
                if "." in call:
                    # obj.method -> method
                    referenced_names.add(call.split(".")[-1])
                else:
                    referenced_names.add(call)
                    
    except Exception:
        pass
    
    return referenced_names


# Dunder methods that are too common to be meaningful for test mapping
_EXCLUDED_DUNDER_METHODS = {
    "__init__", "__new__", "__del__",
    "__str__", "__repr__", "__format__",
    "__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__", "__hash__",
    "__bool__", "__len__", "__iter__", "__next__", "__contains__",
    "__getitem__", "__setitem__", "__delitem__",
    "__getattr__", "__setattr__", "__delattr__",
    "__call__", "__enter__", "__exit__",
    "__add__", "__sub__", "__mul__", "__truediv__",
}


def build_test_mapping(
    repo_path: Path,
    known_functions: set[str],
) -> dict[str, list[str]]:
    """
    Build mapping of function node_id -> test files that reference them.
    
    Uses tree-sitter AST parsing for accurate detection:
    1. Function is called: func_name() or obj.func_name()
    2. Function is imported: from x import func_name
    
    Args:
        repo_path: Path to the repository root
        known_functions: Set of function node_ids from extraction
        
    Returns:
        Dict mapping function_node_id -> list of test file paths (relative)
    """
    mapping: dict[str, list[str]] = {}
    test_files = find_test_files(repo_path)
    
    if not test_files:
        return mapping
    
    # Initialize parser for Python
    parser = CodeParser("python")
    
    # Build lookup: function_name -> [node_ids]
    # Handles both "file.py::func" and "file.py::Class.method"
    name_to_nodes: dict[str, list[str]] = {}
    for node_id in known_functions:
        if "::" in node_id:
            # Extract function/method name
            func_part = node_id.split("::")[-1]
            # Handle Class.method -> method
            func_name = func_part.split(".")[-1]
            
            # Skip dunder methods - they're too common to match meaningfully
            if func_name in _EXCLUDED_DUNDER_METHODS:
                continue
                
            name_to_nodes.setdefault(func_name, []).append(node_id)
    
    for test_file in test_files:
        try:
            content = test_file.read_text(encoding="utf-8")
            rel_path = str(test_file.relative_to(repo_path))
            
            # Parse with tree-sitter to get actual calls and imports
            referenced_names = _extract_calls_and_imports(parser, content)
            
            # Match against known functions
            for func_name, node_ids in name_to_nodes.items():
                # Skip very short names (too many false positives)
                if len(func_name) < 4:
                    continue
                
                # Check if this function is actually referenced in the test file
                if func_name in referenced_names:
                    for node_id in node_ids:
                        mapping.setdefault(node_id, [])
                        if rel_path not in mapping[node_id]:
                            mapping[node_id].append(rel_path)
                            
        except Exception:
            # Skip files that can't be parsed
            continue
    
    return mapping


def generate_test_mapping_file(
    repo_name: str,
    repo_path: Path,
    docs_base_dir: str = ".docs",
) -> dict[str, list[str]]:
    """
    Generate test mapping YAML file from node extraction.
    
    Args:
        repo_name: Name of the repository
        repo_path: Path to the repository root
        docs_base_dir: Base directory for docs output
        
    Returns:
        The generated test mapping dict
    """
    extraction_file = Path(docs_base_dir) / repo_name / "2_node_extraction.yaml"
    
    if not extraction_file.exists():
        return {}
    
    # Load extracted functions
    with open(extraction_file, "r", encoding="utf-8") as f:
        extracted = yaml.safe_load(f) or []
    
    # Build set of known function node_ids
    known_functions: set[str] = set()
    for file_entry in extracted:
        for func in file_entry.get("functions", []):
            if "node_id" in func:
                known_functions.add(func["node_id"])
    
    # Build mapping
    test_mapping = build_test_mapping(repo_path, known_functions)
    
    # Save to file
    if test_mapping:
        mapping_file = Path(docs_base_dir) / repo_name / "2b_test_mapping.yaml"
        with open(mapping_file, "w", encoding="utf-8") as f:
            yaml.dump(test_mapping, f, default_flow_style=False, allow_unicode=True)
    
    return test_mapping


def load_test_mapping(repo_name: str, docs_base_dir: str = ".docs") -> dict[str, list[str]]:
    """
    Load test mapping from YAML file.
    
    Args:
        repo_name: Name of the repository
        docs_base_dir: Base directory for docs
        
    Returns:
        Test mapping dict, or empty dict if file doesn't exist
    """
    mapping_file = Path(docs_base_dir) / repo_name / "2b_test_mapping.yaml"
    
    if not mapping_file.exists():
        return {}
    
    with open(mapping_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

