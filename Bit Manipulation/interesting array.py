class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        # approach 1
        # if the xor is even then return yes else return true
        # if len(A) == 1:
        #     return "No"
        # xor = A[0]
        # for i in range(1, len(A)):
        #     xor ^= A[i]

        # if xor & 1 == 0:
        #     return "Yes"
        # return "No"

        # approach 2
        count = 0
        # if the number of odd numbers are even return yes else no
        # bcoz even number can be splited into equal half and there XOR is 0
        # for odd numbers, if the number of odd number is even then there XOR will be 0
        for i in A:
            if i % 2:
                count += 1
        if count % 2 == 0:
            return "Yes"
        return "No"