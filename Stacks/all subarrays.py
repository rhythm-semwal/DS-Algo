class Solution:
    # @param A : list of integers
    # @return an integer
    """
    Calculate the just greater element on the left and right in the array.
    With this we know the max element and second max will be the current element itself.
    If any one of the array has 0 value that means the current value will be second max value.
    If in both the array has 0 value than current will be max ans second max
    And for the numbers which does not have 0 in both array then for left subarray, current will be second max and for
    right subarray current will be second max so we have to consider both cases.
    """
    def solve(self, A):
        n = len(A)
        stack = []
        just_greater_element_left = [0]*n
        just_greater_element_right = [0] * n

        stack.append(A[0])
        for i in range(1, n):
            current = A[i]

            while stack and stack[-1] <= current:
                stack.pop()

            if stack:
                just_greater_element_left[i] = stack[-1]

            stack.append(current)

        print(just_greater_element_left)

        stack = []
        stack.append(A[-1])
        for i in range(n-2, -1, -1):
            current = A[i]

            while stack and stack[-1] <= current:
                stack.pop()

            if stack:
                just_greater_element_right[i] = stack[-1]
            stack.append(current)

        print(just_greater_element_right)

        max_xor = -1
        for i in range(n):
            if just_greater_element_right[i] == 0 and just_greater_element_left[i] == 0:
                continue
            elif just_greater_element_right[i] == 0:
                max_xor = max(max_xor, just_greater_element_left[i] ^ A[i])
            elif just_greater_element_left[i] == 0:
                max_xor = max(max_xor, just_greater_element_right[i] ^ A[i])
            else:
                max_xor = max(max_xor, just_greater_element_right[i] ^ A[i])
                max_xor = max(max_xor, just_greater_element_left[i] ^ A[i])

        print(max_xor)


A = [2,3,1,6,2,9]
# A = [8, 1, 2]
# A = [1, 3]
print(Solution().solve(A))
