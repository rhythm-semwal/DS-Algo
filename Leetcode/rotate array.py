from typing import List


class Solution:
    def reverse_array(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        n = len(nums)
        k = k % n

        self.reverse_array(nums, 0, n - 1)
        self.reverse_array(nums, 0, k - 1)
        self.reverse_array(nums, k, n - 1)

        print(nums)


# nums = [1,2,3,4,5,6,7]
# k = 3
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)