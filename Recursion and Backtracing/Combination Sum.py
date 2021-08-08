class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    # TC = 2**n * k
    # if n numbers are there 2**n different combinations can be generated
    # k is the time taken to add ans to result
    def find_combinations(self, arr, index, target, result, temp):
        if target == 0:
            ans = temp[:]
            result.append(ans) # this takes k time
            return
        if index == len(arr):
            return

        if arr[index] <= target:
            temp.append(arr[index])
            self.find_combinations(arr, index, target-arr[index], result, temp)
            temp.pop()
        self.find_combinations(arr, index+1, target, result, temp)

    def combinationSum(self, A, B):
        A.sort()
        i = 1
        while i < len(A):
            if A[i] == A[i - 1]:
                A.pop(i)
            else:
                i += 1
        ans = []
        self.find_combinations(A, 0, B, ans, [])
        return ans

A = [2,4,6]
B = 8
print(Solution().combinationSum(A, B))