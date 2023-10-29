class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0

        current = A[0]
        prev = 0

        for i in range(1, len(A)):
            current, prev = max(current,A[i]+prev), current


input = [5, 2, 1, 3]
print(Solution().houseRobber(input))