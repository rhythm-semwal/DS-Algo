class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def find_subsets(self, index, arr, n, result, ds):
        temp = ds.copy()
        result.append(temp)

        for i in range(index, n):
            if i != index and arr[i] == arr[i - 1]:
                continue
            ds.append(arr[i])
            self.find_subsets(i + 1, arr, n, result, ds)
            ds.pop()

    def subsetsWithDup(self, A):
        A.sort()
        result = []
        self.find_subsets(0, A, len(A), result, [])
        return result

