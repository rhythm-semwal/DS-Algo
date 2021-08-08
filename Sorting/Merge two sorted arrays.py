class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        result = list()
        i, j = 0, 0

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            elif B[j] < A[i]:
                result.append(B[j])
                j += 1
            else:
                result.append(A[i])
                result.append(B[j])
                i += 1
                j += 1
        if j < len(B):
            while j < len(B):
                result.append(B[j])
                j += 1
        if i < len(A):
            while i < len(A):
                result.append(A[i])
                i += 1

        return result