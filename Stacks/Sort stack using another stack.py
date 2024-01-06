class Solution:
# @param A : list of integers
# @return a list of integers
    def solve(self, A):
        stack1, stack2 = list(), list()
        stack1.append(A[0])

        for i in range(1, len(A)):
            # if top of stack is < than element to be inserted
            if stack1[-1] < A[i]:
                # while top of the stack is less than the element to be inserted pop from stack1 and add to stack2
                while len(stack1) > 0 and stack1[-1] < A[i]:
                    stack2.append(stack1.pop())
            # append new element to stack1
            stack1.append(A[i])
            # the element in stack 2 will be in decreasing sorted order so add all the element from stack2 to stack1
            while len(stack2) > 0:
                stack1.append(stack2.pop())

        result = list()
        for i in range(len(stack1)-1, -1, -1):
            result.append(stack1[i])

        print(result)

A = [4,3,1,6,2,5]
# A = [5, 4, 3, 2, 1]
Solution().solve(A)