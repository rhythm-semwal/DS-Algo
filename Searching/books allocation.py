class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def feasibility(self, arr, students, target):
        count = 1
        temp = 0
        for i in range(len(arr)):
            temp += arr[i]

            if temp > target:
                count += 1
                temp = arr[i]

        return count <= students

    def books(self, A, B):
        if len(A) < B:
            return -1
        low = max(A)
        high = sum(A)
        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if self.feasibility(A, B, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


if __name__ == '__main__':
    A = [12, 34, 67, 90]
    B = 2
    Solution().books(A, B)
