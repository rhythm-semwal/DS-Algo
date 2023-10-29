class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        cum_sum = 0
        max_sum = float('-inf')

        for i in nums:
            cum_sum += i

            max_sum = max(cum_sum, i, max_sum)

            if cum_sum < 0:
                cum_sum = 0

        return max_sum
