class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor = 0
        for i in range(len(A)):
            xor ^= A[i]

        bit = 0
        # get first set bit in xor
        while not (1 << bit) & xor:
            bit += 1

        bit_set_xor, bit_not_set_xor = 0, 0
        for i in range(len(A)):
            if (1 << bit) & A[i]:
                bit_set_xor = bit_set_xor ^ A[i]
            else:
                bit_not_set_xor = bit_not_set_xor ^ A[i]

        if bit_set_xor < bit_not_set_xor:
            return [bit_set_xor, bit_not_set_xor]
        return [bit_not_set_xor, bit_set_xor]


n = [1,2,3,1,2,4]
Solution().solve(n)
