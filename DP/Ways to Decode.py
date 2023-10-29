class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        ways = [0] * (len(A))

        if int(A[0]) > 0:
            ways[0] = 1

        for i in range(1, len(A)):
            if int(A[i]) > 0:
                ways[i] += ways[i - 1]

            if 10 <= int(A[i - 1]) * 10 + int(A[i]) <= 26:
                if i == 1:
                    ways[i] += 1
                else:
                    ways[i] += ways[i - 2]

        print(ways[-1]%1000000009)


A = "123"
Solution().numDecodings(A)
