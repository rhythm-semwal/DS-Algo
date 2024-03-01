from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        """
        creating a shallow copy of the array
        creating a shallow copy will work here because we don't have 
        nested structure here so deep copy is not required
        """

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:

        arr = self.nums[:]  # list(self.nums) - this also creates a shallow copy.
        """
        then reason why we do arr = self.nums[:] istead of arr = self.nums is
        When you use arr = self.nums, 
        both arr and self.nums will refer to the same list object. 
        This means that if you modify arr 
        (e.g., by swapping elements in the Fisher-Yates shuffle algorithm), 
        it will also modify self.nums because they are referencing the same underlying list. 
        This behavior may lead to unexpected side effects, 
        especially if you want to maintain the original order of the numbers.
        """
        n = len(arr)

        for i in range(n):
            j = random.randrange(i, n)
            arr[i], arr[j] = arr[j], arr[i]

        return arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
