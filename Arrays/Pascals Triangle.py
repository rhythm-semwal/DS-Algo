from typing import List


class Solution:
    # approach 1
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        # elif numRows == 2:
        #     return [[1], [1,1]]
        #
        # result_matrix = [[1], [1, 1]]
        result_matrix = [[1]]
        # rows_count = 2
        rows_count = 1

        while rows_count <= numRows-1:
            inner_matrix = list()
            for k in range(rows_count+1):
                if k == 0 or k == rows_count:
                    inner_matrix.append(1)
                else:
                    inner_matrix.append(result_matrix[rows_count-1][k] + result_matrix[rows_count-1][k-1])

            rows_count += 1
            result_matrix.append(inner_matrix)

        return result_matrix

    # approach 2
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(A):
            row = [0 for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for i in range(1, len(row) - 1):
                row[i] = triangle[row_num - 1][i] + triangle[row_num - 1][i - 1]

            triangle.append(row)

        return triangle


if __name__ == "__main__":
    rows = 10
    print(Solution().generate(rows))
