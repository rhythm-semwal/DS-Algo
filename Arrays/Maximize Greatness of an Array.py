class Solution:
    def maximizeGreatness(self, nums) -> int:
        nums.sort()

        count = 0

        for num in nums:
            if num > nums[count]:
                count += 1

        return count
