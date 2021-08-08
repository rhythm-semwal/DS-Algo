from typing import List


class Solution:
    """
    3 types of questions can be asked.
    1. print all the rows upto the given row number(solution below)
    2. given row and column print the value. in thi case just compute nCr
    3. print just the row number given in the input
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [0 for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for i in range(1, len(row) - 1):
                row[i] = triangle[row_num - 1][i] + triangle[row_num - 1][i - 1]

            triangle.append(row)

        return triangle


if __name__ == "__main__":
    rows = 10
    print(Solution().generate(rows))
