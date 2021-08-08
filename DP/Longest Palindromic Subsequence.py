class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        # base case - string of length 1 are palindrome and i > j so all the values where i > j those grid are of no use
        for i in range(n):
            dp[i][i] = 1

        for substr_length in range(2, n+1):  # this loop will tell the substring length to consider
            for i in range(n-substr_length+1):
                j = i+substr_length-1
                # if string is palindrome and substring length is 2 that means length of palindrome will be 2
                if A[i] == A[j] and substr_length == 2:
                    dp[i][j] = 2
                # if string is palindrome and substring length is > 2 that means length of palindrome will be value in
                # left diagonal + 2 because initially that is the value that is filled with base case and then build on
                # that
                # eg string = aeda{index = 0-3). string is palindrome for index 0 and 3
                # then ans will be = ans for index1,2 + 2
                elif A[i] == A[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                # if string is not palindrome then consider max of (value just below it or before it)
                # for eg if string is  = aedd(index = 0-3). this is not palindrome and hence ans will be max of ([1,3] or [0, 2])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        print(dp[0][n-1])


    # using LCS of the given string and reversing the given string
    # def solve(self, A):
    #     B = A[::-1]
    #
    #     print(B)
    #     row, col = len(A)+1, len(B)+1
    #
    #     dp = [[0 for _ in range(col)] for _ in range(row)]
    #
    #     i_index = 0
    #     for i in range(1, row):
    #         j_index = 0
    #         for j in range(1, col):
    #             if A[i_index] == B[j_index]:
    #                 dp[i][j] = 1+dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #
    #             j_index += 1
    #         i_index += 1
    #
    #     print(dp[-1][-1])



A = "bebeeed"
Solution().solve(A)



