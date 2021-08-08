class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        count_set_bits = 0
        while n != 0:
            count_set_bits += 1
            n = n & (n - 1)
        return count_set_bits == 1

print(Solution().isPowerOfTwo(16))