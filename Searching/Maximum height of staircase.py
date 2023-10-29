class Solution:
    # @param A : integer
    # @return an integer

    # approach 1
    # def solve(self, A):
    #     staircase_count = 0
    #     blocks = 1
    #     i = 1
    #     while blocks <= A:
    #         staircase_count += 1
    #         i += 1
    #         blocks += i
    #
    #     print(staircase_count)

    #     approach 2
    def solve(self, A):
        low = 1
        high = 1000000000
        ans = 0
        while (low <= high):
            mid = (low + high) // 2
            val = ((mid) * (mid + 1)) // 2
            if (val == A):
                return mid
            elif (val < A):
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == '__main__':
    A = 20
    print(Solution().solve(A))
