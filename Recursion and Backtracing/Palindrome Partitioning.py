class Solution:
    # @param A : string
    # @return a list of list of strings
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        return True

    def solve(self, index, s, result, ans):
        if index == len(s):
            temp = ans.copy()
            result.append(temp)
            return result

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                ans.append(s[index:i+1])
                self.solve(i+1, s, result, ans)
                ans.pop(-1)

    def partition(self, A):
        result = list()
        ans = list()
        self.solve(0, A, result, ans)
        return result


A = "aabb"
print(Solution().partition(A))
