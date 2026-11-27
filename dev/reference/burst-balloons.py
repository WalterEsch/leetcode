class Solution:
    def maxCoins(self, nums):
        a = [1] + nums + [1]
        @functools.lru_cache(None)
        def go(l, r):
            return max((a[l] * a[k] * a[r] + go(l, k) + go(k, r) for k in range(l + 1, r)), default=0)
        return go(0, len(a) - 1)
