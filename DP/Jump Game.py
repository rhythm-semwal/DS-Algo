# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums) -> bool:

        if len(nums) == 1:
            return True
        reachable, current_index = 0, 0

        while current_index < len(nums):
            if current_index > reachable:
                return False

            reachable = max(nums[current_index] + current_index, reachable)
            current_index += 1

        return True


nums = [2,0,0]
print(Solution().canJump(nums))