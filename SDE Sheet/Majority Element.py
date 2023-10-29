class Solution:
    def solve(self, A):
        # if majority element is guaranteed
        candidate = 0
        count = 0

        for i in range(len(A)):
            if count == 0:
                candidate = A[i]

            if A[i] == candidate:
                count += 1
            else:
                count -= 1

        print(candidate)

        # if majority element is not guaranteed
        hash_map = dict()
        n = len(A)

        for i in range(len(A)):
            if A[i] not in hash_map:
                hash_map[A[i]] = 1
            else:
                hash_map[A[i]] += 1

        for key, value in hash_map.items():
            if value > n // 2:
                return key

        return -1

# A = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
A = [1,2,1,4,1,1,6,1]
A = [20, 30, 40, 50, 20, 60, 10]
Solution().solve(A)
