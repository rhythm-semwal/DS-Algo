class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    # brute force - O(M*N)
    # def searchMatrix(self, A, B):
    #     n = len(A[0])
    #     for i in range(len(A)):
    #         for j in range(n):
    #             if A[i][j] == B:
    #                 return 1
    #     return 0

    # # using binary search
    # def helper_search(self, arr, target):
    #     low, high = 0, len(arr)-1
    #
    #     while low <= high:
    #         mid = (low + high)//2
    #
    #         if arr[mid] == target:
    #             return True
    #         elif arr[mid] < target:
    #             low = mid+1
    #         else:
    #             high = mid-1
    #     return False
    #
    # def searchMatrix(self, A, B):
    #     start, end = 0, len(A)-1
    #     # outer binary search for the row
    #     while start <= end:
    #         mid = (start+end)//2
    #
    #         if self.helper_search(A[mid], B):
    #             return 1
    #         elif A[mid][-1] > B:
    #             end = mid-1
    #         elif A[mid][-1] < B:
    #             start = mid+1
    #     return 0
    def searchMatrix(self, A, B):
        row, columns = len(A), len(A[0])-1

        i, j = 0, columns
        while i < row and j >= 0:
            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                i += 1
            elif A[i][j] > B:
                j -= 1
        return 0



A = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
B = 2
# A = [
#       [5, 17, 100, 111],
#       [119, 120, 127, 131]
#     ]
# B = 131
print(Solution().searchMatrix(A, B))