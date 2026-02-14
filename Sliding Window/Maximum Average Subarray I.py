# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = 0, 0
        max_average = float('-inf')
        running_sum = 0

        while end < len(nums):
            running_sum += nums[end]

            if end-start+1 == k:
                max_average = max(max_average, running_sum/k)
                running_sum -= nums[start]
                start += 1
            
            end += 1
        
        return max_average
