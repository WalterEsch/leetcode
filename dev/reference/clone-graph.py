class Solution:
    def cloneGraph(self, node):
        copies = {}
        def go(n):
            if n in copies:
                return copies[n]
            c = Node(n.val)
            copies[n] = c
            c.neighbors = [go(x) for x in n.neighbors]
            return c
        return go(node) if node else None
