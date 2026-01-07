#!/usr/bin/env python3
"""
Generate Docusaurus markdown files from YAML documentation.

Reads the generated YAML docs and creates markdown files in .docs/{repo_name}/docs-site/docs folder.
"""

import argparse
import os
import re
import yaml
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def clean_docstring(docstring: str) -> str:
    """Clean up docstring for markdown display.
    
    Handles MDX expression parsing by escaping problematic characters
    that could be interpreted as JSX or JavaScript expressions.
    """
    if not docstring:
        return ""
    # Remove wrapping code blocks if present
    docstring = re.sub(r'^```python\s*', '', docstring)
    docstring = re.sub(r'\s*```$', '', docstring)
    # Remove wrapping triple quotes
    docstring = re.sub(r'^"""?\s*', '', docstring)
    docstring = re.sub(r'\s*"""?$', '', docstring)
    
    # IMPORTANT: Order matters - escape backslashes first to avoid double-escaping
    # Escape curly braces (JSX expressions) - must use HTML entities for MDX
    docstring = docstring.replace('{', '&#123;').replace('}', '&#125;')
    # Escape all angle brackets to prevent MDX treating them as JSX
    docstring = docstring.replace('<', '&lt;').replace('>', '&gt;')
    # Escape dollar signs that might be interpreted as expressions
    docstring = docstring.replace('$', '&#36;')
    
    return docstring.strip()


def escape_markdown(text: str) -> str:
    """Escape special markdown characters in inline text."""
    # Only escape pipe characters in tables
    return text.replace('|', '\\|')


def generate_index(repo_name: str, modules: list[dict], synthesis: dict | None, output_dir: Path):
    """Generate the index/overview page."""
    # Use synthesis intro if available
    intro_text = f"Auto-generated documentation for the **{repo_name}** codebase."
    
    # Check for dynamic TOC format first
    is_dynamic = synthesis and (synthesis.get('is_dynamic', False) or 'sections' in synthesis)
    
    if is_dynamic and synthesis.get('sections'):
        # Find introduction section in dynamic TOC
        intro_section = next(
            (s for s in synthesis.get('sections', []) if s.get('slug') in ['introduction', 'overview']),
            None
        )
        if intro_section:
            intro_text = clean_docstring(intro_section.get('content', '')[:500] + '...')
    elif synthesis and synthesis.get('introduction'):
        intro_text = clean_docstring(synthesis['introduction'])
    
    content = f"""---
sidebar_position: 1
slug: /
---

# {repo_name} Documentation

{intro_text}

"""
    
    # Add navigation (Guide first!)
    content += """## Navigation

- **[Guide](guide/)** - Introduction, Quick Start, and How-To guides
- **[Modules](modules/)** - High-level architectural components
- **[Files](files/)** - File-level documentation  
- **[API Reference](api/)** - Classes and functions

"""
    
    # Add modules overview
    content += """## Modules

This codebase is organized into the following architectural modules:

"""
    for module in modules:
        name = module.get('module', 'Unknown')
        desc = module.get('description', '')
        slug = slugify(name)
        content += f"### [{name}](modules/{slug})\n\n{desc}\n\n"
    
    (output_dir / 'index.md').write_text(content)
    print(f"  ✓ Generated index.md")


