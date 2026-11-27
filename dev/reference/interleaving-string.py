class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        @functools.lru_cache(None)
        def go(i, j):
            if i + j == len(s3):
                return True
            return (i < len(s1) and s1[i] == s3[i + j] and go(i + 1, j)) or \
                   (j < len(s2) and s2[j] == s3[i + j] and go(i, j + 1))
        return go(0, 0)
