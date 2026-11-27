class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0 or (r, c) in seen:
                return 0
            seen.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        return max(dfs(r, c) for r in range(m) for c in range(n))
