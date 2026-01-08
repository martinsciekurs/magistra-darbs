"""Code parser using tree-sitter for AST extraction."""

from typing import Dict, Any
from importlib.resources import files
import tree_sitter_language_pack
import tree_sitter

QUERY_FILES = {"python": "python.scm", "ruby": "ruby.scm"}


def load_query(language_name: str) -> str:
    if language_name not in QUERY_FILES:
        raise ValueError(f"Language {language_name} is not supported.")
    try:
        return files("docgen.analyzer.queries").joinpath(QUERY_FILES[language_name]).read_text()
    except Exception as e:
        raise RuntimeError(f"Could not load query file for {language_name}") from e


class CodeParser:
    def __init__(self, lang: str):
        self.lang_name = lang
        self.query_scm = load_query(lang)
        self.parser = tree_sitter_language_pack.get_parser(lang)
        self.language = tree_sitter_language_pack.get_language(lang)
        self.query = self.language.query(self.query_scm)

    def parse_file(self, code: str, file_name: str = "") -> Dict[str, Any]:
        """Parse code and return imports and functions with node_ids."""
        code_bytes = bytes(code, "utf8")
        tree = self.parser.parse(code_bytes)

        cursor = tree_sitter.QueryCursor(self.query)
        matches = cursor.matches(tree.root_node)

        # Collect all captures
        captures = []
        for _, match_dict in matches:
            for tag, nodes in match_dict.items():
                for node in nodes:
                    captures.append((node, tag))
        captures.sort(key=lambda x: x[0].start_byte)

        imports = self._extract_imports(captures, code_bytes)
        functions = self._extract_functions(captures, code_bytes, file_name)

        return {"imports": imports, "functions": functions}

    def _extract_imports(self, captures: list, code_bytes: bytes) -> list[dict]:
        """Extract import statements from captures."""
        imports = []
        current_from_module = None  # Track "from X" module for subsequent names
        pending_module_import = None  # Track "import X" style imports

        for node, tag in captures:
            text = code_bytes[node.start_byte:node.end_byte].decode("utf8")

            if tag == "import.module":
                # "import X" style - save pending and start new
                if pending_module_import:
                    imports.append(pending_module_import)
                current_from_module = None
                pending_module_import = {"module": text, "name": None, "alias": None}

            elif tag == "import.alias" and pending_module_import:
                pending_module_import["alias"] = text

            elif tag == "import.from":
                # "from X import ..." - just remember the module
                if pending_module_import:
                    imports.append(pending_module_import)
                    pending_module_import = None
                current_from_module = text

            elif tag == "import.name" and current_from_module:
                # "from X import Y" - create entry for each name
                imports.append({"module": current_from_module, "name": text, "alias": None})

        # Don't forget last pending "import X"
        if pending_module_import:
            imports.append(pending_module_import)

        return imports

    def _extract_functions(self, captures: list, code_bytes: bytes, file_name: str) -> list[dict]:
        """Extract function definitions with metadata (decorators, raises, visibility)."""
        functions_map = {}

        for node, tag in captures:
            if tag == "func.def":
                start_line = node.start_point[0] + 1
                end_line = node.end_point[0] + 1
                class_name = self._find_parent_class(node)
                code = code_bytes[node.start_byte:node.end_byte].decode("utf8")
                
                # Extract decorators, signature, raises, visibility
                decorators = self._extract_decorators(node, code_bytes)
                signature = self._extract_full_signature(node, code_bytes)
                raises = self._extract_raises(code)
                
                functions_map[node.id] = {
                    "name": "anonymous",
                    "start_line": start_line,
                    "end_line": end_line,
                    "code": code,
                    "signature": signature,
                    "decorators": decorators,
                    "raises": raises,
                    "calls": [],
                    "_class_name": class_name,
                }
            elif tag in ("func.name", "func.call", "func.call.qualified"):
                parent_id = self._find_parent_id(node, functions_map)
                if parent_id:
                    text = code_bytes[node.start_byte:node.end_byte].decode("utf8")
                    if tag == "func.name":
                        functions_map[parent_id]["name"] = text
                        # Set visibility based on name
                        functions_map[parent_id]["visibility"] = (
                            "private" if text.startswith("__") and not text.endswith("__")
                            else "protected" if text.startswith("_")
                            else "public"
                        )
                    elif text not in functions_map[parent_id]["calls"]:
                        functions_map[parent_id]["calls"].append(text)

        results = list(functions_map.values())
        for func in results:
            class_name = func.pop("_class_name", None)
            if class_name:
                func["node_id"] = f"{file_name}::{class_name}.{func['name']}" if file_name else f"{class_name}.{func['name']}"
            else:
                func["node_id"] = f"{file_name}::{func['name']}" if file_name else func["name"]
        results.sort(key=lambda x: x["start_line"])
        return results

    def _extract_decorators(self, func_node, code_bytes: bytes) -> list[str]:
        """Extract decorator names from function node."""
        decorators = []
        # Look at previous siblings for decorators
        prev = func_node.prev_sibling
        while prev:
            if prev.type == "decorator":
                dec_text = code_bytes[prev.start_byte:prev.end_byte].decode("utf8").strip()
                decorators.insert(0, dec_text)
                prev = prev.prev_sibling
            else:
                break
        return decorators

    def _extract_full_signature(self, func_node, code_bytes: bytes) -> str:
        """Extract full function signature including return type."""
        # Find the parameters and return_type nodes
        params_text = ""
        return_type = ""
        func_name = ""
        
        for child in func_node.children:
            if child.type == "identifier":
                func_name = code_bytes[child.start_byte:child.end_byte].decode("utf8")
            elif child.type == "parameters":
                params_text = code_bytes[child.start_byte:child.end_byte].decode("utf8")
            elif child.type == "type":
                return_type = code_bytes[child.start_byte:child.end_byte].decode("utf8")
        
        sig = f"def {func_name}{params_text}"
        if return_type:
            sig += f" -> {return_type}"
        return sig

    def _extract_raises(self, code: str) -> list[str]:
        """Extract exception types from raise statements."""
        import re
        raises = []
        for match in re.finditer(r'\braise\s+([A-Z][A-Za-z0-9_]*)', code):
            exc = match.group(1)
            if exc not in raises:
                raises.append(exc)
        return raises

    def _find_parent_id(self, child_node, functions_map) -> int | None:
        """Walk up AST to find closest parent function definition."""
        curr = child_node.parent
        while curr:
            if curr.id in functions_map:
                return curr.id
            curr = curr.parent
        return None
    
    def _find_parent_class(self, node) -> str | None:
        """Walk up AST to find parent class definition and return its name."""
        curr = node.parent
        while curr:
            if curr.type == "class_definition":
                # Find the class name (first identifier child)
                for child in curr.children:
                    if child.type == "identifier":
                        return child.text.decode("utf8") if isinstance(child.text, bytes) else child.text
            curr = curr.parent
        return None