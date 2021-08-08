class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        just_greater_element_left = [-1]*n
        just_greater_element_right = [-1]*n
        just_smaller_element_left = [-1] * n
        just_smaller_element_right = [-1] * n
        total_max, total_min = 0, 0

        # calculate just_greater_element_left
        stack = list()
        just_greater_element_left[0] = -1
        stack.append((A[0], 0))
        for i in range(1, n):
            current = A[i]

            if current >= stack[-1][0]:
                while stack and current >= stack[-1][0]:
                    stack.pop()
                if stack:
                    just_greater_element_left[i] = stack[-1][1]
                else:
                    just_greater_element_left[i] = -1
                stack.append((current, i))
            else:
                just_greater_element_left[i] = stack[-1][1]
                stack.append((current, i))

        # calculate just_greater_element_right
        stack = list()
        just_greater_element_right[-1] = n
        stack.append((A[-1], n-1))
        for i in range(n-2, -1, -1):
            current = A[i]

            if current >= stack[-1][0]:
                while stack and current >= stack[-1][0]:
                    stack.pop()
                if stack:
                    just_greater_element_right[i] = stack[-1][1]
                else:
                    just_greater_element_right[i] = n
                stack.append((current, i))
            else:
                just_greater_element_right[i] = stack[-1][1]
                stack.append((current, i))

        # calculate just_smaller_element_left
        stack = list()
        just_smaller_element_left[0] = -1
        stack.append((A[0], 0))

        for i in range(1, n):
            current = A[i]

            if current <= stack[-1][0]:
                while stack and current <= stack[-1][0]:
                    stack.pop()

                if stack:
                    just_smaller_element_left[i] = stack[-1][1]
                else:
                    just_smaller_element_left[i] = -1

                stack.append((current, i))

            else:
                just_smaller_element_left[i] = stack[-1][1]
                stack.append((current, i))

        # calculate just_smaller_element_right
        stack = list()
        just_smaller_element_right[-1] = n
        stack.append((A[-1], n-1))

        for i in range(n-2, -1, -1):
            current = A[i]

            if current <= stack[-1][0]:
                while stack and current <= stack[-1][0]:
                    stack.pop()

                if stack:
                    just_smaller_element_right[i] = stack[-1][1]
                else:
                    just_smaller_element_right[i] = n

                stack.append((current, i))

            else:
                just_smaller_element_right[i] = stack[-1][1]
                stack.append((current, i))

        # print("just_greater_element_right = ", just_greater_element_right)
        # print("just_greater_element_left = ", just_greater_element_left)
        # print("just_smaller_element_right = ", just_smaller_element_right)
        # print("just_smaller_element_left = ", just_smaller_element_left)

        for i in range(n):
            total_max += (A[i]*((just_greater_element_right[i]-i)*(i-just_greater_element_left[i])))
            total_min += (A[i]*((just_smaller_element_right[i] - i) * (i - just_smaller_element_left[i])))
        # return total_max-total_min
        return (total_max-total_min)%1000000007

