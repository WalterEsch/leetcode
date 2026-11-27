class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        cells = sorted((matrix[r][c], r, c) for r in range(m) for c in range(n))
        best = {}
        for v, r, c in reversed(cells):
            best[(r, c)] = 1 + max([best[(x, y)] for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > v] or [0])
        return max(best.values())
