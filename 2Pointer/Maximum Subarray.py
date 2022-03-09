from typing import List


class Solution:
    # Solution way 1
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            # this condition handles the case when all the elements in the array are negative
            if current_sum < nums[i]:
               current_sum = nums[i]
            
            max_sum = max(max_sum, current_sum)
        
        return max_sum

    # Solution way 2
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

            # this condition works only when the all the elements in the array are positive
            if current_sum < 0:
               current_sum =0
                    
        return max_sum
