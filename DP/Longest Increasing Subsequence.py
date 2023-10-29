class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        if n == 0:
            return 0
        # for all the elements min increasing subsequence will always be 1
        lookup_table = [1]*n

        # i, j = 1, 0
        # starting from 1 because for 0th element the ans will be 1 always
        for i in range(1, n):
            j = 0
            while j < i:
                if A[j] < A[i]:
                    lookup_table[i] = max(lookup_table[i], lookup_table[j] + 1)

                j += 1

        return max(lookup_table)


A = [5,4,1,2,3]
# A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# A = [1, 2, 1, 5]
Solution().lis(A)

