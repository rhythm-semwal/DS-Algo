class Solution:

    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # handle overflow
        return (a & mask) if b > 0 else a

    # Python3 Program to add two numbers
    # without using arithmetic operator
    def add(self, x, y):

        # Iterate till there is no carry
        while y != 0:
            # carry now contains common
            # set bits of x and y
            carry = x & y

            # Sum of bits of x and y where at
            # least one of the bits is not set
            x = x ^ y

            # Carry is shifted by one so that
            # adding it to x gives the required sum
            y = carry << 1

        return x


print(Solution().getSum(2, 3))
