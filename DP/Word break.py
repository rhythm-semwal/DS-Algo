class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        if len(A) == 0:
            return True

        for i in range(1, len(A)+1):
            word = A[:i]
            if not word in B:
                continue
            if self.wordBreak(A[i:], B):
                return True

        return False

    def wordBreak(self, A, B):
        can_make = [False]*(len(A)+1)
        # base case. if the string is empty
        can_make[0] = True

        for i in range(1, len(A)+1):  # this is the prefix length
            for j in range(i-1, -1, -1):  # this is the prefix in the reverse order
                print(A[j:i])
                if can_make[j] and A[j:i] in B:
                    can_make[i] = True
                    break

        return 1 if can_make[-1] else 0


A = "iamace"
B = ["i", "am", "ace"]
# A = "a"
# B = ["aaa"]
print(Solution().wordBreak(A, B))
