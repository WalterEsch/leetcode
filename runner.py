"""Runs a solution file against one problem's test cases.

Usage: python runner.py <problem.json> <solution.py>

Prints a single JSON object describing the results to stdout. The app runs
this in a separate process so that an infinite loop or crash in your code
cannot take down the app (it is killed after a time limit).
"""

import collections
import contextlib
import copy
import heapq
import io
import json
import math
import sys
import time
import traceback
from typing import List, Optional  # noqa: F401  (made available to solutions)

MAX_STDOUT = 4000
MAX_NODES = 100_000


# --------------------------------------------------------------------------
# Data structures used by LeetCode-style problems
# --------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def linked_list_to_values(node):
    values = []
    while node is not None:
        if len(values) >= MAX_NODES:
            raise ValueError("Returned linked list looks like it has a cycle")
        values.append(node.val)
        node = node.next
    return values


def build_tree(values):
    """Build a binary tree from level-order values, with None for gaps."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_values(root):
    if root is None:
        return []
    values = []
    queue = collections.deque([root])
    while queue:
        if len(values) >= MAX_NODES:
            raise ValueError("Returned tree is too large (or has a cycle)")
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


CONVERT_IN = {
    "linked_list": build_linked_list,
    "tree": build_tree,
}

CONVERT_OUT = {
    "linked_list": linked_list_to_values,
    "tree": tree_to_values,
}


# --------------------------------------------------------------------------
# Comparing answers
# --------------------------------------------------------------------------

def _sort_key(x):
    return json.dumps(x, sort_keys=True)


def answers_match(actual, expected, mode):
    if mode == "float":
        return isinstance(actual, (int, float)) and math.isclose(
            actual, expected, rel_tol=1e-5, abs_tol=1e-5)
    if mode == "unordered":
        if not isinstance(actual, list):
            return False
        return sorted(actual, key=_sort_key) == sorted(expected, key=_sort_key)
    if mode == "unordered_nested":
        if not isinstance(actual, list) or not all(isinstance(g, list) for g in actual):
            return False
        norm = lambda groups: sorted((sorted(g, key=_sort_key) for g in groups), key=_sort_key)  # noqa: E731
        return norm(actual) == norm(expected)
    return actual == expected


def to_jsonable(value):
    """Make a value safe to send to the browser."""
    try:
        json.dumps(value)
        return value
    except (TypeError, ValueError):
        if isinstance(value, tuple):
            return to_jsonable(list(value))
        return {"__repr__": repr(value)}


# --------------------------------------------------------------------------
# Running
# --------------------------------------------------------------------------

def user_traceback(exc):
    """Format a traceback showing only the lines from the user's solution."""
    frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename == "solution.py"]
    lines = []
    if frames:
        lines.append("Traceback (in your code):")
        lines.extend(traceback.format_list(frames))
    lines.extend(traceback.format_exception_only(type(exc), exc))
    return "".join(lines).rstrip()


def run(problem, code):
    namespace = {
        "__name__": "solution",
        "List": List,
        "Optional": Optional,
        "ListNode": ListNode,
        "TreeNode": TreeNode,
        "collections": collections,
        "heapq": heapq,
        "math": math,
    }
    exec("from typing import *", namespace)

    try:
        compiled = compile(code, "solution.py", "exec")
    except SyntaxError as exc:
        return {"ok": False, "error": "".join(traceback.format_exception_only(type(exc), exc)).rstrip()}

    load_out = io.StringIO()
    try:
        with contextlib.redirect_stdout(load_out):
            exec(compiled, namespace)
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": user_traceback(exc)}

    solution_cls = namespace.get("Solution")
    func_name = problem["function"]
    if solution_cls is None or not hasattr(solution_cls, func_name):
        return {"ok": False, "error": f"Could not find class Solution with a method named {func_name}()."}

    params = problem["params"]
    arg_types = problem.get("arg_types", {})
    return_type = problem.get("return_type")
    compare_mode = problem.get("compare", "exact")

    results = []
    for index, test in enumerate(problem["tests"]):
        raw_args = [copy.deepcopy(test["input"][p]) for p in params]
        args = [CONVERT_IN[arg_types[p]](a) if p in arg_types else a for p, a in zip(params, raw_args)]
        out = io.StringIO()
        entry = {"index": index, "input": test["input"], "expected": test["expected"]}
        start = time.perf_counter()
        try:
            with contextlib.redirect_stdout(out):
                result = getattr(solution_cls(), func_name)(*args)
            if return_type in CONVERT_OUT:
                result = CONVERT_OUT[return_type](result)
            entry["actual"] = to_jsonable(result)
            entry["passed"] = answers_match(result, test["expected"], compare_mode)
        except Exception as exc:  # noqa: BLE001
            entry["passed"] = False
            entry["error"] = user_traceback(exc)
        entry["ms"] = round((time.perf_counter() - start) * 1000, 2)
        printed = out.getvalue()
        if printed:
            entry["stdout"] = printed[:MAX_STDOUT] + ("\n... (output truncated)" if len(printed) > MAX_STDOUT else "")
        results.append(entry)

    return {
        "ok": True,
        "passed": sum(r["passed"] for r in results),
        "total": len(results),
        "results": results,
    }


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        problem = json.load(f)
    with open(sys.argv[2], encoding="utf-8") as f:
        code = f.read()
    real_stdout = sys.stdout
    report = run(problem, code)
    real_stdout.write(json.dumps(report))
    real_stdout.flush()


if __name__ == "__main__":
    main()
