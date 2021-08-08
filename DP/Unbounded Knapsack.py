class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer

    # DP
    def solve(self, A, B, C):
        lookup_table = [0 for _ in range(A + 1)]
        for i in range(A + 1):
            for j in range(len(B)):
                if C[j] <= i:
                    lookup_table[i] = max(lookup_table[i], lookup_table[i - C[j]] + B[j])

        return lookup_table[A]

    # recursive
    # def knapsack(self, A, B, C, n):
    #     if n == 0:
    #         return 0
    #     if A == 0:
    #         return 0

    #     if C[n-1] <= A:
    #         return max((B[n-1] + self.knapsack(A - C[n-1], B, C, n)), self.knapsack(A,B, C, n-1))
    #     else:
    #         return self.knapsack(A, B, C, n - 1)

    # def solve(self, A, B, C):
    #     import sys
    #     sys.setrecursionlimit(10**9)
    #     return self.knapsack(A, B, C, len(B))