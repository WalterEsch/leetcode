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
