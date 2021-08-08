class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def cmp(self, key1, key2):
        str_key1 = str(key1)
        str_key2 = str(key2)

        if int(str_key1 + str_key2) < int(str_key2 + str_key1):
            return 1
        return -1

    def largestNumber(self, A):
        import functools
        result = sorted(A, key=functools.cmp_to_key(self.cmp))

        ans = ""
        for i in result:
            ans += str(i)

        return 0 if ans.startswith('0') else ans


A = [3, 30, 34, 5, 9]
Solution().largestNumber(A)
