class Solution:
    # @param A : list of integers
    # @param B : string
    # @return a list of integers
    def solve(self, A, B):
        hash_map = {}

        for index, value in enumerate(A):
            hash_map[value] = index+1

        A.sort()
        stack = list()
        ans = list()
        for i in range(len(B)):
            if B[i] == '0':
                value = A.pop(0)
                ans.append(hash_map[value])
                stack.append(value)
            else:
                value = stack.pop(-1)
                ans.append(hash_map[value])

        return ans
