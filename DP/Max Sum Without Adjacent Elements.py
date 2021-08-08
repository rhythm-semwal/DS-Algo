class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        max_array = []

        n = len(A[0])
        print(n)
        for i in range(n):
            max_array.append(max(A[0][i], A[1][i]))

        current, prev = max_array[0], 0

        for i in range(1, len(max_array)):
            current,prev = max(max_array[i]+prev, current), current

        print(current)

A = [
        [1, 2, 3, 4],
        [2, 3, 4, 5]
     ]
Solution().adjacent(A)
