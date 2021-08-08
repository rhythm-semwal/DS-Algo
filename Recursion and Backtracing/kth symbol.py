class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 0
        elif A == 2:
            if B == 1:
                return 0
            else:
                return 1
        else:
            result = []
            result.append(['0'])
            result.append(['0', '1'])
            print(result)
            for i in range(2, A):
                count = 0
                row = (i-1)
                temp_result = ''
                while count < 2**(i-1):
                    if result[row][count] == '0':
                        temp_result += '01'
                    else:
                        temp_result += '10'
                    count += 1
                result.append(list("".join(temp_result)))

        print(result)
        print(result[A-1][B-1])
A = 12
B = 36
Solution().solve(A, B)