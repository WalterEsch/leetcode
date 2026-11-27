class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        seen, stack = {0}, [0]
        while stack:
            for y in g[stack.pop()]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        return len(seen) == n
