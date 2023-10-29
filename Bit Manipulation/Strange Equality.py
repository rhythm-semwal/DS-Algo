class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        bits = A.bit_length()
        X = A
        # X = toggle(A)
        while bits:
            X = X ^ (1 << bits - 1)
            bits -= 1

        # Y = pow(2, no of bit+1)
        Y = 1 << A.bit_length()

        return X ^ Y