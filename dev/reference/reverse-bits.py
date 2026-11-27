class Solution:
    def reverseBits(self, n):
        return int(format(n, "032b")[::-1], 2)
