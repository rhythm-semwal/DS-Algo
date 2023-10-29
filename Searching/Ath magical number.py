class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, a, b):
        a, b = b, a % b
        if b == 0:
            return a
        return self.gcd(a, b)

    def solve(self, A, B, C):
        low, high = 2, 100000000000000

        lcm = (B * C) // self.gcd(B, C)

        while low <= high:
            mid = (low+high)//2
            result = (mid//B) + (mid//C) - (mid//lcm)

            if result >= A:
                high = mid-1
            else:
                low = mid+1
        return low %(10**9+7)


if __name__ == '__main__':
    # A = 1
    # B = 2
    # C = 3
    # A= 19
    # B= 11
    # C= 13
    A = 807414236
    B = 3788
    C = 38141

    print(Solution().solve(A, B, C))
