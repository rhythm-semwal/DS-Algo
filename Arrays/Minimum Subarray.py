class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        cum_sum = 0
        min_sum = float('inf')

        for num in nums:
            cum_sum += num

            min_sum = min(min_sum, cum_sum, num)

            if cum_sum > 0:
                cum_sum = 0

        return min_sum