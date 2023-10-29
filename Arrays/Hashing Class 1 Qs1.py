class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        import sys
        hash_map = dict()
        ans = -sys.maxsize
        for i in range(len(A)):
            if A[i] not in hash_map:
                hash_map[A[i]] = i
            else:
                difference = i - hash_map[A[i]]
                ans = max(ans, difference)

        return ans if ans != -sys.maxsize else -1


# A = [7, 1, 3, 4, 1, 7]
# A = [1, 1]
A = [1,2,3,2,7,6,3,2,1]
print(Solution().solve(A))
