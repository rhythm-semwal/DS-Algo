# TC = O(N)
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zero_count = 0
        max_length = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
            
                start += 1
                
            max_length = max(max_length, end-start+1)
        
        return max_length - 1
