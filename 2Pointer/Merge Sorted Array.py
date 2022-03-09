from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if the second array is empty, there's nothing to do
        if nums2:
            p1, p2 = 0, 0

            while p1 < m and p2 < n:
                if nums1[p1] > nums2[p2]:
                    # insert the current element of nums2 into nums1 at the current
                    # position of nums1 that we are inspecting
                    nums1.insert(p1, nums2[p2])
                    p2 += 1
                    m += 1
                # and we always move the nums1 pointer because either the current value of nums1 
                # is in the correct position or it was moved one poistion further in the array 
                # to accomodate one value from nums2
                p1 += 1
            
            # finally, if we didn't reach the end of nums2
            if p2 < n:
                # replace all the zeros at the end of nums1 with the rest of the values of nums2 
                # that are not in nums1
                nums1[m:] = nums2[p2:]
            else:
                # otherwise, we inserted all `n` elements of nums2 into nums1 and,
                # in this case, we need to delete the last `n` elements of nums1 
                # (they are the zeros that we pushed back to acomodate the nums2 values)
                del nums1[-n:]
            
        return nums1

if __name__ == '__main__':
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(Solution().merge(nums1, m, nums2, n))
