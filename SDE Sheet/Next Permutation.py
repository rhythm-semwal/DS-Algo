class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Time complexity : O(n)O(n). In worst case, only two scans of the whole array are needed.
        Space complexity : O(1)O(1). No extra space is used. In place replacements are done

        Algo:
        1. start from the right and find the index position where element is less than its next element. This is the break point.
        2. start from the right and find the just greater element than the element at index in 1st step
        3.swap both the elements
        4.reverse the elements from index in 1st step till th last.
        5. the edge case if the array is in desc order, then we just need to reverse the array.
        """
        index1, index2 = -1, -1
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        start, end = i + 1, n - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums

