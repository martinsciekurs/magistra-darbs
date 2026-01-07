"""Utility functions for DocGen."""

import os
import yaml

# Import logging utilities (backward compatibility)
from .logger import step, success, info, warning, dim, header, error

__all__ = ['step', 'success', 'info', 'warning', 'dim', 'header', 'error', 'map_language_name', 'save_yaml', 'load_yaml']


def map_language_name(linguist_name: str) -> str | None:
    """Map github-linguist language names to CodeParser language names."""
    mapping = {"Python": "python", "Ruby": "ruby",}
    return mapping.get(linguist_name)


def load_yaml(repo_name: str, filename: str) -> dict | list | None:
    """Load data from a YAML file in the documentation directory.

    Args:
        repo_name: Name of the repository
        filename: Name of the file to load

    Returns:
        Loaded data (dict or list), or None if file doesn't exist
    """
    filepath = os.path.join(".docs", repo_name, filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


def save_yaml(repo_name: str, filename: str, data: dict | list, plain_text: bool = False) -> str:
    """Save data to a YAML file in the documentation directory.
    
    Args:
        repo_name: Name of the repository
        filename: Name of the output file
        data: Data to save (dict or list)
        plain_text: If True and data is a list of strings, save as plain text (one per line)
        
    Returns:
        Path to the saved file
    """
    docs_dir = os.path.join(".docs", repo_name)
    os.makedirs(docs_dir, exist_ok=True)
    output_path = os.path.join(docs_dir, filename)
    with open(output_path, "w") as f:
        if plain_text and isinstance(data, list) and all(isinstance(item, str) for item in data):
            f.write("\n".join(data) + "\n")
        else:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    return output_path




