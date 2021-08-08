class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        from collections import deque
        queue = deque()
        for i in range(B):
            queue.append(A[i])

        for i in range(B):
            A[i] = queue.pop()

        print(A)

# A = [1, 2, 3, 4, 5]
# B = 3
A = [1,2,3]
B = 1
Solution().solve(A, B)
