class Solution:
    def change(self, amount, coins):
        @functools.lru_cache(None)
        def go(i, a):
            if a == 0:
                return 1
            if i == len(coins) or a < 0:
                return 0
            return go(i, a - coins[i]) + go(i + 1, a)
        return go(0, amount)
