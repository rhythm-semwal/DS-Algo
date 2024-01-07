class Solution:
    # In this solution since I know that both arrays are sorted, I will start from the last of arr1 and start of arr2.
    # Then compare the value. If arr1[i] > arr2[j], then swap the values
    # else I know that arr1 is sorted towards the left and arr2 is sorted toward the right
    # Now I will just sort both the arrays

    # TC = O(min(n,m)) - while loop + O(nlogn) - sort arr1 + O(mlogm) - sort arr2
    def merge(self, arr1, arr2, n, m):
        i, j = n-1, 0

        while i >= 0 and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                i -= 1
                j += 1
            else:
                break

        arr1.sort()
        arr2.sort()


a = [1,3,5,7]
b = [0,2,6,8,9]
Solution().merge(a, b, len(a), len(b))
print(*a, end="****")
print(*b)