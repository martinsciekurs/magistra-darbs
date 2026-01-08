#!/usr/bin/env python3
"""Fetch a git repository or local directory into .docs/<normalized_name>/repo"""

import re
import shutil
import subprocess
from pathlib import Path
from docgen.utils.logger import setup_logger

logger = setup_logger()


def normalize_repo_name(raw_source: str) -> str:
    """Extract and normalize repository name from URL or path.

    Args:
        raw_source: Repository URL or local path

    Returns:
        Normalized repository name (lowercase, special chars replaced with underscores)
    """
    path = Path(raw_source)
    if path.exists():
        path_name = path.resolve().name
    else:
        raw_source = raw_source.rstrip("/").removesuffix(".git")
        path_name = raw_source.split("/")[-1]
    return re.sub(r"[^a-z0-9]+", "_", path_name.lower()).strip("_")


def fetch_repo(source: str, commit: str | None = None) -> tuple[Path, str]:
    """Clone repo or copy local dir into .docs/<normalized_name>/repo, overwriting if exists.

    Args:
        source: Repository URL or local path
        commit: Optional commit SHA, tag, or branch to checkout. If provided, fetches
                full history to ensure the commit is available.

    Returns:
        Tuple of (repo_path, normalized_repo_name)
    """
    name = normalize_repo_name(source)
    target = Path(".docs") / name / "repo"

    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)

    from docgen.utils.logger import step, success, dim
    step("Fetching repository")

    # If commit is specified, we need full history to checkout that commit
    # Otherwise use shallow clone for speed
    clone_args = ["git", "clone"]
    if not commit:
        clone_args.append("--depth")
        clone_args.append("1")

    if Path(source).is_dir():
        source_path = Path(source).resolve()
        clone_args.append(f"file://{source_path}")
    else:
        clone_args.append(source)

    clone_args.append(str(target))

    subprocess.run(
        clone_args,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Checkout specific commit if provided
    if commit:
        dim(f"  Checking out: {commit}")
        subprocess.run(
            ["git", "checkout", commit],
            cwd=target,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Get the actual commit SHA for display
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=target,
            capture_output=True,
            text=True
        )
        short_sha = result.stdout.strip() if result.returncode == 0 else commit
        success(f"Repository ready at {target} (commit: {short_sha})")
    else:
        success(f"Repository ready at {target}")

    return target, name
