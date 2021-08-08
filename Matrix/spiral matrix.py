from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        in this algorithm when we are appending the element to the list, the constant element
        in the row or column will be the element which will be increased or decreased after it.
        for eg. if we are moving from left to right, then while accessing the element, we will consider the
        top_right element because after the traversal we will increase the top_right.
        """
        if len(matrix) == 0:
            return matrix
        if len(matrix) == 1:
            return matrix[0]
        m, n = len(matrix), len(matrix[0])
        print(m, n)
        left_corner = 0
        right_corner = n - 1
        top_right = 0
        bottom_right = m - 1
        print(right_corner, bottom_right)
        result_list = list()

        while left_corner <= right_corner and top_right <= bottom_right:
            # left to right
            for k in range(left_corner, right_corner + 1):
                result_list.append(matrix[top_right][k])
            top_right += 1

            # top to down
            for k in range(top_right, bottom_right + 1):
                result_list.append(matrix[k][right_corner])
            right_corner -= 1

            # right to left
            if left_corner <= right_corner and top_right <= bottom_right:
                for k in range(right_corner, left_corner - 1, -1):
                    result_list.append(matrix[bottom_right][k])
                bottom_right -= 1

            # down to top
            if left_corner <= right_corner and top_right <= bottom_right:
                for k in range(bottom_right, top_right - 1, -1):
                    result_list.append(matrix[k][left_corner])
                left_corner += 1

        return result_list


if __name__ == "__main__":
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # arr = [[1,2,3],[4,5,6],[7,8,9]]
    # arr = []
    print(Solution().spiralOrder(arr))
