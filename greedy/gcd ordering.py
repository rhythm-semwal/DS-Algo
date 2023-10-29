class Solution:
    # @param A : list of integers
    # @return a list of integers
    def gcd(self, a, b):
        if a < b:
            a, b = b, a

        while b > 0:
            a = a % b
            a, b = b, a

        return a

    def solve(self, A):
        n = len(A)
        if n < 2:
            return A
        if n == 2:
            if A[0] < A[1]:
                A[0], A[1] = A[1], A[0]

            return A

        flag = 0

        # To store the required ans
        ans = []

        # Sort the array
        A.sort(reverse=False)

        for i in range(2, n):

            # If need to make arranagement
            if (A[i] != A[i - 1] +
                    self.gcd(A[i - 1], A[i - 2])):
                flag = 1
                pos = i
                break

        # If possible then check for
        # lexographically larger
        # permutation (if any possible)
        if flag == 0:

            # If larger arrangement is possible
            if (A[1] == A[0] +
                    self.gcd(A[0], A[n - 1])):
                ans.append(A[n - 1])
                for i in range(n - 1):
                    ans.append(A[i])

                return ans

            # If no other arrangement is possible
            else:
                for i in range(n):
                    ans.append(A[i])

                return ans

        # Need to re-arrange the array
        else:

            # If possible, place at first position
            if (A[1] == A[0] +
                    self.gcd(A[pos], A[0])):
                flag = 0
                i = n - 1
                while (i > pos + 2):

                    # If even after one arrangement its
                    # impossible to get the required array
                    if (A[i] != A[i - 1] +
                            self.gcd(A[i - 1], A[i - 2])):
                        flag = 1
                        break

                    i -= 1

                if (flag == 0 and pos < n - 1):

                    # If it is not possible to get
                    # the required array
                    if (A[pos + 1] != A[pos - 1] +
                            self.gcd(A[pos - 1], A[pos - 2])):
                        flag = 1

                if (flag == 0 and pos < n - 2):

                    # If it is not possible to get
                    # the required array
                    if (A[pos + 2] != A[pos + 1] +
                            self.gcd(A[pos - 1], A[pos + 1])):
                        flag = 1

                # If it is possible to get the answer
                if (flag == 0):
                    ans.append(A[pos])
                    for i in range(n):
                        if (i != pos):
                            ans.append(A[i])

                    return ans

        ans.append(-1)
        return ans


A = [2, 4, 6, 8, 8]
print(Solution().solve(A))