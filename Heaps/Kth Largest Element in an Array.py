"""
Qs. https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    """
    TLE error for the below solutions
    Time: O(nlgn + klgn) Space: O(n)
    """
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        # max_heap = []
        # heapify(max_heap)

        # for i in nums:
        #     heappush(max_heap, i*-1)
        #     heapify(max_heap)

        # while k > 1:
        #     heappop(max_heap)
        #     heapify(max_heap)
        #     k -= 1

        # return max_heap[0] * -1

        heapify(nums)

        while len(nums) > k:
            heappop(nums)
            heapify(nums)

        return nums[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        Time: O(nlogk)
        Space: O(k)
        """
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heappop(minheap)
                    heappush(minheap, num)
        return minheap[0]


nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest2(nums, k))
