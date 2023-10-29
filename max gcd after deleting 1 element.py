class Solution:
    # @param A : list of integers
    # @return an integer
    def calc_gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a < b:
            a, b = b, a

        while b > 0:
            a = a%b
            a, b = b, a

        return a

    def solve(self, A):
        n = len(A)
        if n == 1:
            return A[0]
        if n == 2:
            return max(A)
        suffix_array_gcd, prefix_array_gcd = [0]*n, [0]*n
        prefix_array_gcd[0] = A[0]
        suffix_array_gcd[-1] = A[-1]

        # filling prefix array elements
        for i in range(1, n):
            prefix_array_gcd[i] = self.calc_gcd(A[i], prefix_array_gcd[i-1])

        # print("*****prefix_array_gcd = ", prefix_array_gcd)

        # filling suffix array elements
        for i in range(n-2, -1, -1):
            suffix_array_gcd[i] = self.calc_gcd(A[i], suffix_array_gcd[i + 1])

        # print("******suffix_array_gcd = ", suffix_array_gcd)

        max_gcd = 0
        for i in range(n):
            if i == 0:
                temp = suffix_array_gcd[i]
            elif i == n-1:
                temp = prefix_array_gcd[i]
            else:
                temp = self.calc_gcd(prefix_array_gcd[i-1], suffix_array_gcd[i+1])

            max_gcd = max(max_gcd, temp)

        return max_gcd

