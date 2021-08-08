class Solution:
    def print_diagnols(self, matrix):
        result = []
        n = len(matrix)

        for i in range(n-1, -1, -1):
            j, k = i, 0
            temp = list()
            while j < n and k < n:
                temp.append(matrix[j][k])
                j += 1
                k += 1

            result.append(temp)

        for i in range(1, n):
            j, k = 0, i
            temp = []
            while j < n and k < n:
                temp.append(matrix[j][k])
                j += 1
                k += 1
            result.append(temp)

        print(result)


# input = [
#     [1,2,3, 4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Solution().print_diagnols(input)