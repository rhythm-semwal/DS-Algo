class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum, right_sum = 0, sum(nums)

        for index, value in enumerate(nums):
            right_sum -= value

            if left_sum == right_sum:
                return index

            left_sum += value

        return -1
