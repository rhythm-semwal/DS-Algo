class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, arr, k):
        for i in range(26):
            if arr[i] != 0 and arr[i] < k:
                return False
        return True

    def solve(self, A, B):
        max_length = 0

        for i in range(len(A)):
            freq = [0] * 26
            for j in range(i, len(A)):
                freq[ord(A[j]) - ord('a')] += 1

                if self.isValid(freq, B):
                    max_length = max(max_length, j-i+1)

        return max_length


if __name__ == "__main__":
    word = "xwvmulcmtr"
    k = 2
    print(Solution().solve(word, k))
