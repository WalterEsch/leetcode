class Solution:
    def partition(self, s):
        if not s:
            return [[]]
        res = []
        for j in range(1, len(s) + 1):
            if s[:j] == s[:j][::-1]:
                res += [[s[:j]] + rest for rest in self.partition(s[j:])]
        return res
