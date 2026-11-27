class Solution:
    def spiralOrder(self, matrix):
        res = []
        m = [row[:] for row in matrix]
        while m:
            res += m.pop(0)
            m = [list(r) for r in zip(*m)][::-1]
        return res
