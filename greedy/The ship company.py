from heapq import heappop, heappush, heapify


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        ans = []
        min_heap, max_heap = [], []
        heapify(min_heap)
        heapify(max_heap)

        for i in range(B):
            heappush(min_heap, C[i])
            heappush(max_heap, -1 * C[i])

        min_result = 0
        for i in range(A):
            element = heappop(min_heap)
            # print("min element = ", element)
            min_result += element
            if element > 1:
                heappush(min_heap, element - 1)

        max_result = 0
        for i in range(A):
            element = -1 * heappop(max_heap)
            # print("max element = ", element)
            max_result += element
            if element > 1:
                heappush(max_heap, -1 * (element - 1))

        ans.append(max_result)
        ans.append(min_result)

        return ans