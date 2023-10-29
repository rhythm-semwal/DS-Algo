class Solution:
    def check(self, A, target_sum, k):
        current_sum = sum(A[:k])

        if current_sum > target_sum:
            return False

        for i in range(1, len(A) - k + 1):
            current_sum = current_sum - A[i - 1] + A[k + i - 1]

            if current_sum > target_sum:
                return False

        return True

    def solve(self, A, B):
        low, high = 0, len(A)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.check(A, B, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


    """
        Approach 2
    """
    def solve(self, A, B):
        temp = A[0]
        i, j = 0, 1
        temp_result = 1
        while j < len(A):
            temp += A[j]
            if temp <= B:
                temp_result = max(temp_result, j-i+1)

            j += 1

        i, j = 1, len(A) - 1
        while j-i+1 == temp_result:
            temp_sum = sum(A[i:j+1])
            if temp_sum <= B:
                i += 1
            else:
                temp_result -= 1
                i += 1

        print(temp_result)


if __name__ == '__main__':
    # A = [1, 2, 3, 4, 5]
    # B = 10
    A = [1, 1000000000]
    B = 1000000000
    # A = [5, 17, 100, 11]
    # B = 130
    Solution().solve(A, B)

