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
