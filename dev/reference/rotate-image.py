class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        rotated = [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]
        for r in range(n):
            matrix[r][:] = rotated[r]
