class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if len(A) == 1:
            return A
        temp = A.split()
        start, end = 0, len(temp) - 1
        result = [0] * len(temp)
        while start <= end:
            result[start] = temp[end] + " "
            result[end] = temp[start] + " "
            start += 1
            end -= 1

        ans = "".join(result)

        return ans.rstrip(' ')

        # approach 2
        # word_list = A.split()
        # return (" ".join(word_list[::-1]))


if __name__ == "__main__":
    # word = "the sky is blue"
    word = "       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "

    print(Solution().solve(word))
