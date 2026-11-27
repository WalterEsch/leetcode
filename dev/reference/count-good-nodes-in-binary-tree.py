class Solution:
    def goodNodes(self, root):
        def go(n, m):
            if not n:
                return 0
            return (n.val >= m) + go(n.left, max(m, n.val)) + go(n.right, max(m, n.val))
        return go(root, root.val)
