class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        max_rooms = 0
        room = []

        import heapq
        A.sort(key=lambda x: x[0])

        for i in range(len(A)):
            heapq.heappush(room, A[i][1])
            while room[0] <= A[i][0]:
                heapq.heappop(room)
            max_rooms = max(max_rooms, len(room))

        return max_rooms

A =  [     [1, 18],
            [18, 23],
            [15, 29],
            [4, 15],
            [2, 11],
            [5, 13]
      ]

# A = [      [0, 30],
#             [5, 10],
#             [15, 20]
#      ]
print(Solution().solve(A))
