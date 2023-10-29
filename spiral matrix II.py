from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        print_number = 1
        left_corner = 0
        right_corner = n-1
        top_right = 0
        bottom_right = n-1
        result_matrix = [[0 for i in range(n)] for j in range(n)]
        while print_number <= n**2:
            for k in range(left_corner, right_corner+1):
                result_matrix[top_right][k] = print_number
                print_number += 1
            top_right += 1

            for k in range(top_right, bottom_right+1):
                result_matrix[k][right_corner] = print_number
                print_number += 1
            right_corner -= 1

            for k in range(right_corner, left_corner-1, -1):
                result_matrix[bottom_right][k] = print_number
                print_number += 1
            bottom_right -= 1

            for k in range(bottom_right, top_right-1, -1):
                result_matrix[k][left_corner] = print_number
                print_number += 1
            left_corner += 1

        print(result_matrix)


if __name__ == "__main__":
    Solution().generateMatrix(3)
