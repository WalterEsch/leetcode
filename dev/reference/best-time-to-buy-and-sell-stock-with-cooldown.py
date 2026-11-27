class Solution:
    def maxProfit(self, prices):
        @functools.lru_cache(None)
        def go(i, holding):
            if i >= len(prices):
                return 0
            skip = go(i + 1, holding)
            if holding:
                return max(skip, prices[i] + go(i + 2, False))
            return max(skip, -prices[i] + go(i + 1, True))
        return go(0, False)
