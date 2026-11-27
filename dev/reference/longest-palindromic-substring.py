class Solution:
    def longestPalindrome(self, s):
        best = ""
        for i in range(len(s)):
            for j in range(i + len(best) + 1, len(s) + 1):
                t = s[i:j]
                if t == t[::-1]:
                    best = t
        return best
