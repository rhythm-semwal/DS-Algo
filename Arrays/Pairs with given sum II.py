class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        i, j = 0, n-1
        current_sum = 0
        ans = 0
        while i < j:
            current_sum = A[i] + A[j]

            if current_sum == B:
                if A[i] == A[j]:
                    x = j-i+1
                    ans += (x*(x-1))//2  # nC2 formula
                    break
                else:
                    a, b = 1, 1
                    while A[i] == A[i+1]:
                        i += 1
                        a += 1
                    while A[j] == A[j-1]:
                        j -= 1
                        b += 1
                    ans += a*b
                    i += 1
                    j -= 1
            elif current_sum > B:
                j -= 1
            else:
                i += 1

        return ans%1000000007