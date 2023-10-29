class Solution1:
    def subsets(self, A):
        solution = list()
        self.helper(A, solution, [], 0)
        return solution

    def helper(self, A, solution, current, index):
        solution.append(list(current))
        for i in range(index, len(A)):
            current.append(A[i])
            self.helper(A, solution, current, i+1)
            current.pop()


class Solution2:
    def subsets(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


if __name__ == '__main__':
    A = [1, 2, 3]
    print(Solution1().subsets(A))
