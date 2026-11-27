from ._common import existing, LISTNODE, LIST_NOTE
from .stack import DESIGN_NOTE

PROBLEMS = [
    existing("reverse-linked-list"),
    {
        "id": "merge-two-sorted-lists", "title": "Merge Two Sorted Lists", "difficulty": "Easy",
        "desc": f"""
You are given the heads of two sorted linked lists, `list1` and `list2`. Merge them into one sorted linked list by splicing their nodes together, and return its head.

{LIST_NOTE}

**Constraints**

- Each list has 0 to 50 nodes, sorted in non-decreasing order.
""",
        "starter_prefix": LISTNODE,
        "sig": "def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:",
        "arg_types": {"list1": "linked_list", "list2": "linked_list"}, "return_type": "linked_list",
        "tests": [
            {"list1": [1, 2, 4], "list2": [1, 3, 4]}, {"list1": [], "list2": []}, {"list1": [], "list2": [0]},
            {"list1": [5], "list2": [1, 2, 3]}, {"list1": [1, 1, 1], "list2": [1, 1]},
            {"list1": [-10, 0, 10], "list2": [-5, 5, 15, 20]},
        ],
        "examples": 3,
        "expect": {0: [1, 1, 2, 3, 4, 4], 1: [], 2: [0]},
        "hints": [
            "Compare the heads of both lists. The smaller one comes first in the result.",
            "A dummy starting node saves you from special-casing the first node of the result.",
            "Keep a `tail` pointer. While both lists have nodes, attach the smaller head to `tail.next` and advance. Then attach whatever is left of the other list.",
        ],
        "ref": """
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
""",
    },
    {
        "id": "linked-list-cycle", "title": "Linked List Cycle", "difficulty": "Easy",
        "desc": f"""
You are given `head`, the head of a linked list. Return `True` if the list has a cycle, meaning that following `next` pointers eventually comes back to a node you've already seen.

In the tests, `pos` is the index of the node that the last node's `next` points back to, or `-1` for no cycle. Your function only receives `head`.

Can you do it with O(1) extra memory?

{LIST_NOTE}
""",
        "starter_prefix": LISTNODE,
        "sig": "def hasCycle(self, head: Optional[ListNode]) -> bool:",
        "harness": """
def call(problem, ns, inp):
    head = build_linked_list(inp["head"])
    if inp["pos"] >= 0:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        nodes[-1].next = nodes[inp["pos"]]
    return ns["Solution"]().hasCycle(head)
""",
        "tests": [
            {"head": [3, 2, 0, -4], "pos": 1}, {"head": [1, 2], "pos": 0}, {"head": [1], "pos": -1},
            {"head": [], "pos": -1}, {"head": [1], "pos": 0}, {"head": [1, 2, 3, 4, 5], "pos": -1},
            {"head": [1, 2, 3, 4, 5], "pos": 4}, {"head": list(range(1000)), "pos": 500},
        ],
        "examples": 3,
        "expect": {0: True, 1: True, 2: False},
        "hints": [
            "A set of visited nodes works, but uses O(n) memory.",
            "Imagine two runners on a circular track, one running twice as fast. What happens eventually?",
            "Move `slow` one step and `fast` two steps at a time. If `fast` reaches the end there is no cycle. If they ever point to the same node, there is a cycle.",
        ],
        "ref": """
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
""",
    },
    {
        "id": "reorder-list", "title": "Reorder List", "difficulty": "Medium",
        "desc": f"""
You are given the head of a linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`. Reorder it **in place** to `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`.

Change the nodes' `next` pointers rather than their values. Your function returns nothing. The tests check the list starting from the original `head`.

{LIST_NOTE}

**Constraints**

- The list has 1 to 5 * 10^4 nodes.
""",
        "starter_prefix": LISTNODE,
        "sig": "def reorderList(self, head: Optional[ListNode]) -> None:",
        "arg_types": {"head": "linked_list"}, "output_from_arg": "head",
        "tests": [
            {"head": [1, 2, 3, 4]}, {"head": [1, 2, 3, 4, 5]}, {"head": [1]}, {"head": [1, 2]},
            {"head": [1, 2, 3]}, {"head": [10, 20, 30, 40, 50, 60]},
        ],
        "expect": {0: [1, 4, 2, 3], 1: [1, 5, 2, 4, 3]},
        "hints": [
            "The result interleaves the first half of the list with the second half reversed.",
            "Find the middle with slow and fast pointers, then reverse the second half.",
            "Split the list at the middle, reverse the second half, then merge the two halves by alternating nodes: one from the first, one from the second.",
        ],
        "ref": """
class Solution:
    def reorderList(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i, j = 0, len(nodes) - 1
        order = []
        while i <= j:
            order.append(nodes[i])
            if i != j:
                order.append(nodes[j])
            i += 1
            j -= 1
        for a, b in zip(order, order[1:]):
            a.next = b
        order[-1].next = None
""",
    },
    {
        "id": "remove-nth-node-from-end-of-list", "title": "Remove Nth Node From End of List", "difficulty": "Medium",
        "desc": f"""
You are given the head of a linked list and an integer `n`. Remove the `n`th node counting from the end of the list (`n = 1` is the last node), and return the head of the changed list.

Try to do it in one pass.

{LIST_NOTE}

**Constraints**

- The list has `sz` nodes, `1 <= sz <= 30`, and `1 <= n <= sz`.
""",
        "starter_prefix": LISTNODE,
        "sig": "def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:",
        "arg_types": {"head": "linked_list"}, "return_type": "linked_list",
        "tests": [
            {"head": [1, 2, 3, 4, 5], "n": 2}, {"head": [1], "n": 1}, {"head": [1, 2], "n": 1},
            {"head": [1, 2], "n": 2}, {"head": [1, 2, 3], "n": 3}, {"head": [5, 6, 7, 8], "n": 1},
        ],
        "examples": 3,
        "expect": {0: [1, 2, 3, 5], 1: [], 2: [1]},
        "hints": [
            "Two passes work: count the length, then walk to the node before the one to remove.",
            "For one pass, start a second pointer `n` steps behind the first. When the first reaches the end, where is the second?",
            "Start both pointers at a dummy node placed before `head`. Move `fast` ahead `n + 1` steps, then move both until `fast` is `None`. Now `slow.next` is the node to remove.",
        ],
        "ref": """
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return dummy.next
""",
    },
    {
        "id": "copy-list-with-random-pointer", "title": "Copy List with Random Pointer", "difficulty": "Medium",
        "desc": """
Each node of a linked list has a `next` pointer and a `random` pointer. `random` can point to any node in the list, or be `None`. Return a **deep copy** of the list: brand new nodes with the same values, whose `next` and `random` pointers point to the matching new nodes. No pointer in the copy may point to a node of the original list.

The `Node` class is already defined:

```
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
```

Tests show the list as `[val, random_index]` pairs, where `random_index` is the position of the node that `random` points to, or `None`.

**Constraints**

- The list has 0 to 1000 nodes.
""",
        "prelude": """
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
""",
        "starter_prefix": """# Definition for a Node (already provided):
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

""",
        "sig": "def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':",
        "harness": """
def call(problem, ns, inp):
    Node = ns["Node"]
    nodes = [Node(v) for v, _ in inp["head"]]
    for i, (_, r) in enumerate(inp["head"]):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[r] if r is not None else None
    original = {id(n) for n in nodes}
    copy_head = ns["Solution"]().copyRandomList(nodes[0] if nodes else None)
    out, index, node = [], {}, copy_head
    while node is not None:
        if id(node) in original:
            raise ValueError("Your copy contains a node from the original list. Every node must be new.")
        if len(out) > 5000:
            raise ValueError("Your copied list seems to have a cycle")
        index[id(node)] = len(out)
        out.append(node)
        node = node.next
    result = []
    for n in out:
        if n.random is not None and id(n.random) not in index:
            raise ValueError("A random pointer in your copy points outside the copied list")
        result.append([n.val, index[id(n.random)] if n.random is not None else None])
    return result
""",
        "tests": [
            {"head": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]}, {"head": [[1, 1], [2, 1]]},
            {"head": [[3, None], [3, 0], [3, None]]}, {"head": []}, {"head": [[5, 0]]},
            {"head": [[1, 2], [2, 2], [3, None], [4, 0]]},
        ],
        "examples": 3,
        "hints": [
            "The hard part is the `random` pointer: when you copy a node, its `random` target may not have been copied yet.",
            "Make two passes. First create a copy of every node and remember which copy belongs to which original, in a dictionary.",
            "In the second pass, set `copy.next = old_to_new[node.next]` and `copy.random = old_to_new[node.random]` (mapping `None` to `None`).",
        ],
        "ref": """
class Solution:
    def copyRandomList(self, head):
        m = {None: None}
        n = head
        while n:
            m[n] = Node(n.val)
            n = n.next
        n = head
        while n:
            m[n].next = m[n.next]
            m[n].random = m[n.random]
            n = n.next
        return m[head]
""",
    },
    {
        "id": "add-two-numbers", "title": "Add Two Numbers", "difficulty": "Medium",
        "desc": f"""
You are given two non-empty linked lists `l1` and `l2` that represent non-negative integers. The digits are stored in **reverse order**, one digit per node, so `[2, 4, 3]` means 342. Return the sum as a linked list in the same format.

Neither number has leading zeros, except the number 0 itself.

{LIST_NOTE}

**Constraints**

- Each list has 1 to 100 nodes.
""",
        "starter_prefix": LISTNODE,
        "sig": "def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:",
        "arg_types": {"l1": "linked_list", "l2": "linked_list"}, "return_type": "linked_list",
        "tests": [
            {"l1": [2, 4, 3], "l2": [5, 6, 4]}, {"l1": [0], "l2": [0]}, {"l1": [9, 9, 9, 9, 9, 9, 9], "l2": [9, 9, 9, 9]},
            {"l1": [5], "l2": [5]}, {"l1": [1, 8], "l2": [0]}, {"l1": [9], "l2": [1, 9, 9, 9]},
        ],
        "examples": 3,
        "expect": {0: [7, 0, 8], 1: [0], 2: [8, 9, 9, 9, 0, 0, 0, 1]},
        "hints": [
            "Add the digits the way you would by hand, starting from the ones place, which is the head of each list.",
            "Keep a `carry`. Each new digit is `(a + b + carry) % 10`, and the new carry is `(a + b + carry) // 10`.",
            "Loop while either list has nodes **or** carry is non-zero, treating a missing node as 0. Build the result after a dummy node.",
        ],
        "ref": """
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry, d = divmod(s, 10)
            tail.next = ListNode(d)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
""",
    },
    {
        "id": "find-the-duplicate-number", "title": "Find the Duplicate Number", "difficulty": "Medium",
        "desc": """
You are given a list `nums` of `n + 1` integers, each between `1` and `n` inclusive. Exactly one value is repeated (it may appear more than twice). Return that value.

Do it without changing `nums` and with only O(1) extra space.

**Constraints**

- `1 <= n <= 10^5`
""",
        "sig": "def findDuplicate(self, nums: List[int]) -> int:",
        "tests": [
            {"nums": [1, 3, 4, 2, 2]}, {"nums": [3, 1, 3, 4, 2]}, {"nums": [3, 3, 3, 3, 3]}, {"nums": [1, 1]},
            {"nums": [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]}, {"nums": [1, 4, 4, 2, 4]}, {"nums": [2, 1, 2]},
        ],
        "examples": 3,
        "expect": {0: 2, 1: 3, 2: 3},
        "hints": [
            "Think of each index `i` as a node with an edge to `nums[i]`. Because two indices point to the same value, this graph has a cycle.",
            "The duplicate value is the entrance to that cycle. That is the same problem as finding where a linked list's cycle starts.",
            "Use Floyd's algorithm: move `slow = nums[slow]` and `fast = nums[nums[fast]]` until they meet. Then start a second pointer at `0` and move both one step at a time. They meet at the duplicate.",
        ],
        "ref": """
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
""",
    },
    {
        "id": "lru-cache", "title": "LRU Cache", "difficulty": "Medium", "kind": "design", "class": "LRUCache",
        "desc": f"""
Design a Least Recently Used (LRU) cache with a fixed capacity.

- `LRUCache(capacity)` creates the cache.
- `get(key)` returns the key's value, or `-1` if it is not present. Reading a key counts as using it.
- `put(key, value)` inserts or updates the key, which also counts as using it. If this makes the cache hold more than `capacity` keys, remove the key that was used least recently.

`get` and `put` must each run in O(1) average time.

{DESIGN_NOTE}
""",
        "starter": """
class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
""",
        "tests": [
            {"operations": ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
             "arguments": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]},
            {"operations": ["LRUCache", "put", "get", "put", "get", "get"],
             "arguments": [[1], [2, 1], [2], [3, 2], [2], [3]]},
            {"operations": ["LRUCache", "put", "put", "put", "put", "get", "get"],
             "arguments": [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]},
            {"operations": ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
             "arguments": [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]},
        ],
        "hints": [
            "You need fast lookup by key (a dictionary) and a way to track usage order that you can update in O(1).",
            "A doubly linked list lets you move any node to the front, or remove it, in O(1) if you already have a reference to that node.",
            "Map each key to its node in a doubly linked list ordered from most to least recently used. On `get` or `put`, move the node to the front. When over capacity, remove the node at the back. (`collections.OrderedDict` with `move_to_end` does the same thing.)",
        ],
        "ref": """
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)
""",
    },
    {
        "id": "merge-k-sorted-lists", "title": "Merge k Sorted Lists", "difficulty": "Hard",
        "desc": f"""
You are given a list `lists` of `k` linked lists, each sorted in increasing order. Merge them all into one sorted linked list and return its head.

{LIST_NOTE}

**Constraints**

- `0 <= k <= 10^4`, and the total number of nodes is at most 10^4.
""",
        "starter_prefix": LISTNODE,
        "sig": "def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:",
        "arg_types": {"lists": "linked_list_list"}, "return_type": "linked_list",
        "tests": [
            {"lists": [[1, 4, 5], [1, 3, 4], [2, 6]]}, {"lists": []}, {"lists": [[]]}, {"lists": [[], [1]]},
            {"lists": [[5], [4], [3], [2], [1]]}, {"lists": [[-2, -1, 0], [-3], [], [1, 1, 1]]},
        ],
        "examples": 3,
        "expect": {0: [1, 1, 2, 3, 4, 4, 5, 6], 1: [], 2: []},
        "hints": [
            "Merging lists one at a time into a growing result works, but can take O(k * N) time.",
            "At each step the next node is the smallest head among all lists. Which data structure finds the smallest quickly?",
            "Put each list's head in a min-heap as `(val, index, node)` (the index breaks ties, since nodes can't be compared). Pop the smallest, append it, and push its `next`. Merging lists in pairs, like merge sort, also gives O(N log k).",
        ],
        "ref": """
class Solution:
    def mergeKLists(self, lists):
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        return build_linked_list(sorted(vals))
""",
    },
    {
        "id": "reverse-nodes-in-k-group", "title": "Reverse Nodes in k-Group", "difficulty": "Hard",
        "desc": f"""
You are given the head of a linked list and a positive integer `k`. Reverse the nodes of the list `k` at a time, and return the new head. If the number of nodes left at the end is less than `k`, leave them in their original order.

Change the links between nodes, not the values inside them.

{LIST_NOTE}

**Constraints**

- The list has `n` nodes, `1 <= k <= n <= 5000`.
""",
        "starter_prefix": LISTNODE,
        "sig": "def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:",
        "arg_types": {"head": "linked_list"}, "return_type": "linked_list",
        "tests": [
            {"head": [1, 2, 3, 4, 5], "k": 2}, {"head": [1, 2, 3, 4, 5], "k": 3}, {"head": [1], "k": 1},
            {"head": [1, 2, 3, 4], "k": 4}, {"head": [1, 2, 3, 4, 5, 6], "k": 3}, {"head": [1, 2, 3], "k": 1},
            {"head": [1, 2, 3, 4, 5, 6, 7], "k": 2},
        ],
        "expect": {0: [2, 1, 4, 3, 5], 1: [3, 2, 1, 4, 5]},
        "hints": [
            "Handle one group at a time. Before reversing a group, check that it really has `k` nodes.",
            "To reconnect a reversed group, you need the node just before the group and the node just after it.",
            "Use a dummy node. For each group: find the `k`th node, remember `group_next = kth.next`, reverse the group so it points to `group_next`, then link the previous group's tail to `kth` and move on.",
        ],
        "ref": """
class Solution:
    def reverseKGroup(self, head, k):
        vals = linked_list_to_values(head)
        out = []
        for i in range(0, len(vals), k):
            chunk = vals[i:i + k]
            out.extend(chunk[::-1] if len(chunk) == k else chunk)
        return build_linked_list(out)
""",
    },
]
