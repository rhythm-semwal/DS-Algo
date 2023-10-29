class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)-2):
            if A[i] == 'b':
                if A[i+1] == 'o' and A[i+2] == 'b':
                    count += 1

        print(count)


if __name__ == "__main__":
    # word = 'abobc'
    # word = 'bobbob'
    word = "scaler"
    Solution().solve(word)
