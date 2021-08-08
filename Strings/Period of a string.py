class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        z = [0] * len(A)
        left, right = 0, 0

        for i in range(1, len(A)):
            if i > right:
                left, right = i, i

                while right < len(A) and A[right] == A[right - left]:
                    right += 1

                z[i] = right - left
                right -= 1

            else:
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]
                else:
                    left = i
                    while right < len(A) and A[right] == A[right - left]:
                        right += 1

                    z[i] = right - left
                    right -= 1
        print(z)
        for i in range(1, len(z)-1):
            if z[i]+i == len(A):
                return i
        return len(A)

A = "abcaabcaab"
print(Solution().solve(A))
