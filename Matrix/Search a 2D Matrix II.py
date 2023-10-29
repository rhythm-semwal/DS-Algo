class Solution:
    def searchMatrix(self, matrix, target: int):
        row, col = len(matrix), len(matrix[0])-1
        i, j = 0, col

        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1

        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 14
print(Solution().searchMatrix(matrix, target))
