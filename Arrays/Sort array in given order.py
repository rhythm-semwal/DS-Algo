class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hash_map = dict()
        result = list()
        index_map = dict()
        for i in range(len(A)):
            if A[i] not in hash_map:
                hash_map[A[i]] = 1
            else:
                hash_map[A[i]] += 1

        # approach 1
        # for i in range(len(B)):
        #     if B[i] in hash_map:
        #         while hash_map[B[i]] > 0:
        #             result.append(B[i])
        #             hash_map[B[i]] -= 1
        # temp = list()
        # for key, value in hash_map.items():
        #     if value > 0:
        #         while value > 0:
        #             temp.append(key)
        #             value -= 1
        #
        # temp.sort()
        # result.extend(temp)
        # return result

        # approach 2
        for i in range(len(B)):
            if B[i] in hash_map:
                while hash_map[B[i]] > 0:
                    result.append(B[i])
                    hash_map[B[i]] -= 1
                del hash_map[B[i]]

        sorted_hash_map = sorted(hash_map.items())

        for key, value in sorted_hash_map:
            while value:
                result.append(key)
                value -= 1

        return result



A = [3, 2, 3, 3, 3, 4, 5, 1]
B = [5, 4, 2]
Solution().solve(A, B)
