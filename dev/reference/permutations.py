class Solution:
    def permute(self, nums):
        return [list(p) for p in itertools.permutations(nums)]
