from typing import List


class Solution:
    """
    In this approach instead of storing the result in a third array, we know that median value i.e either n/2
    or n/2-1.
    So we can just get the value of these index position using 2 pointers
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        index1 = n // 2
        index2 = index1 - 1

        index1_element = -1
        index2_element = -1

        i, j = 0, 0

        count = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if count == index1:
                    index1_element = nums1[i]
                if count == index2:
                    index2_element = nums1[i]

                count += 1
                i += 1
            else:
                if count == index1:
                    index1_element = nums2[j]
                if count == index2:
                    index2_element = nums2[j]

                count += 1
                j += 1

        while i < n1:
            if count == index1:
                index1_element = nums1[i]
            if count == index2:
                index2_element = nums1[i]

            count += 1
            i += 1

        while j < n2:
            if count == index1:
                index1_element = nums2[j]
            if count == index2:
                index2_element = nums2[j]

            count += 1
            j += 1

        if n % 2 == 1:
            return index1_element
        else:
            return (index1_element + index2_element) / 2