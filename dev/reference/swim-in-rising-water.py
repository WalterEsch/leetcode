class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        def ok(t):
            if grid[0][0] > t:
                return False
            seen, stack = {(0, 0)}, [(0, 0)]
            while stack:
                r, c = stack.pop()
                if (r, c) == (n - 1, n - 1):
                    return True
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and grid[x][y] <= t:
                        seen.add((x, y))
                        stack.append((x, y))
            return False
        t = 0
        while not ok(t):
            t += 1
        return t
