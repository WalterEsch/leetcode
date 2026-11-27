class Solution:
    def missingNumber(self, nums):
        return (set(range(len(nums) + 1)) - set(nums)).pop()
