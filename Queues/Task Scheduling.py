class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        from collections import deque
        queue = deque()

        for i in range(len(A)):
            queue.append(A[i])

        clock_cycles = 0
        for i in range(len(B)):
            if B[i] == queue[0]:
                clock_cycles += 1
                queue.popleft()
            else:
                while B[i] != queue[0]:
                    element = queue.popleft()
                    queue.append(element)
                    clock_cycles += 1

                clock_cycles += 1
                queue.popleft()

        print(clock_cycles)


A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]
# A = [1]
# B = [1]
Solution().solve(A, B)
