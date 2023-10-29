class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()

        time_taken, ans = float('-inf'), 0

        for i in range(len(A)):
            ans = abs(A[i] - B[i])
            time_taken = max(ans, time_taken)

        return time_taken