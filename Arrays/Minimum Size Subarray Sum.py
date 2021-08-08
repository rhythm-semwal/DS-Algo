class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        slow, fast = 0, 0
        min_window_length = float('inf')
        current_sum = 0

        while fast < len(nums):
            current_sum += nums[fast]

            while current_sum >= s:
                min_window_length = min(min_window_length, fast-slow+1)
                current_sum -= nums[slow]
                slow += 1

            fast += 1

        return -1 if min_window_length == float('inf') else min_window_length


target = 7
nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]
# target = 11
# nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums))
