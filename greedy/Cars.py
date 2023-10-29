from functools import cmp_to_key
import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def time_cmp(self, A, B):
        if A[0] < B[0]:
            return -1
        elif A[0] == B[0]:
            if A[1] > B[1]:
                return 1
            else:
                return -1
        else:
            return 1

    def solve(self, A, B):

        profit_cmp_key = cmp_to_key(self.time_cmp)
        zipped_array = list(zip(A, B))

        zipped_array.sort(key=profit_cmp_key)

        time_count = 0
        profit = 0
        heap_list = []
        heapq.heapify(heap_list)
        for i in range(len(zipped_array)):
            if time_count < zipped_array[i][0]:
                profit += zipped_array[i][1]
                time_count += 1
                heapq.heappush(heap_list, zipped_array[i][1])
                heapq.heapify(heap_list)
            else:
                if zipped_array[i][1] > heap_list[0]:
                    min = heapq.heappop(heap_list)
                    profit -= min
                    profit += zipped_array[i][1]
                    heapq.heappush(heap_list, zipped_array[i][1])
                    heapq.heapify(heap_list)
        print(profit)


A = [1, 3, 2, 3, 3]
B = [5, 6, 1, 3, 9]
print(Solution().solve(A, B))
