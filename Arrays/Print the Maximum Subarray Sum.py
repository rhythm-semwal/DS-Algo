# https://www.geeksforgeeks.org/print-the-maximum-subarray-sum/

class Solution:
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')
        start_index, last_index = 0, 0

        for i in range(len(nums)):
            # this is the start of a subarray
            if current_sum == 0:
                start = i

            current_sum += nums[i]

            if current_sum < 0:
                current_sum = 0

            if current_sum > max_sum:
                max_sum = current_sum
                start_index = start
                last_index = i

        return nums[start_index:last_index+1]


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
print(Solution().maxSubArray(nums))




