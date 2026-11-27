class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        def reach(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and heights[x][y] >= heights[r][c]:
                        seen.add((x, y))
                        stack.append((x, y))
            return seen
        pac = reach([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
        atl = reach([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
        return [[r, c] for r, c in sorted(pac & atl)]
