class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A, B):
        str_length = len(A)
        result = ""
        # for i in range(str_length-B, str_length):
        #     result += A[i]
        # # print(result)
        #
        # for i in range(0, str_length-B):
        #     result += A[i]
        #
        # print(result)
        result += A[str_length-B:] + A[:str_length-B]
        print(result)


if __name__ == "__main__":
    word = "academy"
    k = 3
    Solution().solve(word, k)
