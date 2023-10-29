class Solution:
    def transfigure(self, A, B):
        # code here
        m = len(A)
        n = len(B)

        if m != n:
            return -1

        count_array = [0] * 256

        for i in range(n):
            count_array[ord(A[i])] += 1

        for i in range(n):
            count_array[ord(B[i])] -= 1

        for i in range(256):
            if count_array[i]:
                return -1

        result = 0
        i, j = n - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] == B[j]:
                j -= 1
                i -= 1

            else:
                i -= 1
                result += 1

        return result

