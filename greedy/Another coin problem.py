class Solution:
    # @param A : integer
    # @return an integer
    def nearest_power(self, num):
        pow = 1
        while 5 ** pow <= num:
            pow += 1
        return pow - 1

    def solve(self, A):
        if A < 5:
            ans = 0
            while A > 0:
                ans += 1
                A -= 1
            return ans

        nearest_power = self.nearest_power(A)
        # print(nearest_power)
        ans = 0

        while A > 0:
            if A >= 5 ** nearest_power:
                ans += 1
                A = A - 5 ** nearest_power
            else:
                nearest_power -= 1

            # print("new value of A = ", A)

        return ans