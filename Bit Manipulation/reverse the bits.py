class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        # approach
        # ret = 0
        # for i in range(32):
        #     ret = A << i
        # print(ret)

        # approach 1
        # result = 0
        # power = 31
        # while A:
        #     result += (A&1) << power
        #     A = A >> 1
        #     power -= 1
        # return result

        # approach 2 - bit masking
        A = ((A & 0xffff0000) >> 16) | ((A & 0x0000ffff) << 16)
        A = ((A & 0xff00ff00) >> 8) | ((A & 0x00ff00ff) << 8)
        A = ((A & 0xf0f0f0f0) >> 4) | ((A & 0x0f0f0f0f) << 4)
        A = ((A & 0xcccccccc) >> 2) | ((A & 0x33333333) << 2)
        A = ((A & 0xaaaaaaaa) >> 1) | ((A & 0x55555555) << 1)
        print(A)

input = 21
print(Solution().reverse(input))