def generate_guide(synthesis: dict | None, repo_name: str, output_dir: Path, architecture_diagram: dict | None = None):
    """Generate guide pages from synthesis documentation.
    
    Supports both dynamic TOC (synthesis['sections']) and legacy fixed structure.
    Optionally includes Mermaid architecture diagram if provided.
    """
    guide_dir = output_dir / 'guide'
    guide_dir.mkdir(parents=True, exist_ok=True)
    
    if not synthesis:
        # Create placeholder
        content = f"""---
sidebar_position: 1
---

# {repo_name} Guide

Run the documentation pipeline to generate the full guide.
"""
        (guide_dir / 'index.md').write_text(content)
        print(f"  ✓ Generated 1 guide page (placeholder)")
        return
    
    pages_generated = 0
    
    # Check if this is dynamic TOC format
    is_dynamic = synthesis.get('is_dynamic', False) or 'sections' in synthesis
    
    if is_dynamic and synthesis.get('sections'):
        # Dynamic TOC: generate pages from sections list
        sections = synthesis.get('sections', [])
        
        # Build section links for index
        section_links = []
        for section in sections:
            slug = section.get('slug', '')
            title = section.get('title', slug.replace('-', ' ').title())
            section_links.append(f"- [{title}]({slug})")
        
        # Guide index
        guide_index = f"""---
sidebar_position: 1
---

# {repo_name} Guide

Welcome to the {repo_name} documentation guide.

## Sections

{chr(10).join(section_links)}
"""
        (guide_dir / 'index.md').write_text(guide_index)
        pages_generated += 1
        
        # Generate each section page
        for i, section in enumerate(sections):
            slug = section.get('slug', f'section-{i}')
            title = section.get('title', slug.replace('-', ' ').title())
            content_text = clean_docstring(section.get('content', ''))
            
            if content_text:
                page_content = f"""---
sidebar_position: {i + 2}
---

# {title}

{content_text}
"""
                # Add Mermaid diagram to architecture section if available
                if slug == 'architecture' and architecture_diagram:
                    mermaid_code = architecture_diagram.get('mermaid', '')
                    components = architecture_diagram.get('components', [])
                    if mermaid_code:
                        page_content += f"""
## System Diagram

```mermaid
{mermaid_code}
```

"""
                    if components:
                        page_content += "## Components\n\n"
                        for comp in components:
                            comp_name = comp.get('name', comp.get('id', 'Unknown'))
                            comp_desc = comp.get('description', '')
                            page_content += f"**{comp_name}**: {comp_desc}\n\n"
                
                (guide_dir / f'{slug}.md').write_text(page_content)
                pages_generated += 1
        
        print(f"  ✓ Generated {pages_generated} guide pages (dynamic TOC)")
        return
    
    # Legacy fixed structure (backward compatibility)
    # Guide index
    guide_index = f"""---
sidebar_position: 1
---

# {repo_name} Guide

Welcome to the {repo_name} documentation guide.

## Sections

- [Introduction](introduction) - What is {repo_name}?
- [Why {repo_name}](why) - Motivation and benefits
- [Quick Start](quick-start) - Get started in minutes
- [Architecture](architecture) - How it works
- [Key Concepts](key-concepts) - Core terminology
- [How-To Guides](how-to) - Common tasks
"""
    (guide_dir / 'index.md').write_text(guide_index)
    pages_generated += 1
    
    # Introduction page
    intro = clean_docstring(synthesis.get('introduction', ''))
    if intro:
        content = f"""---
sidebar_position: 2
---

# Introduction

{intro}
"""
        (guide_dir / 'introduction.md').write_text(content)
        pages_generated += 1
    
    # Why page
    why = clean_docstring(synthesis.get('why', ''))
    if why:
        content = f"""---
sidebar_position: 3
---

# Why {repo_name}?

{why}
"""
        (guide_dir / 'why.md').write_text(content)
        pages_generated += 1
    
    # Quick Start page
    quick_start = clean_docstring(synthesis.get('quick_start', ''))
    if quick_start:
        content = f"""---
sidebar_position: 4
---

# Quick Start

{quick_start}
"""
        (guide_dir / 'quick-start.md').write_text(content)
        pages_generated += 1
    
    # Architecture page
    architecture = clean_docstring(synthesis.get('architecture', ''))
    if architecture:
        content = f"""---
sidebar_position: 5
---

# Architecture

{architecture}
"""
        # Add Mermaid diagram if available
        if architecture_diagram:
            mermaid_code = architecture_diagram.get('mermaid', '')
            components = architecture_diagram.get('components', [])
            if mermaid_code:
                content += f"""
## System Diagram

```mermaid
{mermaid_code}
```

"""
            if components:
                content += "## Components\n\n"
                for comp in components:
                    comp_name = comp.get('name', comp.get('id', 'Unknown'))
                    comp_desc = comp.get('description', '')
                    content += f"**{comp_name}**: {comp_desc}\n\n"
        
        (guide_dir / 'architecture.md').write_text(content)
        pages_generated += 1
    
    # Key Concepts page
    key_concepts = clean_docstring(synthesis.get('key_concepts', ''))
    if key_concepts:
        content = f"""---
sidebar_position: 6
---

# Key Concepts

{key_concepts}
"""
        (guide_dir / 'key-concepts.md').write_text(content)
        pages_generated += 1
    
    # How-To Guides page
    how_to_guides = synthesis.get('how_to_guides', [])
    if how_to_guides:
        content = f"""---
sidebar_position: 7
---

# How-To Guides

"""
        for i, guide in enumerate(how_to_guides):
            title = guide.get('title', f'Guide {i+1}')
            guide_content = clean_docstring(guide.get('content', ''))
            content += f"## {title}\n\n{guide_content}\n\n"
        
        (guide_dir / 'how-to.md').write_text(content)
        pages_generated += 1
    
    print(f"  ✓ Generated {pages_generated} guide pages")


