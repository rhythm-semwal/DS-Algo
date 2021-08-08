class Solution:
    # @param A : list of integers
    # @return an integer
    def greater_element_left(self, A):
        stack = []
        stack.append((A[0], 0))
        result = [0] * len(A)
        result[0] = 0
        for i in range(1, len(A)):
            if A[i] < stack[-1][0]:
                result[i] = (stack[-1][1])
            else:
                while stack and A[i] >= stack[-1][0]:
                    stack.pop()

                if stack:
                    result[i] = stack[-1][1]
                else:
                    result[i] = 0
            stack.append((A[i], i))
        return result

    def greater_element_right(self, A):
        stack = []
        stack.append((A[-1], len(A) - 1))
        result = [0] * len(A)
        result[-1] = 0
        for i in range(len(A) - 2, -1, -1):
            if A[i] < stack[-1][0]:
                result[i] = stack[-1][1]
            else:
                while stack and A[i] >= stack[-1][0]:
                    stack.pop()

                if stack:
                    result[i] = stack[-1][1]
                else:
                    result[i] = 0
            stack.append((A[i], i))
        return result

    def maxSpecialProduct(self, A):
        greater_element_left = self.greater_element_left(A)
        greater_element_right = self.greater_element_right(A)
        # print("greater_element_left = ", greater_element_left)
        # print("greater_element_right = ", greater_element_right)

        ans = float('-inf')

        for i in range(len(A)):
            ans = max(ans, greater_element_left[i] * greater_element_right[i])

        return ans % 1000000007
