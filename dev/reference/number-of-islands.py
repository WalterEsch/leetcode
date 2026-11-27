class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    stack = [(r, c)]
                    seen.add((r, c))
                    while stack:
                        a, b = stack.pop()
                        for x, y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1" and (x, y) not in seen:
                                seen.add((x, y))
                                stack.append((x, y))
        return count
