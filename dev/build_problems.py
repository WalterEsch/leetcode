"""Builds problems/*.json and dev/reference/*.py from the sources in dev/src/.

Each source module defines PROBLEMS, a list of dicts in roadmap order. Expected
answers are computed by running the reference solution, so a test is only as
good as its reference; dev/check_problems.py re-checks everything afterwards.

Usage: python dev/build_problems.py
"""
import ast
import importlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "dev"))
import runner  # noqa: E402

# (module, category) in NeetCode roadmap order.
CATEGORIES = [
    ("arrays_hashing", "Arrays & Hashing"),
    ("two_pointers", "Two Pointers"),
    ("sliding_window", "Sliding Window"),
    ("stack", "Stack"),
    ("binary_search", "Binary Search"),
    ("linked_list", "Linked List"),
    ("trees", "Trees"),
    ("tries", "Tries"),
    ("heap", "Heap / Priority Queue"),
    ("backtracking", "Backtracking"),
    ("graphs", "Graphs"),
    ("advanced_graphs", "Advanced Graphs"),
    ("dp_1d", "1-D Dynamic Programming"),
    ("dp_2d", "2-D Dynamic Programming"),
    ("greedy", "Greedy"),
    ("intervals", "Intervals"),
    ("math_geometry", "Math & Geometry"),
    ("bit_manipulation", "Bit Manipulation"),
]

PASSTHROUGH = ["compare", "checker", "harness", "prelude", "arg_types", "return_type",
               "output_from_arg", "kind", "class"]


def params_from_signature(sig):
    tree = ast.parse("class S:\n    " + sig.strip() + "\n        pass\n")
    fn = tree.body[0].body[0]
    return fn.name, [a.arg for a in fn.args.args[1:]]


def build(src, category, order):
    p = {
        "id": src["id"],
        "order": order,
        "title": src["title"],
        "category": category,
        "difficulty": src["difficulty"],
        "description": src["desc"].strip(),
    }
    if "starter" in src:
        p["starter"] = src["starter"].strip("\n") + "\n"
        if src.get("kind") != "design":
            p["function"] = src["function"]
            p["params"] = src.get("params", [])
    else:
        name, params = params_from_signature(src["sig"])
        p["function"] = name
        p["params"] = params
        p["starter"] = (src.get("starter_prefix", "") + "class Solution:\n    " + src["sig"].strip()
                        + "\n        pass\n")
    for key in PASSTHROUGH:
        if key in src:
            p[key] = src[key]
    p["hints"] = src["hints"]

    # Compute expected answers from the reference solution.
    p["tests"] = [{"input": t, "expected": None} for t in src["tests"]]
    compute = {k: v for k, v in p.items() if k not in ("compare", "checker")}
    report = runner.run(compute, src["ref"])
    if not report.get("ok"):
        raise SystemExit(f"{src['id']}: reference failed to load: {report.get('error')}")
    for test, r in zip(p["tests"], report["results"]):
        if "error" in r:
            raise SystemExit(f"{src['id']}: reference raised on {json.dumps(test['input'])[:200]}: {r['error']}")
        test["expected"] = r["actual"]
    # Optional hand-written answers, to double check the reference solution.
    for i, want in (src.get("expect") or {}).items():
        got = p["tests"][i]["expected"]
        mode = p.get("compare", "exact")
        if mode != "custom" and not runner.answers_match(got, want, mode):
            raise SystemExit(f"{src['id']}: test {i} expected {want!r} but reference gave {got!r}")
    for t in p["tests"][: src.get("examples", 2)]:
        t["example"] = True
    return p


def main():
    (ROOT / "problems").mkdir(exist_ok=True)
    (ROOT / "dev" / "reference").mkdir(exist_ok=True)
    order = 0
    seen = set()
    for module_name, category in CATEGORIES:
        if not (ROOT / "dev" / "src" / f"{module_name}.py").is_file():
            print(f"{category}: (no source yet)")
            continue
        module = importlib.import_module(f"src.{module_name}")
        for src in module.PROBLEMS:
            order += 1
            if src["id"] in seen:
                raise SystemExit(f"duplicate id {src['id']}")
            seen.add(src["id"])
            p = build(src, category, order)
            (ROOT / "problems" / f"{p['id']}.json").write_text(json.dumps(p, indent=1) + "\n", encoding="utf-8")
            (ROOT / "dev" / "reference" / f"{p['id']}.py").write_text(src["ref"].strip() + "\n", encoding="utf-8")
        print(f"{category}: {len(module.PROBLEMS)}")
    print(f"total: {order}")


if __name__ == "__main__":
    main()
