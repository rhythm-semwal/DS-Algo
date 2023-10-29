class Solution:
    def hammingWeight1(self, n: int) -> int:
        """
        doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0
        Instead of checking every bit of the number, we repeatedly flip the least-significant
        1-bit of the number to 0,
         and add 1 to the sum.
         As soon as the number becomes 0, we know that it does not have any more 1-bits, and we return the sum.
        """
        sum = 0

        while n != 0:
            sum += 1
            n = n & (n - 1)

        return sum

    def hammingWeight2(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & (1 << i) != 0:
                count += 1

        return count