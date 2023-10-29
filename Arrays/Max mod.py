class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        import sys
        first, second = -sys.maxsize, -sys.maxsize

        for i in range(len(A)):
            if A[i] > first:
                second = first
                first = A[i]

            if A[i] > second and A[i] != first:
                second = A[i]

        if second != -sys.maxsize:
            return second
        return 0