class Solution:
    def isSubtree(self, root, subRoot):
        def ser(n):
            return f"({n.val},{ser(n.left)},{ser(n.right)})" if n else "#"
        return ser(subRoot) in ser(root)
