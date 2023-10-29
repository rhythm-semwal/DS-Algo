from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        i, j = 0, 0

        while i < m and j < n:
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                m += 1
                j += 1
            else:
                i += 1

        if j < len(nums2):
            nums1[m:] = nums2[j:]
        else:
            del nums1[m:]