class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        import sys
        diff = sys.maxsize
        left_pointer, right_pointer = 0, 0
        i = 0  # pointer in first array
        j = len(B) - 1  # pointer in second array

        while i < len(A) and j >= 0:
            if abs(A[i] + B[j] - C) < diff:
                diff = abs(A[i] + B[j] - C)
                left_pointer = i
                right_pointer = j
            elif abs(A[i] + B[j] - C) == diff:
                if i < left_pointer:
                    left_pointer = i
                    right_pointer = j
                if i == left_pointer and j < right_pointer:
                    right_pointer = j

            if A[i] + B[j] > C:
                j -= 1
            elif A[i] + B[j] <= C:
                i += 1
        print(A[left_pointer])
        print(B[right_pointer])


A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8]
C = 9
# A = [5, 10, 20]
# B = [1, 2, 30]
# C = 13
# A = [ 1 ]
# B = [ 2, 4 ]
# C = 4
Solution().solve(A, B, C)