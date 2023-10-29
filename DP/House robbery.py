from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # approach 1
        # if not nums:
        #     return 0
        #
        # current, prev = nums[0], 0
        #
        # for i in range(1, len(nums)):
        #
        #     current, prev = max(nums[i]+prev, current), current
        #
        # return current

        # approach 2
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


nums = [2,1,1,2]
print(Solution().rob(nums))
