class Solution:
    def countSubstrings(self, s):
        return sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
