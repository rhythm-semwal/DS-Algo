from heapq import heapify, heappush, heappop
from typing import List

"""
Let's say we have some stream of numbers, nums = [6, 2, 3, 1, 7], and k = 3. Because the input is small, we can clearly see the kth smallest element is 3. Although, earlier we said that a heap can only find an element in O(1)O(1)O(1) time if it's a minimum or maximum (depending on choice of implementation). Well, a heap is also capable of removing the smallest element quickly, so what if we just keep removing the smallest element from nums until nums.length == k? In this case, we would have nums = [3, 6, 7], and a heap can now give us our answer in O(1)O(1)O(1) time.

That's the key to solving this problem - use a min-heap (min means that the heap will remove/find the smallest element, a max heap is the same thing but for the largest element) and keep the heap at size k. That way, the smallest element in the heap (the one we can access in O(1)O(1)O(1)) will always be the kth largest element. This way, when adding a number to the heap with add(), we can do it very quickly in log⁡(n)\log(n)log(n) time. If our heap exceeds size k, then we can also remove it very quickly. In the end, the smallest element in the heap will be the answer.

Algorithm

In the constructor, create a min heap using the elements from nums. Then, pop from the heap until heap.length == k.

For every call to add():

First, push val into heap.
Next, check if heap.length > k. If so, pop from the heap.
Finally, return the smallest value from the heap, which we can get in O(1)O(1)O(1) time.
"""

"""
Time complexity: O(N⋅log(N)+M⋅log(k))
Space complexity: O(N)O(N)O(N)
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        TC of this constructor = O(N+N⋅log(N))=O(N⋅log(N))
        """
        self.heap = nums
        ''' Below step takes O(N)'''
        heapify(self.heap)
        self.k = k

        '''
        we need to remove from the heap until there are only k elements in it,  which means removing N - k elements. 
        Since k can be, say 1, in terms of big O this is N operations, with each operation costing log(N). 
        Total = O(N.log(N))
        '''
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:

        heappush(self.heap, val)
        '''
        heappush step takes O(log(k)) time for adding a new value and M calls will take O(M.log(k))
        '''
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)