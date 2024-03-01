class Solution:
    def isUgly(self, n: int) -> bool:
        for prime_factor in [2, 3, 5]:
            while n > 1 and n % prime_factor == 0:
                n //= prime_factor

        return True if n == 1 else False
