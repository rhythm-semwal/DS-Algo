class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def get_sign(self, sign1, sign2):
        if (sign1 == '+' and sign2 == '-') or (sign1 == '-' and sign2 == '+'):
            return '-'
        else:
            return '+'

    def get_element_sign(self, A, index):
        if index == 0:
            return '+'
        elif A[index-1] == '(':
            return '+'
        return A[index-1]

    def get_sign_in_list(self, A):
        i = 0
        stack = list()
        stack.append('+')
        alphabets_list = [0] * 26
        while i < len(A):
            if A[i] == '+' or A[i] == '-':
                i += 1
                continue
            elif A[i] == '(':
                sign = self.get_element_sign(A, i)
                global_sign = stack[-1]
                stack.append(self.get_sign(global_sign, sign))
            elif A[i] == ')':
                stack.pop()
            else:
                global_sign = stack[-1]
                current_sign = self.get_element_sign(A, i)
                alphabets_list[ord(A[i]) - ord('a')] = self.get_sign(global_sign, current_sign)
            i += 1

        return alphabets_list

    def solve(self, A, B):
        a_string_list = self.get_sign_in_list(A)
        b_string_list = self.get_sign_in_list(B)
        print(a_string_list)
        print(b_string_list)
        return 1 if a_string_list == b_string_list else 0




# A = "a-b-(c-d)"
# B = "a-b-c-d"
A = "-(a+b+c)"
B = "-a-b-c"
# A = "-(-(-(-a+b)-d+c)-q)"
# B = "a-b-d+c+q"
# A = "-(a+((b-c)-(d+e)))"
# B = "-(a+b-c-d-e)"
print(Solution().solve(A, B))
