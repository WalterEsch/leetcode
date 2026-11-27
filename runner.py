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
    "linked_list_list": lambda lists: [build_linked_list(v) for v in lists],
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


def deep_equal(a, b):
    """Like ==, but floats only need to be close, and tuples count as lists."""
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b if isinstance(a, bool) and isinstance(b, bool) else False
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if isinstance(a, float) or isinstance(b, float):
            return math.isclose(a, b, rel_tol=1e-5, abs_tol=1e-5)
        return a == b
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(deep_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(deep_equal(a[k], b[k]) for k in a)
    return a == b


def answers_match(actual, expected, mode, test_input=None, checker=None):
    if mode == "custom":
        return bool(checker(copy.deepcopy(test_input), actual, expected))
    if mode == "unordered":
        if not isinstance(actual, (list, tuple)):
            return False
        actual = [list(x) if isinstance(x, tuple) else x for x in actual]
        return sorted(actual, key=_sort_key) == sorted(expected, key=_sort_key)
    if mode == "unordered_nested":
        if not isinstance(actual, (list, tuple)) or not all(isinstance(g, (list, tuple)) for g in actual):
            return False
        norm = lambda groups: sorted((sorted(g, key=_sort_key) for g in groups), key=_sort_key)  # noqa: E731
        return norm(actual) == norm(expected)
    return deep_equal(actual, expected)


def to_jsonable(value):
    """Make a value safe to send to the browser."""
    if isinstance(value, tuple):
        value = list(value)
    if isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
        return {"__repr__": repr(value)}
    try:
        json.dumps(value, allow_nan=False)
        return value
    except (TypeError, ValueError):
        if isinstance(value, list):
            return [to_jsonable(v) for v in value]
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


def base_namespace():
    namespace = {
        "__name__": "solution",
        "ListNode": ListNode,
        "TreeNode": TreeNode,
        "build_linked_list": build_linked_list,
        "linked_list_to_values": linked_list_to_values,
        "build_tree": build_tree,
        "tree_to_values": tree_to_values,
    }
    exec("from typing import *\nimport collections, heapq, math, bisect, itertools, functools\n"
         "from collections import *\nfrom heapq import *\nfrom functools import *", namespace)
    return namespace


def call_function(problem, namespace, test_input):
    """Default way to run one test: call Solution().<function>(*args)."""
    params = problem["params"]
    arg_types = problem.get("arg_types", {})
    raw_args = [copy.deepcopy(test_input[p]) for p in params]
    args = [CONVERT_IN[arg_types[p]](a) if p in arg_types else a for p, a in zip(params, raw_args)]
    result = getattr(namespace["Solution"](), problem["function"])(*args)
    # Some problems ask you to change an argument in place instead of returning.
    out_arg = problem.get("output_from_arg")
    if out_arg:
        result = args[params.index(out_arg)]
        conv = arg_types.get(out_arg)
        return CONVERT_OUT[conv](result) if conv in CONVERT_OUT else result
    return_type = problem.get("return_type")
    return CONVERT_OUT[return_type](result) if return_type in CONVERT_OUT else result


def call_design(problem, namespace, test_input):
    """Design problems: build the class, then call methods in order."""
    ops = test_input["operations"]
    arguments = copy.deepcopy(test_input["arguments"])
    obj = namespace[ops[0]](*arguments[0])
    outputs = [None]
    for op, op_args in zip(ops[1:], arguments[1:]):
        outputs.append(getattr(obj, op)(*op_args))
    return outputs


def run(problem, code):
    namespace = base_namespace()
    if problem.get("prelude"):
        exec(problem["prelude"], namespace)

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

    kind = problem.get("kind", "function")
    if kind == "design":
        name = problem["class"]
        if name not in namespace:
            return {"ok": False, "error": f"Could not find a class named {name}."}
        caller = call_design
    else:
        if "Solution" not in namespace or not hasattr(namespace["Solution"], problem["function"]):
            return {"ok": False, "error": f"Could not find class Solution with a method named {problem['function']}()."}
        caller = call_function

    # A problem can supply its own way to call your code (for example, to build
    # a linked list with a cycle) and its own way to check answers.
    helpers = dict(namespace)
    if problem.get("harness"):
        exec(problem["harness"], helpers)
        caller = helpers["call"]
    checker = None
    if problem.get("checker"):
        exec(problem["checker"], helpers)
        checker = helpers["check"]
    compare_mode = problem.get("compare", "exact")

    results = []
    for index, test in enumerate(problem["tests"]):
        out = io.StringIO()
        entry = {"index": index, "input": test["input"], "expected": test.get("expected")}
        start = time.perf_counter()
        try:
            with contextlib.redirect_stdout(out):
                result = caller(problem, namespace, copy.deepcopy(test["input"]))
            entry["actual"] = to_jsonable(result)
            entry["passed"] = answers_match(result, test.get("expected"), compare_mode, test["input"], checker)
        except RecursionError as exc:
            entry["passed"] = False
            entry["error"] = user_traceback(exc)[-1500:]
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
    sys.setrecursionlimit(20000)  # recursive tree and DFS solutions can go deep
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
