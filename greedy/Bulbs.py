class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        state = 0
        result = 0

        for i in range(len(A)):
            if A[i] == state:
                result += 1
                state = 1 - state
        return result

    def bulbs(self, A):

        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return 0 if A[0] else 1

        result = 0
        # this is done because if 0 is the first element than 1 bulb switch is required for that also
        if A[0] == 0:
            result += 1

        for i in range(1, n):
            if A[i] != A[i - 1]:
                result += 1

        return result
