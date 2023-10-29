class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def factorial(self, n):
        fact = 1
        mod = 1000000007
        for i in range(1, n + 1):
            fact = (fact * i) % (mod - 1)
        return fact

    def fast(self, a, b, mod):
        if b == 0:
            return 1

        if b % 2 == 0:
            return self.fast((a % mod * a % mod) % mod, b // 2, mod)
        else:
            return (a * self.fast((a % mod * a % mod) % mod, b // 2, mod)) % mod

    def solve(self, A, B):
        """
        Used fermet's theorem property = a^b%m => a ^ (b%m-1) % m
        """
        mod = 1000000007
        fact = self.factorial(B) % (mod - 1)
        return self.fast(A, fact, mod)
