class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        rotten = {(r, c) for r in range(m) for c in range(n) if grid[r][c] == 2}
        fresh = {(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1}
        t = 0
        while fresh:
            new = {(x, y) for (x, y) in fresh if any(p in rotten for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))}
            if not new:
                return -1
            fresh -= new
            rotten |= new
            t += 1
        return t
