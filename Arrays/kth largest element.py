import sys


class Solution1:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here
        result = 0
        while k > 0:
            max_num = -sys.maxsize

            for i in range(len(nums)):
                if nums[i] > max_num:
                    max_num = nums[i]
                    position = i
            nums.pop(position)
            result = max_num
            k -= 1

        print(result)


class Solution2:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    # TC = O(n + kLogn)
    def kthLargestElement(self, k, nums):
        # write your code here

        from heapq import heapify, heappush, heappop
        max_heap = []
        heapify(max_heap)

        for i in nums:
            heappush(max_heap, i*-1)
            heapify(max_heap)

        while k > 1:
            heappop(max_heap)
            heapify(max_heap)
            k -= 1

        return max_heap[0]*-1

k = 3
nums = [9,3,2,4,8]
print(Solution1().kthLargestElement(k, nums))