def generate_modules(modules: list[dict], output_dir: Path):
    """Generate module documentation pages."""
    modules_dir = output_dir / 'modules'
    modules_dir.mkdir(parents=True, exist_ok=True)
    
    for i, module in enumerate(modules):
        name = module.get('module', 'Unknown')
        description = module.get('description', '')
        docstring = clean_docstring(module.get('docstring', ''))
        files = module.get('files', [])
        
        slug = slugify(name)
        
        content = f"""---
sidebar_position: {i + 1}
---

# {name}

{description}

## Overview

{docstring}

## Files in this Module

"""
        for file in files:
            file_slug = slugify(file.replace('/', '-').replace('.py', ''))
            content += f"- [`{file}`](../files/{file_slug})\n"
        
        (modules_dir / f'{slug}.md').write_text(content)
    
    print(f"  ✓ Generated {len(modules)} module pages")


def generate_files(file_docs: list[dict], output_dir: Path):
    """Generate file documentation pages."""
    files_dir = output_dir / 'files'
    files_dir.mkdir(parents=True, exist_ok=True)
    
    for i, file_doc in enumerate(file_docs):
        file_path = file_doc.get('file', 'unknown')
        docstring = clean_docstring(file_doc.get('docstring', ''))
        functions = file_doc.get('functions', [])
        classes = file_doc.get('classes', [])
        
        slug = slugify(file_path.replace('/', '-').replace('.py', ''))
        
        content = f"""---
sidebar_position: {i + 1}
---

# {file_path}

## Overview

{docstring}

"""
        if classes:
            content += "## Classes\n\n"
            for cls in classes:
                cls_slug = slugify(f"{file_path}-{cls}".replace('/', '-').replace('.py', ''))
                content += f"- [`{cls}`](../api/classes/{cls_slug})\n"
            content += "\n"
        
        if functions:
            content += "## Functions\n\n"
            for func in functions:
                # Skip class methods (they contain dots like ClassName.method)
                if '.' not in func:
                    func_slug = slugify(f"{file_path}-{func}".replace('/', '-').replace('.py', ''))
                    content += f"- [`{func}`](../api/functions/{func_slug})\n"
            content += "\n"
        
        (files_dir / f'{slug}.md').write_text(content)
    
    print(f"  ✓ Generated {len(file_docs)} file pages")


def generate_classes(class_docs: list[dict], output_dir: Path):
    """Generate class documentation pages."""
    classes_dir = output_dir / 'api' / 'classes'
    classes_dir.mkdir(parents=True, exist_ok=True)
    
    for i, cls_doc in enumerate(class_docs):
        class_id = cls_doc.get('class_id', 'unknown')
        file_path = cls_doc.get('file', '')
        name = cls_doc.get('name', 'Unknown')
        docstring = clean_docstring(cls_doc.get('docstring', ''))
        methods = cls_doc.get('methods', [])
        
        slug = slugify(class_id.replace('::', '-').replace('/', '-').replace('.py', ''))
        
        content = f"""---
sidebar_position: {i + 1}
---

# {name}

**File:** `{file_path}`

## Overview

{docstring}

"""
        if methods:
            content += "## Methods\n\n"
            for method in methods:
                method_name = method.get('name', '')
                signature = method.get('signature', '')
                content += f"### `{method_name}`\n\n"
                content += f"```python\n{signature}\n```\n\n"
        
        (classes_dir / f'{slug}.md').write_text(content)
    
    print(f"  ✓ Generated {len(class_docs)} class pages")


