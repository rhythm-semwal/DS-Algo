from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = True
        rows, cols = len(matrix), len(matrix[0])

        # rows - 0 and col 0 is kept for checking which elements are 0
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = False
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(rows-1, -1, -1):

            for j in range(cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if not col0:
                matrix[i][0] = 0
        print(matrix)


        # zeros_list = []
        #
        # row, cols = len(matrix), len(matrix[0])
        #
        # for i in range(row):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             zeros_list.append((i, j))
        #
        # print(zeros_list)
        #
        # for each in zeros_list:
        #     i, j = each[0], 0
        #     while i < row and j < cols:
        #         matrix[i][j] = 0
        #         j += 1
        #
        #     i, j = 0, each[1]
        #     while i < row and j < cols:
        #         matrix[i][j] = 0
        #         i += 1
        #
        # print(matrix)


# matrix = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,0,0,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
