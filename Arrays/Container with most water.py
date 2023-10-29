class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        i, j = 0, n - 1
        result = 0
        while i < j:
            result = max(result, min(A[i], A[j]) * (j - i))

            # if A[i] is less than A[j] then move forward bcoz min area is already calculated
            if A[i] <= A[j]:
                i += 1
            # same as above case
            else:
                j -= 1

        return result
