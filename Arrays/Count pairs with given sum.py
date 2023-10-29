class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        hash_map = dict()

        for i in range(n):
            if arr[i] in hash_map:
                hash_map[arr[i]] += 1
            else:
                hash_map[arr[i]] = 1

        for i in range(n):
            if k - arr[i] in hash_map:
                count += hash_map[k-arr[i]]

            if k - arr[i] == arr[i]:
                count -= 1

        return count // 2

N = 4
X = 6
arr = [1, 5, 7, 1]

N = 4
X = 2
arr = [1, 1, 1, 1]
print(Solution().getPairsCount(arr, N, X))
