class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        order_index = dict()
        for index, value in enumerate(B):
            order_index[value] = index

        for i in range(len(A)-1):
            word1 = A[i]
            word2 = A[i+1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break  # break condition if the upper if loop is not satisfied i.e words are in sorted order
            else:
                if len(word1) > len(word2):
                    return False
        return True


if __name__ == "__main__":
    # A = ["hello", "scaler", "interviewbit"]
    # B = "adhbcfegskjlponmirqtxwuvzy"

    A = ["fine", "none", "no"]
    B = "qwertyuiopasdfghjklzxcvbnm"

    print(Solution().solve(A,B))
