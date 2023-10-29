class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        slow, fast = 0, 1
        ans = 0
        while fast < len(nums):
            if nums[fast] > nums[fast - 1]:
                fast += 1
            else:
                ans = max(ans, fast - slow)
                slow = fast
                fast = fast + 1

        return max(ans, fast - slow)