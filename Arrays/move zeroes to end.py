# @type of arr: list of integers
# @return type: list of integers
from typing import List


class Solution:
    def moveZeroes(self, arr: List[int]):
        zeros = 0
        for index, value in enumerate(arr):
            if value != 0:
                arr[zeros], arr[index] = arr[index], arr[zeros]
                zeros += 1
        print(arr)

arr =  [1, 8, 0, 2, 0, 1, 13, 0]
Solution().moveZeroes(arr)