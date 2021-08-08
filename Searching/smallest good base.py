import math
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = int(A)
        # max no of bits required to represent a number is in base2, so the following line is for the same
        max_no_of_bits = int(math.log(n, 2))
        for i in range(max_no_of_bits, 0, -1):
            # estimating the base
            k = int(n**(1/i))
            print("LHS = ", k**(i+1)-1)
            print("RHS = ", n*(k-1))
            if(k**(i+1)-1) == n*(k-1):
                return str(k)
        return str(n-1)


if __name__ == '__main__':
    n = "13"
    print(Solution().solve(n))
