class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        # 1 is for the empty strings case in both A and B
        row, col = len(A)+1, len(B)+1

        edit_dist = [[0 for _ in range(col)] for _ in range(row)]


        for i in range(row):
            edit_dist[i][0] = i

        for i in range(col):
            edit_dist[0][i] = i

        i_index = 0

        for i in range(1, row):
            j_index = 0
            for j in range(1, col):
                if A[i_index] == B[j_index]:
                    edit_dist[i][j] = edit_dist[i-1][j-1]
                else:
                    # explore all the 3 operations and take min of all 3
                    # delete = edit_dist[i-1][j]
                    # insert = edit_dist[i][j-1]
                    # replace =  edit_dist[i-1][j-1
                    # print("min = ", min(edit_dist[i-1][j], edit_dist[i][j-1], edit_dist[i-1][j-1]))
                    edit_dist[i][j] = 1+min(edit_dist[i-1][j], edit_dist[i][j-1], edit_dist[i-1][j-1])

                j_index += 1
            i_index += 1

        # return row = len(A), col = len(B)
        print(edit_dist[row-1][col-1])

A = "Anshuman"
B = "Antihuman"

Solution().minDistance(A, B)
