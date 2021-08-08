class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = []
        path_list = A.split('/')
        # print(path_list)
        for i in range(len(path_list)):
            # print(path_list[i])

            if path_list[i] == '..':
                if stack:
                    stack.pop()
            elif path_list[i] and path_list[i] != '.':
                stack.append(path_list[i])

        # print(stack)
        result = "/"
        for i in range(len(stack)):
            if i == len(stack) - 1:
                result += stack[i]
            else:
                result += stack[i] + '/'

        return result