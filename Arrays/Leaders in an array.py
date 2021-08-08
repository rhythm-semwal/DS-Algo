class Solution:
    def solve(self, A):
        N = len(A)

        ans = list()
        ans.append(A[-1])

        for i in range(N - 2, -1, -1):
            if A[i] > ans[-1]:
                ans.append(A[i])

        return ans

    def leaders(self, A, N):
        # Code here
        temp_arr = [-1]*N

        stack = []
        stack.append(A[-1])

        for i in range(N-2, -1, -1):
            while stack and A[i] >= stack[-1]:
                stack.pop()

            if stack:
                temp_arr[i] = stack[-1]
            stack.append(A[i])

        print(temp_arr)
        result = []
        for i in range(N):
            if temp_arr[i] == -1:
                result.append(A[i])
        return result


arr = [1,2,3,4,0]
print(Solution().leaders(arr, len(arr)))
