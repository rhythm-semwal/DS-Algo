class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start, end = 0, len(A)-1

        while start <= end:
            mid = (start+end)//2

            if A[mid] == B:
                return mid
            elif A[mid] > B:
                end = mid-1
            else:
                start = mid+1

        return start


if __name__ == '__main__':
    A = [1, 3, 5, 6]
    B = 7
    # A = [1]
    # B = 1
    print(Solution().searchInsert(A, B))
