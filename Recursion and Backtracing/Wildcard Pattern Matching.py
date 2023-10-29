class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def check(self, input, li, wildcard, lw):
        # base cases
        if li == 0 and lw == 0:
            return True
        elif lw == 0:
            return False
        elif li == 0:
            if wildcard[lw-1] == "*":
                return self.check(input, li, wildcard, lw-1)
            else:
                return False

        if input[li-1] == wildcard[lw-1]:
            return self.check(input, li-1, wildcard, lw - 1)
        elif wildcard[lw-1] == "?":
            return self.check(input, li-1, wildcard, lw - 1)
        elif wildcard[lw-1] == "*":
                return self.check(input, li-1, wildcard, lw) or self.check(input, li, wildcard, lw-1)
        else:
            return False
            # elif li < lw:
            #     return self.check(input, li - 1, wildcard, lw-1)

    def isMatch(self, A, B):
        return 1 if self.check(A, len(A), B, len(B)) else 0
