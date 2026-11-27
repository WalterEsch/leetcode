class Solution:
    def singleNumber(self, nums):
        return [x for x, c in collections.Counter(nums).items() if c == 1][0]
