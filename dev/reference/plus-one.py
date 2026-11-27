class Solution:
    def plusOne(self, digits):
        return [int(c) for c in str(int("".join(map(str, digits))) + 1)]
