class Solution:
    def calculate_sum(self, index, arr, n, current_sum, result):
        if index == n:
            result.append(current_sum)
            return

        self.calculate_sum(index + 1, arr, n, current_sum + arr[index], result)
        self.calculate_sum(index + 1, arr, n, current_sum, result)

    def subsetSums(self, arr, N):
        # code here
        result = list()
        self.calculate_sum(0, arr, N, 0, result)
        result.sort()
        return result


arr = [2, 3]
Solution().subsetSums(arr, len(arr))
