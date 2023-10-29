class Solution:
    def rob(self, nums) -> int:

        if len(nums) < 2:
            return max(nums)

        # do not consider the first element
        current1, prev = 0, 0
        for i in range(1, len(nums)):
            current1, prev = max(current1, prev + nums[i]), current1

        # do not consider the last element
        current2, prev = 0, 0
        for i in range(len(nums) - 1):
            current2, prev = max(current2, prev + nums[i]), current2

        return max(current2, current1)