#!/usr/bin/env python3
"""
LLM-as-a-judge evaluation for generated documentation.

Usage:
    python eval/evaluate_docs.py <repo_name>
    python eval/evaluate_docs.py graphrag --sample 10
    python eval/evaluate_docs.py graphrag --compare docgen-prev
"""

import argparse
import json
import os
import random
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

EVALUATION_CRITERIA = """
Evaluate this documentation on the following criteria (1-5 scale):

1. **Clarity** (1-5): Is the documentation clear and easy to understand?
2. **Completeness** (1-5): Does it cover what the code does, parameters, return values, and usage?
3. **Accuracy** (1-5): Does the description accurately reflect what the code likely does based on context?
4. **Structure** (1-5): Is it well-organized with proper headings, formatting, and flow?
5. **Usefulness** (1-5): Would this help a developer understand and use this code?

Respond in JSON format:
{
    "clarity": <score>,
    "completeness": <score>,
    "accuracy": <score>,
    "structure": <score>,
    "usefulness": <score>,
    "overall": <average>,
    "strengths": ["..."],
    "weaknesses": ["..."],
    "summary": "One sentence summary"
}
"""

COMPARISON_PROMPT = """
Compare these two documentation samples for the same or similar code.

**Documentation A:**
{doc_a}

**Documentation B:**
{doc_b}

Which documentation is better? Evaluate both and determine a winner.

Respond in JSON format:
{
    "doc_a_score": <1-5>,
    "doc_b_score": <1-5>,
    "winner": "A" or "B" or "tie",
    "reasoning": "Why one is better than the other"
}
"""


def get_llm():
    """Initialize the LLM client."""
    from langchain_openai import ChatOpenAI

    api_key = os.getenv("KIMI_API_KEY")
    if not api_key:
        raise ValueError("KIMI_API_KEY not found in environment. Set it in .env or export it.")

    return ChatOpenAI(
        model="kimi-k2-turbo-preview",
        api_key=api_key,
        base_url="https://api.moonshot.ai/v1"
    )


def load_combined_docs(repo: str, base_path: Path) -> dict:
    """Load the combined docs JSON for a repo."""
    docs_file = base_path / ".docs" / repo / "combined_docs.json"
    if not docs_file.exists():
        raise FileNotFoundError(f"Combined docs not found: {docs_file}\nRun: python eval/combine_docs.py {repo}")

    with open(docs_file) as f:
        return json.load(f)


def sample_docs(data: dict, n: int = 10, section: str | None = None) -> list[dict]:
    """Sample n documents from the combined docs."""
    all_docs = []

    for sec in data["structure"]["sections"]:
        if section and sec["name"] != section:
            continue
        all_docs.extend(sec["files"])

    all_docs.extend(data["structure"]["files"])

    if len(all_docs) <= n:
        return all_docs

    return random.sample(all_docs, n)


def evaluate_single_doc(llm, doc: dict) -> dict:
    """Evaluate a single documentation entry."""
    prompt = f"""
{EVALUATION_CRITERIA}

**Title:** {doc['title']}
**Path:** {doc['path']}

**Documentation Content:**
{doc['content'][:4000]}  # Truncate for token limits
"""

    messages = [
        ("system", "You are a documentation quality evaluator. Respond only with valid JSON."),
        ("human", prompt)
    ]

    response = llm.invoke(messages)

    try:
        # Extract JSON from response
        text = response.content
        # Handle markdown code blocks
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]

        return json.loads(text.strip())
    except json.JSONDecodeError:
        return {"error": "Failed to parse LLM response", "raw": response.content}


def compare_docs(llm, doc_a: dict, doc_b: dict) -> dict:
    """Compare two documentation entries."""
    prompt = COMPARISON_PROMPT.format(
        doc_a=f"**{doc_a['title']}**\n{doc_a['content'][:2000]}",
        doc_b=f"**{doc_b['title']}**\n{doc_b['content'][:2000]}"
    )

    messages = [
        ("system", "You are a documentation quality evaluator. Respond only with valid JSON."),
        ("human", prompt)
    ]

    response = llm.invoke(messages)

    try:
        text = response.content
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]

        return json.loads(text.strip())
    except json.JSONDecodeError:
        return {"error": "Failed to parse LLM response", "raw": response.content}


