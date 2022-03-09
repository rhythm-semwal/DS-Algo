from ast import List


class Solution:
    def minSubArrayLen(self, target, nums):
        start, end = 0, 0

        min_window_length = float('inf')
        running_sum = 0

        while end < len(nums):
            running_sum += nums[end]
            while running_sum >= target:
                min_window_length = min(min_window_length, end-start+1)
                running_sum -= nums[start]
                start += 1
            end += 1
        
        return 0 if min_window_length == float('inf') else min_window_length

if __name__ == '__main__':
    target = 8
    nums = [1,4]
    print(Solution().minSubArrayLen(target, nums))
