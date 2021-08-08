class Solution:
    def diagonal(self, A):

        result = []
        n = len(A)

        # number of diagnols = 2*(n-1)+1
        # for anti diagnols = sum of i,j is same
        # sum = j+k --> k = sum-j
        for i in range(2*(n-1)+1):
            temp = []
            for j in range(i+1):
                k = i-j
                if j >= n or k >= n:
                    continue
                temp.append(A[j][k])
            result.append(temp)

        print(result)


input = [
    [1,2,3, 4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
# input = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
Solution().diagonal(input)