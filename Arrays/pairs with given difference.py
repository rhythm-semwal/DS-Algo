class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()

        i, j = 1, 0
        ans = 0
        n = len(A)
        temp_set = set()
        while i < n and j < n:
            if i == j:
                if i == n - 1:
                    break
                i += 1
            if A[i] - A[j] > B:
                j += 1
            elif A[i] - A[j] < B:
                i += 1
            else:
                ans += 1
                temp_set.add((A[j], A[i]))
                i += 1
                j += 1

        return len(temp_set)

    def solve(self, A, B):
        hash_map = dict()
        hash_set = set()
        n = len(A)
        for i in range(n):
            if A[i] not in hash_map:
                hash_map[A[i]] = 1
            else:
                hash_map[A[i]] += 1

        for i in range(n):
            if A[i] - B in hash_map:
                # count += 1
                if A[i] - B == A[i] and hash_map[A[i] - B] <= 1:
                    continue
                else:
                    hash_set.add((A[i], A[i] - B))

        return len(hash_set)

nums = [11, 6, 10, 5, 11, 16]
k = 5

nums = [1, 5, 4, 1, 2]
k = 0
print(Solution().solve(nums, k))
