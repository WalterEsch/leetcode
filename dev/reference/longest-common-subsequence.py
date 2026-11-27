class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @functools.lru_cache(None)
        def go(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + go(i + 1, j + 1)
            return max(go(i + 1, j), go(i, j + 1))
        return go(0, 0)
