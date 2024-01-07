class Solution:
    def kthElement(self, arr1, arr2, n, m, k):

        i, j = n - 1, 0

        while i >= 0 and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                i -= 1
                j += 1
            else:
                break

        arr1.sort()
        arr2.sort()

        arr3 = arr1 + arr2

        return arr3[k - 1]