from bisect import bisect_left
from typing import List

# Intuition
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/?envType=daily-question&envId=2024-01-05


class Solution:
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for index, num in enumerate(nums):
            if index == 0 or num > result[-1]:
                result.append(num)
            else:
                # idx = bisect_left(result, num)
                idx = self.binary_search(result, num)
                result[idx] = num

        return len(result)
