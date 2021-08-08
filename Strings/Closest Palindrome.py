class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        count = 0
        start, end = 0, len(A)-1

        while start < end:
            if A[start] != A[end]:
                count += 1
                if count > 1:
                    return False
            start += 1
            end -= 1
        # if the string is palindrome and if len of the string is even then we have to make 2 changes minimum to make
        # string palindrome hence we return NO
        if count == 0 and len(A)%2 == 0:
            return "NO"
        # if the string is palindrome and if len of the string is odd then we have to make 1 changes minimum to make
        # string palindrome hence we return YES
        return "YES"


A = "aa"
print(Solution().solve(A))