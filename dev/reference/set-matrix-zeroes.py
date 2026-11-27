class Solution:
    def setZeroes(self, matrix):
        rows = {r for r, row in enumerate(matrix) for v in row if v == 0}
        cols = {c for row in matrix for c, v in enumerate(row) if v == 0}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0
