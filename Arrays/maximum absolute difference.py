class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        import sys
        max1, max2 = -sys.maxsize, -sys.maxsize
        min1, min2 = sys.maxsize, sys.maxsize

        for i in range(len(A)):
            temp1 = A[i]+(i+1)
            max1 = max(max1, temp1)
            min1 = min(min1, temp1)

            temp2 = A[i]-(i+1)
            max2 = max(max2, temp2)
            min2 = min(min2, temp2)

        result = max(max1-min1, max2-min2)
        print(result)
        print(max1)
        print(min1)
        print(max2)
        print(min2)


A = [3, -2, 5, -4]
Solution().maxArr(A)
