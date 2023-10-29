class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        result = [-1]*len(A)
        stack = list()
        stack.append(A[0])
        for i in range(1, len(A)):
            current = A[i]
            # handle duplicates also
            while len(stack) > 0 and stack[-1] >= current:
                stack.pop()

            if len(stack) == 0:
                result[i] = -1
            else:
                result[i] = stack[-1]

            stack.append(current)

        print(result)

        # approach 2
        result = [-1] * len(A)

        stack = list()
        stack.append(A[0])
        n = len(A)
        for i in range(1, n):
            current = A[i]

            if current <= stack[-1]:
                while stack and current <= stack[-1]:
                    stack.pop()

                if stack:
                    result[i] = stack[-1]
                else:
                    result[i] = -1

                stack.append(current)

            else:
                result[i] = stack[-1]
                stack.append(current)

        return result

# A = [4, 5, 2, 10, 8]
# A = [3, 2, 1]
# A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
A = [4,7,3,8]
Solution().prevSmaller(A)
