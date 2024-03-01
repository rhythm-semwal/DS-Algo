"""
Qs. https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution1:
    # Time: O(nlogk)
    # Space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappop, heappush, heapify

        heap = []
        heapify(heap)
        i = 0
        while i < k:
            heappush(heap, nums[i])
            i += 1

        for i in range(k, len(nums)):
            if nums[i] < heap[0]:
                continue
            else:
                heappop(heap)
                heappush(heap, nums[i])

        return heap[0]


class Solution2:
    """
    TLE error for the below solutions
    Time: O(nlgn + klgn) Space: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        while len(nums) > k:
            heappop(nums)
            heapify(nums)

        return nums[0]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
