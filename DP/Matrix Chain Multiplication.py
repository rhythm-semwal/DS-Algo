class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        lookup_table = [[0 for _ in range(n)] for _ in range(n)]

        # base case for length = 1 ans = 0
        for i in range(n):
            lookup_table[i][i] = 0

        import sys
        # chain length
        for L in range(2, n):
            # no of time i loop will run or posiiton of the left pointer
            for i in range(1, n - L + 1):
                # position of right pointer wrt to left pointer
                j = L + i - 1
                lookup_table[i][j] = sys.maxsize
                # same loop as in the recursive code
                for k in range(i, j):
                    # for finding for (1,2) this is equal to (1,1) + (2,2). Below piece does the same task
                    count = lookup_table[i][k] + lookup_table[k + 1][j] + (A[i - 1] * A[k] * A[j])
                    lookup_table[i][j] = min(count, lookup_table[i][j])
        # n-1 because if n is the number of elements then n-1 are the possible matrices
        return lookup_table[1][n - 1]
    # def mcm(self, A, left, right, result):
    #     if left == right:
    #         return 0

    #     for i in range(left, right):
    #         count = self.mcm(A, left, i, result) + self.mcm(A, i+1, right, result) + (A[left-1]*A[i]*A[right])

    #         result = min(result, count)

    #     return result

    # def solve(self, A):
    #     result = float('inf')
    #     return self.mcm(A, 1, len(A)-1, result)
