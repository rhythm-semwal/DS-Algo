# Qs. Given a sorted array of integers A where every element appears twice except for one element which appears once,
# find and return this single element that appears only once.
#
# NOTE: Users are expected to solve this in O(log(N)) time.


class Solution1:
    # @param A : list of integers
    # @return an integer
    def singleNonDuplicate(self, nums) -> int:
        """
        EXPLANATION:-
        Suppose array is [1, 1, 2, 2, 3, 3, 4, 5, 5]
        we can observe that for each pair,
        first element takes even position and second element takes odd position
        for example, 1 is appeared as a pair,
        so it takes 0 and 1 positions. similarly for all the pairs also.

        this pattern will be missed when single element is appeared in the array.

        From these points, we can implement algorithm.
        1. Take left and right pointers .
            left points to start of list. right points to end of the list.
        2. find mid.
            if mid is even, then it's duplicate should be in next index.
            or if mid is odd, then it's duplicate  should be in previous index.
            check these two conditions,
            if any of the conditions is satisfied,
            then pattern is not missed,
            so check in next half of the array. i.e, left = mid + 1
            if condition is not satisfied, then the pattern is missed.
            so, single number must be before mid.
            so, update end to mid.
        3. At last return the nums[left]

        Time: -  O(logN)
        space:-  O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid

        return nums[left]


class Solution2:
    def singleNonDuplicate(self, nums) -> int:
        from collections import defaultdict
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        for key, value in hash_map.items():
            if value == 1:
                return key


if __name__ == '__main__':
     arr = [1, 1, 7]
     arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
     print(Solution1().singleNonDuplicate(arr))
