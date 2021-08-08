class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        n = len(A)
        stack = list()
        result = [-1] * n
        stack.append(A[-1])

        for i in range(len(A)-2, -1, -1):
            current = A[i]
            while len(stack) > 0 and current >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                result[i] = -1
            else:
                result[i] = stack[-1]
            stack.append(A[i])

        print(result)


# A = [6,7,8,9,10]
# A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
# A = [3, 2, 1]
Solution().nextGreater(A)


