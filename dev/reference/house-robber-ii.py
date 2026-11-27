class Solution:
    def rob(self, nums):
        def line(arr):
            a = b = 0
            for x in arr:
                a, b = b, max(b, a + x)
            return b
        return nums[0] if len(nums) == 1 else max(line(nums[1:]), line(nums[:-1]))
