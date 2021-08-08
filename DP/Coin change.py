class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # DP solution - TC = O(N^2), SC = O(N^2)
    # def coinchange2(self, A, B):
    #     lookup_table = [0 for _ in range(B+1)]
    #
    #     # base case when coins =0 and target sum = 0
    #     lookup_table[0] = 1
    #
    #     for i in range(len(A)):
    #         for j in range(A[i], B+1):
    #             lookup_table[j] += lookup_table[j-A[i]]
    #
    #     print(lookup_table)
    def coinchange2(self, A, B):
        n = len(A)
        lookup_table = [[0 for _ in range(n)] for _ in range(B+1)]

        # base case, when B == 0
        for i in range(n):
            lookup_table[0][i] = 1

        for i in range(1, B+1):
            for j in range(n):
                # if i am considering the current coin then B will decrease and n would remain same
                x = lookup_table[i-A[j]][j] if i-A[j] >= 0 else 0
                # if i am not considering the current coin then B will remain same and n would decrease

                y = lookup_table[i][j-1] if j >= 1 else 0
                lookup_table[i][j] = x + y

        return lookup_table[B][n - 1]
    # recursive solution
    # def solve(self, coins, target, n):
    #       n = len(A)

    #     if target == 0:
    #         return 1
    #
    #     if target < 0:
    #         return 0
    #
    #     if n <= 0 and target > 0:
    #         return 0
    #
    #     return self.solve(coins, target, n-1) + self.solve(coins, target-coins[n-1], n)
    #
    # def coinchange2(self, A, B):
    #     return self.solve(A, B , len(A))


A = [1,2,5]
B = 11
print(Solution().coinchange2(A, B))
