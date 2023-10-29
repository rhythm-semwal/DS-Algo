from functools import cmp_to_key


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def time_cmp(self, A, B):
        if A[0] < B[0]:
            return -1
        elif A[0] == B[0]:
            if A[1] > B[1]:
                return 1
            else:
                return -1
        else:
            return 1

    def solve(self, A):
        n = len(A)
        profit_cmp_key = cmp_to_key(self.time_cmp)

        A.sort(key=profit_cmp_key)
        # print(A)

        lis = [1]*n

        for i in range(1, n):
            for j in range(i):
                if A[j][1] < A[i][1] and A[j][0] < A[i][0]:
                    lis[i] = max(lis[i], lis[j]+1)

        return max(lis)
