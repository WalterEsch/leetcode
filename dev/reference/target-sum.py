class Solution:
    def findTargetSumWays(self, nums, target):
        return sum(1 for signs in itertools.product((1, -1), repeat=len(nums))
                   if sum(s * x for s, x in zip(signs, nums)) == target)