def generate_functions(function_docs: list[dict], output_dir: Path):
    """Generate function documentation pages."""
    functions_dir = output_dir / 'api' / 'functions'
    functions_dir.mkdir(parents=True, exist_ok=True)
    
    # Group functions by file for better organization
    functions_by_file: dict[str, list] = {}
    for func in function_docs:
        file_path = func.get('file', 'unknown')
        if file_path not in functions_by_file:
            functions_by_file[file_path] = []
        functions_by_file[file_path].append(func)
    
    position = 1
    for file_path, funcs in sorted(functions_by_file.items()):
        for func_doc in funcs:
            node_id = func_doc.get('node_id', '')
            name = func_doc.get('name', 'unknown')
            signature = func_doc.get('signature', '')
            docstring = clean_docstring(func_doc.get('docstring', ''))
            line_start = func_doc.get('line_start', 0)
            line_end = func_doc.get('line_end', 0)
            dependencies = func_doc.get('dependencies', [])
            called_by = func_doc.get('called_by', [])
            
            # Skip class methods (they're documented in class pages)
            if '::' in node_id and '.' in node_id.split('::')[1]:
                continue
            
            slug = slugify(node_id.replace('::', '-').replace('/', '-').replace('.py', ''))
            
            # Get code example if available
            code_example = func_doc.get('code_example', '')
            example_source = func_doc.get('example_source', '')
            
            content = f"""---
sidebar_position: {position}
---

# {name}

**File:** `{file_path}` (lines {line_start}-{line_end})

## Signature

```python
{signature}
```

## Description

{docstring}

"""
            # Add code example section if available
            if code_example:
                source_badge = "✅ From tests" if example_source == "test" else "💡 Generated"
                content += f"""## Example {source_badge}

```python
{code_example}
```

"""
            
            if dependencies:
                content += "## Dependencies\n\n"
                content += "This function calls:\n\n"
                for dep in dependencies:
                    content += f"- `{dep}`\n"
                content += "\n"
            
            if called_by:
                content += "## Called By\n\n"
                content += "This function is called by:\n\n"
                for caller in called_by:
                    content += f"- `{caller}`\n"
                content += "\n"
            
            (functions_dir / f'{slug}.md').write_text(content)
            position += 1
    
    print(f"  ✓ Generated {position - 1} function pages")


def detect_repo_name() -> str | None:
    """Auto-detect repo name from .docs directory if there's only one."""
    docs_base = Path('.docs')
    if not docs_base.exists():
        return None
    
    repos = [d.name for d in docs_base.iterdir() if d.is_dir() and (d / '4_llm_summary.yaml').exists()]
    
    if len(repos) == 1:
        return repos[0]
    return None


