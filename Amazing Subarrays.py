class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowel_set = ('a','e','i','o','u')
        A = A.lower()
        result = 0
        length = len(A)
        for i in range(len(A)):
            if A[i] in vowel_set:
                result += length - i

        print(result%10003)


if __name__ == "__main__":
    word = "ABEC"
    Solution().solve(word)

