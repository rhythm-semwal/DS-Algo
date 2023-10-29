class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        """
        the ans will contain the first character of A and first character of B.
        compare whether all the characters are less than the first char of B.
        In B if we take any other character even though it is less than the first character but it would increase its rank.
        """
        check_against = ord(B[0])
        ans = ""
        ans += A[0]

        for i in range(1, len(A)):
            # less because if same characters are added to the result then it would increase the rank and it may happen
            # that next character after the equal character is smaller than B[0] but overall it would increase the rank
            if ord(A[i]) < check_against:
                ans += A[i]
            else:
                break
        ans += B[0]

        return ans


A = "twvvsl"
B = "wtcyawv"
print(Solution().smallestPrefix(A, B))
