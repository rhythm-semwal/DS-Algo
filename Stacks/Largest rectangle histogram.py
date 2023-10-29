class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        """
        Algo: for the current element just check till where we can extend the current element i.e till what range
        is the current element min in both left and right side.
        This can be achieved thorugh evaluating the just smaller element on the left and just smaller element on the
        right.
        """
        stack = list()
        n = len(A)
        # calculate just smaller element on the left
        just_smaller_left = [-1]*n
        just_smaller_left[0] = -1
        stack = list()
        stack.append((A[0], 0))

        for i in range(1, n):
            current = A[i]

            while stack and current <= stack[-1][0]:
                stack.pop()

            if stack:
                just_smaller_left[i] = stack[-1][1]
            else:
                just_smaller_left[i] = -1

            stack.append((current, i))

        just_smaller_right = [-1] * n
        just_smaller_right[-1] = n
        stack.append((A[-1], n - 1))

        for i in range(n - 2, -1, -1):
            current = A[i]

            while stack and current <= stack[-1][0]:
                stack.pop()

            if stack:
                just_smaller_right[i] = stack[-1][1]
            else:
                just_smaller_right[i] = n

            stack.append((current, i))

        print(just_smaller_left)
        print(just_smaller_right)
        ans = 0
        for i in range(n):
            current_area = A[i]*(just_smaller_right[i] - just_smaller_left[i] - 1)
            ans = max(ans, current_area)

        print(ans)


A = [2, 1, 5, 6, 2, 3]
# A = [6,2,5,4,5,1,6]
Solution().largestRectangleArea(A)
