# Solution 1
"""
TC = O(N*k)
SC = O(1)
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        result = []
        for i in range(len(A) - B + 1):
            ans = A[i]
            for j in range(1, B):
                ans = max(ans, A[i + j])

            result.append(ans)

        print(result)


# Solution 2
"""
TC = O(N)
SC = O(k)
"""
from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        n = len(A)
        queue = deque()
        for i in range(B):
            while queue and A[i] >= A[queue[-1]]:
                queue.pop()

            queue.append(i)

        result = []
        for i in range(B, n):
            result.append(A[queue[0]])

            while queue and queue[0] <= i - B:
                queue.popleft()

            while queue and A[i] >= A[queue[-1]]:
                queue.pop()

            queue.append(i)

        result.append(A[queue[0]])
        return result
