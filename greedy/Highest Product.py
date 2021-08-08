class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        n = len(A)
        if n < 3:
            return 0

        A.sort()
        return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])