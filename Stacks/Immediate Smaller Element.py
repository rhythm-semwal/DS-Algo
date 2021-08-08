class Solution:
    def immediateSmaller(self, arr, n):
        # code here
        next_smaller = [-1] * n

        stack = []

        for i in range(n):
            while stack and arr[i] <= stack[-1]:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]
            else:
                next_smaller[i] = -1

        return next_smaller
