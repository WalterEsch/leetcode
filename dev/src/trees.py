from ._common import TREENODE, TREE_NOTE

N = None


def T(sig, **kw):
    """Shorthand for a tree problem whose `root` argument is a tree."""
    d = {"starter_prefix": TREENODE, "sig": sig, "arg_types": {"root": "tree"}}
    d.update(kw)
    return d


PROBLEMS = [
    T("def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:",
      id="invert-binary-tree", title="Invert Binary Tree", difficulty="Easy", return_type="tree",
      desc=f"""
You are given the `root` of a binary tree. Mirror it, so that every node's left and right children are swapped, and return the root.

{TREE_NOTE}

**Constraints**

- The tree has 0 to 100 nodes.
""",
      tests=[{"root": [4, 2, 7, 1, 3, 6, 9]}, {"root": [2, 1, 3]}, {"root": []}, {"root": [1]},
             {"root": [1, 2]}, {"root": [1, 2, N, 3, N, 4]}, {"root": [5, 3, 8, N, 4, 7]}],
      examples=3, expect={0: [4, 7, 2, 9, 6, 3, 1], 1: [2, 3, 1], 2: []},
      hints=[
          "Swapping the root's two children is a start. What else needs to happen?",
          "Every subtree also has to be mirrored. That is the same problem on a smaller tree.",
          "Recursively: if `root` is `None` return `None`; otherwise swap `root.left` and `root.right`, invert both children, and return `root`. A BFS with a queue works too.",
      ],
      ref="""
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
"""),
    T("def maxDepth(self, root: Optional[TreeNode]) -> int:",
      id="maximum-depth-of-binary-tree", title="Maximum Depth of Binary Tree", difficulty="Easy",
      desc=f"""
You are given the `root` of a binary tree. Return its maximum depth: the number of nodes on the longest path from the root down to a leaf. An empty tree has depth `0`.

{TREE_NOTE}

**Constraints**

- The tree has 0 to 10^4 nodes.
""",
      tests=[{"root": [3, 9, 20, N, N, 15, 7]}, {"root": [1, N, 2]}, {"root": []}, {"root": [0]},
             {"root": [1, 2, 3, 4, N, N, 5, 6]}, {"root": [1, 2, N, 3, N, 4, N, 5]}],
      examples=3, expect={0: 3, 1: 2, 2: 0},
      hints=[
          "How does the depth of a tree relate to the depths of its two subtrees?",
          "`depth(root) = 1 + max(depth(left), depth(right))`, and an empty tree has depth 0.",
          "Write that as a recursive function, or do a level-by-level BFS and count the levels.",
      ],
      ref="""
class Solution:
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
"""),
    T("def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:",
      id="diameter-of-binary-tree", title="Diameter of Binary Tree", difficulty="Easy",
      desc=f"""
You are given the `root` of a binary tree. Return its diameter: the number of **edges** on the longest path between any two nodes. The path does not have to pass through the root.

{TREE_NOTE}

**Constraints**

- The tree has 1 to 10^4 nodes.
""",
      tests=[{"root": [1, 2, 3, 4, 5]}, {"root": [1, 2]}, {"root": [1]},
             {"root": [1, N, 2, 3, 4, 5, N, N, 6, 7, N, N, 8]}, {"root": [4, -7, -3, N, N, -9, -3, 9, -7, -4, N, 6, N, -6, -6]}],
      expect={0: 3, 1: 1},
      hints=[
          "The longest path that bends at a given node goes down its left side as far as possible and down its right side as far as possible.",
          "So at each node, the best path through it is `height(left) + height(right)`.",
          "Write one recursive height function. While computing each node's height, update a running best with `left_height + right_height`.",
      ],
      ref="""
class Solution:
    def diameterOfBinaryTree(self, root):
        best = 0
        def h(n):
            nonlocal best
            if not n:
                return 0
            a, b = h(n.left), h(n.right)
            best = max(best, a + b)
            return 1 + max(a, b)
        h(root)
        return best
"""),
    T("def isBalanced(self, root: Optional[TreeNode]) -> bool:",
      id="balanced-binary-tree", title="Balanced Binary Tree", difficulty="Easy",
      desc=f"""
You are given the `root` of a binary tree. Return `True` if it is height-balanced: at **every** node, the heights of the left and right subtrees differ by at most 1.

{TREE_NOTE}

**Constraints**

- The tree has 0 to 5000 nodes.
""",
      tests=[{"root": [3, 9, 20, N, N, 15, 7]}, {"root": [1, 2, 2, 3, 3, N, N, 4, 4]}, {"root": []},
             {"root": [1, 2, 2, 3, N, N, 3, 4, N, N, 4]}, {"root": [1, N, 2, N, 3]}, {"root": [1, 2, 3, 4]}, {"root": [1]}],
      examples=3, expect={0: True, 1: False, 2: True, 3: False},
      hints=[
          "Checking the heights at the root is not enough. Every node has to be balanced.",
          "Computing heights separately for every node repeats a lot of work (O(n^2)). Can one pass compute heights and check balance together?",
          "Write a recursive function that returns a subtree's height, or `-1` if that subtree is unbalanced. Pass the `-1` straight up as soon as you see it.",
      ],
      ref="""
class Solution:
    def isBalanced(self, root):
        def h(n):
            if not n:
                return 0
            a, b = h(n.left), h(n.right)
            if a < 0 or b < 0 or abs(a - b) > 1:
                return -1
            return 1 + max(a, b)
        return h(root) >= 0
"""),
    {
        "id": "same-tree", "title": "Same Tree", "difficulty": "Easy",
        "desc": f"""
You are given the roots of two binary trees, `p` and `q`. Return `True` if they have exactly the same shape and the same value at every node.

{TREE_NOTE}

**Constraints**

- Each tree has 0 to 100 nodes.
""",
        "starter_prefix": TREENODE,
        "sig": "def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:",
        "arg_types": {"p": "tree", "q": "tree"},
        "tests": [{"p": [1, 2, 3], "q": [1, 2, 3]}, {"p": [1, 2], "q": [1, N, 2]}, {"p": [1, 2, 1], "q": [1, 1, 2]},
                  {"p": [], "q": []}, {"p": [1], "q": []}, {"p": [5, 4, 8, 11, N, 13, 4], "q": [5, 4, 8, 11, N, 13, 4]}],
        "examples": 3, "expect": {0: True, 1: False, 2: False},
        "hints": [
            "When are two empty trees the same? What about one empty and one not?",
            "Two non-empty trees are the same when their roots have equal values and both pairs of subtrees are the same.",
            "Recursively: return `True` if both are `None`, `False` if only one is, and otherwise compare values and recurse on the left children and the right children.",
        ],
        "ref": """
class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
""",
    },
    {
        "id": "subtree-of-another-tree", "title": "Subtree of Another Tree", "difficulty": "Easy",
        "desc": f"""
You are given the roots of two binary trees, `root` and `subRoot`. Return `True` if `root` contains a subtree that has exactly the same shape and values as `subRoot`. A subtree is a node together with **all** of its descendants.

{TREE_NOTE}

**Constraints**

- `root` has 1 to 2000 nodes, `subRoot` has 1 to 1000 nodes.
""",
        "starter_prefix": TREENODE,
        "sig": "def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:",
        "arg_types": {"root": "tree", "subRoot": "tree"},
        "tests": [{"root": [3, 4, 5, 1, 2], "subRoot": [4, 1, 2]},
                  {"root": [3, 4, 5, 1, 2, N, N, N, N, 0], "subRoot": [4, 1, 2]},
                  {"root": [1], "subRoot": [1]}, {"root": [1, 1], "subRoot": [1]}, {"root": [12], "subRoot": [2]},
                  {"root": [1, 2, 3], "subRoot": [1, 2]}, {"root": [3, 4, 5, 1, N, 2], "subRoot": [3, 1, 2]}],
        "expect": {0: True, 1: False},
        "hints": [
            "You already know how to check whether two trees are identical (Same Tree).",
            "Try every node of `root` as a possible starting point for a match.",
            "`isSubtree(root, sub)` is `True` if `sameTree(root, sub)`, or `isSubtree(root.left, sub)`, or `isSubtree(root.right, sub)`. An empty `root` can't contain a non-empty `subRoot`.",
        ],
        "ref": """
class Solution:
    def isSubtree(self, root, subRoot):
        def ser(n):
            return f"({n.val},{ser(n.left)},{ser(n.right)})" if n else "#"
        return ser(subRoot) in ser(root)
""",
    },
    T("def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:",
      id="lowest-common-ancestor-of-a-binary-search-tree",
      title="Lowest Common Ancestor of a Binary Search Tree", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary search tree and two of its nodes, `p` and `q`. Return their lowest common ancestor: the deepest node that has both `p` and `q` as descendants. A node counts as a descendant of itself.

In the tests, `p` and `q` are shown by their values, and the expected output is the value of the node you return. Your function receives the actual `TreeNode` objects.

{TREE_NOTE}

**Constraints**

- The tree has 2 to 10^5 nodes with distinct values. `p != q`, and both are in the tree.
""",
      harness="""
def call(problem, ns, inp):
    root = build_tree(inp["root"])
    def find(n, v):
        while n and n.val != v:
            n = n.left if v < n.val else n.right
        return n
    ans = ns["Solution"]().lowestCommonAncestor(root, find(root, inp["p"]), find(root, inp["q"]))
    return ans.val if ans is not None else None
""",
      tests=[{"root": [6, 2, 8, 0, 4, 7, 9, N, N, 3, 5], "p": 2, "q": 8},
             {"root": [6, 2, 8, 0, 4, 7, 9, N, N, 3, 5], "p": 2, "q": 4}, {"root": [2, 1], "p": 2, "q": 1},
             {"root": [6, 2, 8, 0, 4, 7, 9, N, N, 3, 5], "p": 3, "q": 5},
             {"root": [6, 2, 8, 0, 4, 7, 9, N, N, 3, 5], "p": 0, "q": 5},
             {"root": [6, 2, 8, 0, 4, 7, 9, N, N, 3, 5], "p": 7, "q": 9}],
      examples=3, expect={0: 6, 1: 2, 2: 2},
      hints=[
          "In a BST, everything smaller than a node is on its left and everything larger is on its right.",
          "If `p` and `q` are both smaller than the current node, the answer is in the left subtree. If both are larger, it's in the right subtree.",
          "Walk down from the root. The first node where `p` and `q` split (one on each side, or one of them equals the node) is the answer.",
      ],
      ref="""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
"""),
    T("def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:",
      id="binary-tree-level-order-traversal", title="Binary Tree Level Order Traversal", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary tree. Return its values level by level: a list of lists, where list `i` holds the values on depth `i` from left to right.

{TREE_NOTE}

**Constraints**

- The tree has 0 to 2000 nodes.
""",
      tests=[{"root": [3, 9, 20, N, N, 15, 7]}, {"root": [1]}, {"root": []}, {"root": [1, 2, 3, 4, N, N, 5]},
             {"root": [1, 2, N, 3, N, 4]}],
      examples=3, expect={0: [[3], [9, 20], [15, 7]], 1: [[1]], 2: []},
      hints=[
          "Which traversal visits nodes level by level?",
          "Breadth-first search with a queue visits nodes in level order. The trick is knowing where one level ends.",
          "At the start of each round, the queue holds exactly one level. Process `len(queue)` nodes, collecting their values and adding their children, then append that level's list.",
      ],
      ref="""
class Solution:
    def levelOrder(self, root):
        res, level = [], [root] if root else []
        while level:
            res.append([n.val for n in level])
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
"""),
    T("def rightSideView(self, root: Optional[TreeNode]) -> List[int]:",
      id="binary-tree-right-side-view", title="Binary Tree Right Side View", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary tree. Imagine standing to the right of the tree. Return the values you can see, from top to bottom (the rightmost node on each level).

{TREE_NOTE}

**Constraints**

- The tree has 0 to 100 nodes.
""",
      tests=[{"root": [1, 2, 3, N, 5, N, 4]}, {"root": [1, N, 3]}, {"root": []}, {"root": [1, 2, 3, 4]},
             {"root": [1, 2, 3, N, 5, N, N, 6]}],
      examples=3, expect={0: [1, 3, 4], 1: [1, 3], 2: [], 3: [1, 3, 4]},
      hints=[
          "The visible node on each level is the last one in that level from left to right. It is not always in the right subtree.",
          "Do a level-order traversal and keep the last value of each level.",
          "Alternatively, do a DFS that visits right children first, and record a node's value the first time you reach a new depth.",
      ],
      ref="""
class Solution:
    def rightSideView(self, root):
        res, level = [], [root] if root else []
        while level:
            res.append(level[-1].val)
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
"""),
    T("def goodNodes(self, root: TreeNode) -> int:",
      id="count-good-nodes-in-binary-tree", title="Count Good Nodes in Binary Tree", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary tree. A node is **good** if no node on the path from the root down to it has a larger value. Return the number of good nodes.

{TREE_NOTE}

**Constraints**

- The tree has 1 to 10^5 nodes.
""",
      tests=[{"root": [3, 1, 4, 3, N, 1, 5]}, {"root": [3, 3, N, 4, 2]}, {"root": [1]},
             {"root": [2, N, 4, 10, 8, N, N, 4]}, {"root": [9, N, 3, 6]}, {"root": [-1, 5, -2, 4, 4, 2, -2]}],
      examples=3, expect={0: 4, 1: 3, 2: 1},
      hints=[
          "To decide whether a node is good you only need one number from the path above it.",
          "That number is the maximum value seen so far on the path from the root.",
          "DFS while passing down `max_so_far`. A node is good if `node.val >= max_so_far`. Pass `max(max_so_far, node.val)` to the children.",
      ],
      ref="""
class Solution:
    def goodNodes(self, root):
        def go(n, m):
            if not n:
                return 0
            return (n.val >= m) + go(n.left, max(m, n.val)) + go(n.right, max(m, n.val))
        return go(root, root.val)
"""),
    T("def isValidBST(self, root: Optional[TreeNode]) -> bool:",
      id="validate-binary-search-tree", title="Validate Binary Search Tree", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary tree. Return `True` if it is a valid binary search tree:

- every value in a node's left subtree is **strictly less** than the node's value,
- every value in its right subtree is **strictly greater**, and
- both subtrees are valid binary search trees too.

{TREE_NOTE}

**Constraints**

- The tree has 1 to 10^4 nodes.
""",
      tests=[{"root": [2, 1, 3]}, {"root": [5, 1, 4, N, N, 3, 6]}, {"root": [2, 2, 2]}, {"root": [5, 4, 6, N, N, 3, 7]},
             {"root": [1]}, {"root": [10, 5, 15, N, N, 11, 20]}, {"root": [3, 1, 5, 0, 2, 4, 6]}],
      examples=3, expect={0: True, 1: False, 2: False, 3: False},
      hints=[
          "Checking only each node against its direct children is not enough. Look at test 4: `3` is below `6`, but it is in the right subtree of `5`.",
          "Every node must fit within a range `(low, high)` set by its ancestors.",
          "Recurse with bounds: the root's range is `(-inf, inf)`. Going left, the upper bound becomes the node's value; going right, the lower bound does. (An in-order traversal must also be strictly increasing.)",
      ],
      ref="""
class Solution:
    def isValidBST(self, root):
        vals = []
        def ino(n):
            if n:
                ino(n.left)
                vals.append(n.val)
                ino(n.right)
        ino(root)
        return all(a < b for a, b in zip(vals, vals[1:]))
"""),
    T("def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:",
      id="kth-smallest-element-in-a-bst", title="Kth Smallest Element in a BST", difficulty="Medium",
      desc=f"""
You are given the `root` of a binary search tree and an integer `k`. Return the `k`th smallest value in the tree, counting from 1.

{TREE_NOTE}

**Constraints**

- The tree has `n` nodes, `1 <= k <= n <= 10^4`.
""",
      tests=[{"root": [3, 1, 4, N, 2], "k": 1}, {"root": [5, 3, 6, 2, 4, N, N, 1], "k": 3}, {"root": [1], "k": 1},
             {"root": [5, 3, 6, 2, 4, N, N, 1], "k": 6}, {"root": [2, 1, 3], "k": 2}],
      expect={0: 1, 1: 3},
      hints=[
          "Which traversal of a BST visits the values in sorted order?",
          "An in-order traversal (left, node, right) produces the values from smallest to largest.",
          "Do an in-order traversal (iteratively with a stack is neat) and stop as soon as you have visited `k` nodes.",
      ],
      ref="""
class Solution:
    def kthSmallest(self, root, k):
        vals = []
        def ino(n):
            if n:
                ino(n.left)
                vals.append(n.val)
                ino(n.right)
        ino(root)
        return vals[k - 1]
"""),
    {
        "id": "construct-binary-tree-from-preorder-and-inorder-traversal",
        "title": "Construct Binary Tree from Preorder and Inorder Traversal", "difficulty": "Medium",
        "desc": f"""
You are given two lists, `preorder` and `inorder`, which are the preorder and inorder traversals of the same binary tree. All values are distinct. Build the tree and return its root.

{TREE_NOTE}

**Constraints**

- `1 <= len(preorder) == len(inorder) <= 3000`
""",
        "starter_prefix": TREENODE,
        "sig": "def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:",
        "return_type": "tree",
        "tests": [{"preorder": [3, 9, 20, 15, 7], "inorder": [9, 3, 15, 20, 7]}, {"preorder": [-1], "inorder": [-1]},
                  {"preorder": [1, 2], "inorder": [2, 1]}, {"preorder": [1, 2], "inorder": [1, 2]},
                  {"preorder": [1, 2, 4, 5, 3, 6, 7], "inorder": [4, 2, 5, 1, 6, 3, 7]},
                  {"preorder": [1, 2, 3, 4], "inorder": [4, 3, 2, 1]}],
        "expect": {0: [3, 9, 20, N, N, 15, 7], 1: [-1]},
        "hints": [
            "The first value in `preorder` is always the root.",
            "Find the root in `inorder`. Everything to its left is the left subtree, and everything to its right is the right subtree. The sizes tell you how to split `preorder` too.",
            "Recurse on the two halves. To make it O(n), store each value's index in `inorder` in a dictionary, and walk through `preorder` with a shared index instead of slicing.",
        ],
        "ref": """
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root
""",
    },
    T("def maxPathSum(self, root: Optional[TreeNode]) -> int:",
      id="binary-tree-maximum-path-sum", title="Binary Tree Maximum Path Sum", difficulty="Hard",
      desc=f"""
A path in a binary tree is a sequence of nodes where each pair of neighbors is connected by an edge, and no node appears twice. The path does not need to pass through the root, and it must contain at least one node.

Given the `root` of a binary tree, return the largest possible sum of the values along a path.

{TREE_NOTE}

**Constraints**

- The tree has 1 to 3 * 10^4 nodes.
- `-1000 <= Node.val <= 1000`
""",
      tests=[{"root": [1, 2, 3]}, {"root": [-10, 9, 20, N, N, 15, 7]}, {"root": [-3]}, {"root": [2, -1]},
             {"root": [-2, -1]}, {"root": [5, 4, 8, 11, N, 13, 4, 7, 2, N, N, N, 1]}, {"root": [1, -2, 3]}],
      examples=3, expect={0: 6, 1: 42, 2: -3},
      hints=[
          "At every node, the best path that turns at that node is `node.val + (best downward path from the left) + (best downward path from the right)`.",
          "A downward path that would make the sum smaller should be dropped. Use `max(0, ...)` for each side.",
          "Write a DFS that returns the best single downward path starting at a node (`node.val + max(0, left, right)`), while updating a global best with the path that turns at that node.",
      ],
      ref="""
class Solution:
    def maxPathSum(self, root):
        best = -10**18
        def down(n):
            nonlocal best
            if not n:
                return 0
            a, b = max(0, down(n.left)), max(0, down(n.right))
            best = max(best, n.val + a + b)
            return n.val + max(a, b)
        down(root)
        return best
"""),
    {
        "id": "serialize-and-deserialize-binary-tree", "title": "Serialize and Deserialize Binary Tree",
        "difficulty": "Hard", "kind": "design", "class": "Codec",
        "desc": f"""
Design a `Codec` class with two methods:

- `serialize(root)` turns a binary tree into a string.
- `deserialize(data)` turns that string back into the same tree.

You can choose any string format. Each test serializes a tree, deserializes the result, and checks that you get back an identical tree.

{TREE_NOTE}

**Constraints**

- The tree has 0 to 10^4 nodes, with values from -1000 to 1000.
""",
        "starter": TREENODE + """class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass
""",
        "harness": """
def call(problem, ns, inp):
    data = ns["Codec"]().serialize(build_tree(inp["root"]))
    if not isinstance(data, str):
        raise TypeError(f"serialize() must return a str, but it returned {type(data).__name__}")
    return tree_to_values(ns["Codec"]().deserialize(data))
""",
        "tests": [{"root": [1, 2, 3, N, N, 4, 5]}, {"root": []}, {"root": [1]}, {"root": [-1, 0, 1000, -1000]},
                  {"root": [1, N, 2, N, 3, N, 4]}, {"root": [5, 4, 7, 3, N, 2, N, -1, N, 9]},
                  {"root": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}],
        "hints": [
            "A traversal alone loses information about where children are missing. How could you record missing children?",
            "Write a marker such as `N` for every `None` child. A preorder traversal with those markers describes the tree exactly.",
            "Serialize with a preorder DFS that writes values and `N` separated by commas. To deserialize, split on commas and rebuild with a recursive function that reads the next token: `N` means `None`, otherwise make a node and build its left, then right child.",
        ],
        "ref": """
class Codec:
    def serialize(self, root):
        out = []
        def go(n):
            if not n:
                out.append("N")
                return
            out.append(str(n.val))
            go(n.left)
            go(n.right)
        go(root)
        return ",".join(out)

    def deserialize(self, data):
        it = iter(data.split(","))
        def go():
            v = next(it)
            if v == "N":
                return None
            n = TreeNode(int(v))
            n.left = go()
            n.right = go()
            return n
        return go()
""",
    },
]
