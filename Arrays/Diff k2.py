class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        hash_set = set()

        for i in range(len(A)):
            if A[i] + B in hash_set or A[i] - B in hash_set:
                return 1
            else:
                hash_set.add(A[i])
        return 0
