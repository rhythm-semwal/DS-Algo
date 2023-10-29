class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        count_array = [0]*26
        freq_count_array = [0]*26
        ans = 0
        for i in A:
            count_array[ord(i)-ord('a')] += 1

        for i in range(len(A)):
            freq_count_array[ord(B[i])-ord('a')] += 1

        if count_array == freq_count_array:
            ans += 1

        j = 0
        for i in range(len(A), len(B)):
            freq_count_array[ord(B[j])-ord('a')] -= 1
            freq_count_array[ord(B[i]) - ord('a')] += 1
            if count_array == freq_count_array:
                ans += 1
            j += 1

        return ans