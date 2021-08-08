class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):

        if A == 0:
            return 0

        if A < 10:
            return 1

        hash_Set = set()
        A = str(A)
        for i in range(len(A)):
            product = 1
            for j in range(i, len(A)):
                product *= int(A[j])

                if product in hash_Set:
                    return 0
                hash_Set.add(product)

        return 1
