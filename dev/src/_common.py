"""Shared bits for problem sources."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

LISTNODE = """# Definition for a singly linked list node (already provided):
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

TREENODE = """# Definition for a binary tree node (already provided):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

LIST_NOTE = "Tests show linked lists as Python lists, so `[1, 2, 3]` means `1 -> 2 -> 3`, and `[]` means `None`."
TREE_NOTE = ("Tests show trees in level order, left to right, with `None` for a missing child. "
             "For example `[3, 9, 20, None, None, 15, 7]` is a root `3` with children `9` and `20`, "
             "where `20` has children `15` and `7`.")


def existing(pid, **overrides):
    """Reuse a problem that was written by hand in the first version."""
    p = json.loads((ROOT / "problems" / f"{pid}.json").read_text(encoding="utf-8"))
    lines = p["starter"].split("\n")
    i = lines.index("class Solution:")
    src = {
        "id": p["id"], "title": p["title"], "difficulty": p["difficulty"],
        "desc": p["description"], "sig": lines[i + 1].strip(),
        "starter_prefix": "\n".join(lines[:i]) + ("\n" if i else ""),
        "tests": [t["input"] for t in p["tests"]],
        "examples": sum(1 for t in p["tests"] if t.get("example")),
        "hints": p["hints"],
        "ref": (ROOT / "dev" / "reference" / f"{pid}.py").read_text(encoding="utf-8"),
        "expect": {i: t["expected"] for i, t in enumerate(p["tests"])},
    }
    for k in ("compare", "arg_types", "return_type"):
        if k in p:
            src[k] = p[k]
    src.update(overrides)
    return src
