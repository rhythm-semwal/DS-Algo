class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        n1 = len(A)
        n2 = len(B)
        n3 = len(C)
        i, j, k = 0, 0, 0
        import sys
        ans = sys.maxsize
        while i < n1 and j < n2 and k < n3:
            ans = min(ans, max(A[i], B[j], C[k])-min(A[i], B[j], C[k]))

            if A[i] <= B[j] and A[i] <= C[k]:
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                j += 1
            elif C[k] <= B[j] and C[k] <= A[i]:
                k += 1

        print(ans)


# A = [1, 4, 10]
# B = [2, 15, 20]
# C = [10, 12]

# A = [3, 5, 6]
# B = [2]
# C = [3, 4]

A = [1,4,5,8,20]
B = [6,9,15]
C = [2,3,6,6]
Solution().minimize(A, B, C)
