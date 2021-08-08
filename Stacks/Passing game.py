class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def isEmpty(self, stack):
        if len(stack) == 0:
            return True
        return False

    def solve(self, A, B, C):
        ball_stack = list()
        i = 0
        while i < A:
            if C[i] != 0:
                ball_stack.append(C[i])
            else:
                if self.isEmpty(ball_stack):
                    return B
                else:
                    ball_stack.pop()

            i += 1
        if self.isEmpty(ball_stack):
            return B
        return ball_stack[-1]


# A = 10
# B = 23
# C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]
A = 4
B = 1
C = [3, 0, 4, 0]
print(Solution().solve(A, B, C))

