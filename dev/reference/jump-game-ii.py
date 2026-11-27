class Solution:
    def jump(self, nums):
        n = len(nums)
        best = [0] + [float("inf")] * (n - 1)
        for i in range(n):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                best[j] = min(best[j], best[i] + 1)
        return best[-1]
