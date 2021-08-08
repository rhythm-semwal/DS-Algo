class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        for i in range(B):
            # min_index = i
            max_index = i
            for j in range(i+1, len(A)):
                # if A[min_index] > A[j]:
                if A[max_index] < A[j]:
                    # min_index = j
                    max_index = j
            # A[i], A[min_index] = A[min_index], A[i]
            A[i], A[max_index] = A[max_index], A[i]
        print(A)


A = [3,2,4,5,6]
B = 2
Solution().kthsmallest(A, B)
