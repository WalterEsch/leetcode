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
