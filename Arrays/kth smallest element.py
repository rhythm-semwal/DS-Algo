# TC = O(n + kLogn)

class Solution1:
    def kthSmallest(self, arr, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        from heapq import heapify, heappush, heappop
        min_heap = []
        heapify(min_heap)

        for i in arr:
            heappush(min_heap, i)
            heapify(min_heap)

        while k > 1:
            heappop(min_heap)
            heapify(min_heap)
            k -= 1

        print(min_heap[0])

class Solution2:
    def kthSmallest(self, arr, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()

        return arr[k-1]


arr = [7, 10, 4, 3, 20, 15]
K = 3
print(Solution1().kthSmallest(arr, K))