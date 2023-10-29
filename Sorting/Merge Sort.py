class Solution:
    # @param A : list of integers
    # @return an integer

    def merge_array(self, arr, temp_arr, low, high, mid):
        inversionCount = 0

        i = low
        j = mid+1
        k = low

        while i <= mid and j <= high:
            if arr[i] < arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
                inversionCount += (mid - i+1)

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= high:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for i in range(low, high + 1):
            arr[i] = temp_arr[i]

        return inversionCount

    def sort_function(self, arr, temp_arr, low, high):

        if len(arr) == 1:
            return arr[0]

        inversionCount = 0

        if high > low:
            mid = low + (high - low) // 2

            inversionCount += self.sort_function(arr, temp_arr, low, mid)
            inversionCount += self.sort_function(arr, temp_arr,  mid + 1, high)
            inversionCount += self.merge_array(arr, temp_arr, low, high, mid)

        return inversionCount

    def solve(self, A):
        temp_arr = [0]*len(A)
        ans = self.sort_function(A, temp_arr, 0, len(A) - 1)
        return ans


# arr = [5, 4, 3, 2, 1]
arr = [ 221, 117, 1783, 3698, 1922, 1554, 3672, 2598, 1286, 1367, 4283, 360, 1928, 1921, 2659, 2932, 1257, 3683, 656, 3966, 3619 ]

print(Solution().solve(arr))
# print(arr)