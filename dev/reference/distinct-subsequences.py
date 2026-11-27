class Solution:
    def numDistinct(self, s, t):
        @functools.lru_cache(None)
        def go(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            return go(i + 1, j) + (go(i + 1, j + 1) if s[i] == t[j] else 0)
        return go(0, 0)
