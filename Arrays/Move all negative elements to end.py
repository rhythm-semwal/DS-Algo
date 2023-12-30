class Solution1:
    def segregateElements(self, arr, n):
        # Your code goes here
        # TC = O(N)
        # SC = O(N)
        tmp1 = []
        tmp2 = []

        for num in arr:
            if num < 0:
                tmp2.append(num)
            else:
                tmp1.append(num)

        c = 0
        for i in tmp1 + tmp2:
            arr[c] = i
            c += 1
