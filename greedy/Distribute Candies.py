class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)

        candies_count_left = [1] * n

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                candies_count_left[i] = candies_count_left[i - 1] + 1

        result = 0
        current = 1
        result += max(candies_count_left[-1], current)
        for i in range(n - 2, -1, -1):
            if A[i] <= A[i + 1]:
                current = 1
                result += max(candies_count_left[i], current)
            elif A[i] > A[i + 1]:
                current += 1
                result += max(candies_count_left[i], current)

        return result
