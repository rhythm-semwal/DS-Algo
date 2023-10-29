class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):

        # approach 1 -> if the array can be modified.
        # TC = O(N)
        # SC = O(1)
        # n = len(A)
        # result = []
        # for i in range(n):
        #     if A[abs(A[i])-1] > 0:
        #         A[abs(A[i]) - 1] *= -1
        #     else:
        #         result.append(abs(A[i]))
        #
        # # print(A)
        # # print(result)
        # for i in range(n):
        #     if A[i] > 0:
        #         result.append(i+1)
        #
        # print(result)

        # approach 2 - using XOR
        # TC = O(N)
        # SC = O(1)
        n = len(A)
        xor_result = A[0]
        bit_set, bit_not_set = 0, 0
        # xor with all the array elements
        for i in range(1, n):
            xor_result ^= A[i]

        # xor with all the elements upto length of the array
        for i in range(1, n+1):
            xor_result ^= i

        print(xor_result)
        set_bit_no = xor_result & ~(xor_result-1)

        for i in range(n):
            if A[i] & set_bit_no != 0:
                bit_set ^= A[i]

            else:
                bit_not_set ^= A[i]

        for i in range(1, n+1):
            if i & set_bit_no != 0:
                bit_set ^= i
            else:
                bit_not_set ^= i

        print(bit_set, bit_not_set)


A = [3, 1, 2, 5, 3]
Solution().repeatedNumber(A)
