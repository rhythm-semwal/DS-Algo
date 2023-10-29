class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        max_limit = 2147483647
        negative = False
        if A < 0 and B < 0:
            negative = False
        elif A < 0 or B < 0:
            negative = True
        A = abs(A)
        B = abs(B)

        power = A.bit_length()

        result = 0

        while power >= 0:
            temp = B << power
            if temp <= A:
                # result = result | (1 << power)
                result += (1 << power)
                A -= temp
            power -= 1

        if negative:
            result *= -1

        if result >= max_limit:
            return max_limit
        if result < -max_limit:
            return result
        return result

A = -2147483648
B = -1
print(Solution().divide(A, B))
