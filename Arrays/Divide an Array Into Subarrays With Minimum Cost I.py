# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        result = 0

        result += nums[0]

        new_array = nums[1:]

        new_array.sort()

        result += new_array[0] + new_array[1]

        return result

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        first_min = second_min = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < first_min:
                second_min = first_min
                first_min = nums[i]
            elif nums[i] < second_min:
                second_min = nums[i]


        return nums[0] + first_min + second_min
