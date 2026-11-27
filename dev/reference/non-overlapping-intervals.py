class Solution:
    def eraseOverlapIntervals(self, intervals):
        iv = sorted(intervals)
        @functools.lru_cache(None)
        def keep(i, prev_end):
            if i == len(iv):
                return 0
            best = keep(i + 1, prev_end)
            if iv[i][0] >= prev_end:
                best = max(best, 1 + keep(i + 1, iv[i][1]))
            return best
        return len(iv) - keep(0, -10**9)
