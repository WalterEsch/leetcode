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
