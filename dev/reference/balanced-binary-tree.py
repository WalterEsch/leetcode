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
