class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    # this solution is for when the min sum is 0 if all elements are -ve
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


# this solution is for when we just have to find the min sum irrespective of +ve or -ve elements
class Solution:
    def maxSubArraySum(self, a, size):
        ans = a[0]
        max_so_far = a[0]
        for i in range(1, size):
            max_so_far = max(a[i], max_so_far + a[i])

            if max_so_far > ans:
                ans = max_so_far

        return ans