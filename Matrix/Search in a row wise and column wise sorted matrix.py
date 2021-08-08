class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import sys
        row, col = len(A), len(A[0]) - 1
        i, j = 0, col
        result = sys.maxsize
        while i < row and j >= 0:
            if A[i][j] == B:
                result = min(result, (((i + 1) * 1009) + (j + 1)))
                i += 1

            elif A[i][j] < B:
                i += 1
            elif A[i][j] > B:
                j -= 1
        if result == sys.maxsize:
            return -1
        return result