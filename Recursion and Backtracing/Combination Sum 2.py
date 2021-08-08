class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def find_combinations(self, candidates, target, result, temp, index):
        if target == 0:
            ans = temp[:]
            result.append(ans)
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            # i == index condition is to take the first element in each recursion step
            if i == index or candidates[i] != candidates[i-1]:
                temp.append(candidates[i])
                self.find_combinations(candidates, target-candidates[i], result, temp, i+1)
                temp.pop()

    def combinationSum(self, A, B):
        A.sort()
        result = []
        self.find_combinations(A, B, result, [], 0)
        return result


A = [1,1,1,1,1]
B = 5
print(Solution().combinationSum(A, B))
