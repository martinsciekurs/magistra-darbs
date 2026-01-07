import json
from pathlib import Path

# Load your existing combined_docs.json
with open(".docs/graphrag/combined_docs.json", "r") as f:
    data = json.load(f)

# 1. Create the docs_tree.json
# CodeWikiBench usually wants a list of all paths or a nested structure
docs_tree = {
    "repo": data["repo"],
    "structure": data["structure"]["sections"] # or the full structure object
}

# 2. Create the structured_docs.json
# Flatten your sections and root files into a single list
all_docs = []
all_docs.extend(data["structure"]["files"])
for section in data["structure"]["sections"]:
    all_docs.extend(section["files"])

# Save to the benchmark's expected directory structure
output_dir = Path(f"data/{data['repo']}/my_custom_docs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "docs_tree.json", "w") as f:
    json.dump(docs_tree, f, indent=2)

with open(output_dir / "structured_docs.json", "w") as f:
    json.dump(all_docs, f, indent=2)