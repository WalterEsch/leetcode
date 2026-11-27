class Solution:
    def minInterval(self, intervals, queries):
        return [min((r - l + 1 for l, r in intervals if l <= q <= r), default=-1) for q in queries]