def run_evaluation(repo: str, base_path: Path, sample_size: int = 10, section: str | None = None):
    """Run evaluation on sampled docs from a repo."""
    print(f"Loading docs for {repo}...")
    data = load_combined_docs(repo, base_path)

    print(f"Sampling {sample_size} documents...")
    samples = sample_docs(data, sample_size, section)

    print(f"Initializing LLM...")
    llm = get_llm()

    results = []
    for i, doc in enumerate(samples, 1):
        print(f"Evaluating [{i}/{len(samples)}]: {doc['title'][:50]}...")
        result = evaluate_single_doc(llm, doc)
        result["doc_path"] = doc["path"]
        result["doc_title"] = doc["title"]
        results.append(result)

    # Calculate aggregates
    valid_results = [r for r in results if "error" not in r]
    if valid_results:
        avg_scores = {
            "clarity": sum(r["clarity"] for r in valid_results) / len(valid_results),
            "completeness": sum(r["completeness"] for r in valid_results) / len(valid_results),
            "accuracy": sum(r["accuracy"] for r in valid_results) / len(valid_results),
            "structure": sum(r["structure"] for r in valid_results) / len(valid_results),
            "usefulness": sum(r["usefulness"] for r in valid_results) / len(valid_results),
        }
        avg_scores["overall"] = sum(avg_scores.values()) / len(avg_scores)
    else:
        avg_scores = {}

    return {
        "repo": repo,
        "sample_size": len(samples),
        "evaluated": len(valid_results),
        "average_scores": avg_scores,
        "individual_results": results
    }


def run_comparison(repo_a: str, repo_b: str, base_path: Path, sample_size: int = 5):
    """Compare docs between two repos (matching by similar titles if possible)."""
    print(f"Loading docs for {repo_a} and {repo_b}...")
    data_a = load_combined_docs(repo_a, base_path)
    data_b = load_combined_docs(repo_b, base_path)

    # Sample from repo_a
    samples_a = sample_docs(data_a, sample_size)
    samples_b = sample_docs(data_b, sample_size)

    print(f"Initializing LLM...")
    llm = get_llm()

    results = []
    for i, (doc_a, doc_b) in enumerate(zip(samples_a, samples_b), 1):
        print(f"Comparing [{i}/{len(samples_a)}]: {doc_a['title'][:30]} vs {doc_b['title'][:30]}...")
        result = compare_docs(llm, doc_a, doc_b)
        result["doc_a_path"] = doc_a["path"]
        result["doc_b_path"] = doc_b["path"]
        results.append(result)

    # Tally wins
    wins = {"A": 0, "B": 0, "tie": 0}
    for r in results:
        if "winner" in r:
            wins[r["winner"]] += 1

    return {
        "repo_a": repo_a,
        "repo_b": repo_b,
        "comparisons": len(results),
        "wins": wins,
        "results": results
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate documentation quality using LLM-as-a-judge")
    parser.add_argument("repo", help="Repository name to evaluate")
    parser.add_argument("--sample", "-n", type=int, default=10, help="Number of docs to sample (default: 10)")
    parser.add_argument("--section", "-s", help="Only evaluate docs from this section (e.g., 'guide', 'api')")
    parser.add_argument("--compare", "-c", help="Compare against another repo")
    parser.add_argument("--output", "-o", help="Output results to JSON file")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible sampling")

    args = parser.parse_args()
    base_path = Path(__file__).parent.parent

    if args.seed:
        random.seed(args.seed)

    if args.compare:
        results = run_comparison(args.repo, args.compare, base_path, args.sample)
        print("\n" + "=" * 60)
        print(f"COMPARISON: {args.repo} vs {args.compare}")
        print("=" * 60)
        print(f"Wins: {results['repo_a']}={results['wins']['A']}, {results['repo_b']}={results['wins']['B']}, ties={results['wins']['tie']}")
    else:
        results = run_evaluation(args.repo, base_path, args.sample, args.section)
        print("\n" + "=" * 60)
        print(f"EVALUATION RESULTS: {args.repo}")
        print("=" * 60)
        if results["average_scores"]:
            print(f"Sample size: {results['sample_size']}")
            print(f"Average scores:")
            for k, v in results["average_scores"].items():
                print(f"  {k}: {v:.2f}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")

    return results


if __name__ == "__main__":
    main()
