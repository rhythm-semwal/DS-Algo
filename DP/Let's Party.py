class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A == 1:
            return 1
        if A == 2:
            return 2

        second = 1
        first = 2
        mod = 10003
        for i in range(3, A + 1):
            result = (first % mod + ((i - 1) * second) % mod) % mod
            second = first
            first = result

        return first % 10003