def generate_docusaurus_docs(repo_name: str) -> bool:
    """Generate Docusaurus markdown files from YAML documentation.
    
    Args:
        repo_name: Name of the repository to generate docs for
        
    Returns:
        True if successful, False otherwise
    """
    # Paths
    docs_dir = Path('.docs') / repo_name
    docs_site_dir = docs_dir / 'site'
    output_dir = docs_site_dir / 'docs'
    
    # Verify docs directory exists
    if not docs_dir.exists():
        print(f"Error: Documentation directory not found: {docs_dir}")
        return False
    
    # Verify required YAML files exist
    required_files = ['11_module_docs.yaml', '9_file_docs.yaml', '7_class_docs.yaml', '5_function_docs.yaml']
    missing = [f for f in required_files if not (docs_dir / f).exists()]
    if missing:
        print(f"Error: Missing required documentation files:")
        for f in missing:
            print(f"  - {docs_dir / f}")
        print("\nPlease run the documentation pipeline first (main.py)")
        return False
    
    # Ensure docs-site directory exists
    docs_site_dir.mkdir(parents=True, exist_ok=True)
    
    # Clean output directory (but keep the docs-site structure)
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating Docusaurus documentation for '{repo_name}'...")
    
    # Load YAML docs
    print("\nLoading documentation files...")
    
    with open(docs_dir / '11_module_docs.yaml') as f:
        modules = yaml.safe_load(f) or []
    print(f"  Loaded {len(modules)} modules")
    
    with open(docs_dir / '9_file_docs.yaml') as f:
        file_docs = yaml.safe_load(f) or []
    print(f"  Loaded {len(file_docs)} files")
    
    with open(docs_dir / '7_class_docs.yaml') as f:
        class_docs = yaml.safe_load(f) or []
    print(f"  Loaded {len(class_docs)} classes")
    
    with open(docs_dir / '5_function_docs.yaml') as f:
        function_docs = yaml.safe_load(f) or []
    print(f"  Loaded {len(function_docs)} functions")
    
    # Load synthesis docs (optional - may not exist)
    synthesis = None
    synthesis_file = docs_dir / '15_synthesis_doc.yaml'
    if synthesis_file.exists():
        with open(synthesis_file) as f:
            synthesis_raw = yaml.safe_load(f)
        # Handle case where synthesis is stored as a string in a list
        if synthesis_raw:
            if isinstance(synthesis_raw, list) and len(synthesis_raw) > 0:
                first_item = synthesis_raw[0]
                if isinstance(first_item, str):
                    # Parse the YAML string
                    synthesis = yaml.safe_load(first_item)
                else:
                    synthesis = first_item
            elif isinstance(synthesis_raw, dict):
                synthesis = synthesis_raw
        print(f"  Loaded synthesis documentation")
    else:
        print(f"  No synthesis docs found (15_synthesis_doc.yaml)")
    
    # Load architecture diagram (optional - may not exist)
    architecture_diagram = None
    arch_file = docs_dir / '12_architecture_diagram.yaml'
    if arch_file.exists():
        with open(arch_file) as f:
            arch_raw = yaml.safe_load(f)
        # Handle case where diagram is stored as a string in a list
        if arch_raw:
            if isinstance(arch_raw, list) and len(arch_raw) > 0:
                first_item = arch_raw[0]
                if isinstance(first_item, str):
                    architecture_diagram = yaml.safe_load(first_item)
                else:
                    architecture_diagram = first_item
            elif isinstance(arch_raw, dict):
                architecture_diagram = arch_raw
        print(f"  Loaded architecture diagram")
    
    # Generate markdown
    print("\nGenerating markdown files...")
    
    generate_guide(synthesis, repo_name, output_dir, architecture_diagram)
    generate_index(repo_name, modules, synthesis, output_dir)
    generate_modules(modules, output_dir)
    generate_files(file_docs, output_dir)
    generate_classes(class_docs, output_dir)
    generate_functions(function_docs, output_dir)
    
    print(f"\n✅ Documentation generated in {output_dir}")
    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate Docusaurus documentation from YAML docs")
    parser.add_argument(
        'repo_name',
        nargs='?',
        help='Repository name (defaults to auto-detection if only one repo exists)'
    )
    args = parser.parse_args()
    
    # Determine repo_name
    repo_name = args.repo_name
    if not repo_name:
        repo_name = detect_repo_name()
        if not repo_name:
            print("Error: Could not determine repo_name.")
            print("Please specify it as an argument: python generate_docs.py <repo_name>")
            print("\nAvailable repos in .docs/:")
            docs_base = Path('.docs')
            if docs_base.exists():
                for d in docs_base.iterdir():
                    if d.is_dir():
                        print(f"  - {d.name}")
            return
        print(f"Auto-detected repo_name: {repo_name}")
    
    success = generate_docusaurus_docs(repo_name)
    if success:
        docs_site_dir = Path('.docs') / repo_name / 'site'
        print("\nTo view the docs, run:")
        print(f"  cd {docs_site_dir} && npm start")


if __name__ == '__main__':
    main()



