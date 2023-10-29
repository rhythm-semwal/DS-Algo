import sys


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # def check(self, input, li, wildcard, lw):
    #     # base cases
    #     if li == 0 and lw == 0:
    #         return True
    #     elif lw == 0:
    #         return False
    #     elif li == 0:
    #         if wildcard[lw-1] == "*":
    #             return self.check(input, li, wildcard, lw-1)
    #         else:
    #             return False

    #     if input[li-1] == wildcard[lw-1]:
    #         return self.check(input, li-1, wildcard, lw - 1)
    #     elif wildcard[lw-1] == "?":
    #         return self.check(input, li-1, wildcard, lw - 1)
    #     elif wildcard[lw-1] == "*":
    #             return self.check(input, li-1, wildcard, lw) or self.check(input, li, wildcard, lw-1)
    #     else:
    #         return False
    # elif li < lw:
    #     return self.check(input, li - 1, wildcard, lw-1)

    def isMatch(self, A, B):
        # sys.setrecursionlimit(10**6)
        # return 1 if self.check(A, len(A), B, len(B)) else 0

        b_list = list(B)
        isFirst = True
        index = 0
        new_b = ""
        for i in range(len(b_list)):
            if b_list[i] == "*":
                if isFirst:
                    new_b += b_list[i]
                    isFirst = False
            else:
                new_b += b_list[i]
                isFirst = True

        B = new_b

        row, col = len(A) + 1, len(B) + 1
        lookup_matrix = [[False for _ in range(col)] for _ in range(row)]

        # base case i.e when len(word) and len(pattern) == 0
        lookup_matrix[0][0] = True

        # base case when word is empty and pattern is not empty, then for * we nned to check else everything will be false
        for i in range(1, col):
            if B[i - 1] == "*":
                lookup_matrix[0][i] = lookup_matrix[0][i - 1]

        # base case ===> len(word) != 0  and len(pattern) == 0, in lookup matrix that is already False, so need to assign value again

        for i in range(1, row):
            for j in range(1, col):
                if A[i - 1] == B[j - 1] or B[j - 1] == "?":
                    lookup_matrix[i][j] = lookup_matrix[i - 1][j - 1]
                elif B[j - 1] == "*":
                    lookup_matrix[i][j] = lookup_matrix[i - 1][j] or lookup_matrix[i][j - 1]

        return 1 if lookup_matrix[row - 1][col - 1] else 0
