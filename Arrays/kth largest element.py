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
    # TC = O(nlgn + klgn)
    def kthLargestElement(self, k, nums):
        # write your code here
        if not nums or not k or k < 0:
            return None

        from heapq import heappush, heappop
        max_heap = []

        for i in nums:
            heappush(max_heap, i*-1)

        while k > 1:
            heappop(max_heap)
            k -= 1

        return max_heap[0]*-1


# minheap, add k element to minheap, if nums[i] > minheap[0], then pop and add it, else pass.
#  Time: O(nlgk) Space: O(k) Runtime: 78%
class Solution3:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        if not nums or not k or k < 0:
            return None

        from heapq import heappush, heappop

        minheap = []
        for num in nums:
            if len(minheap) < k:
                heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heappop(minheap)
                    heappush(minheap, num)

        return minheap[0]


k = 2
nums = [3,2,1,5,6,4]
# nums = [-10, -40, -25, -12, -25, -10]
print(Solution3().kthLargestElement(k, nums))
