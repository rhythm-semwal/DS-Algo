class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        n = len(A)
        result = [-1] * n
        stack = [A[-1]]

        for i in range(n-2, -1, -1):
            current = A[i]
            while stack and current >= stack[-1]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(A[i])

        print(result)


# A = [6,7,8,9,10]
# A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
# A = [3, 2, 1]
Solution().nextGreater(A)


