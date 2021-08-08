class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        result = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1] or A[i] < A[i-1]:
                value = (A[i-1]+1)-A[i]
                result += value
                A[i] = A[i]+ value
        # print(result)
        return result