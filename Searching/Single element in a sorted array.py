# Qs. Given a sorted array of integers A where every element appears twice except for one element which appears once,
# find and return this single element that appears only once.
#
# NOTE: Users are expected to solve this in O(log(N)) time.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        start, end = 0, len(A)-1
        while start <= end:

            mid = (start+end)//2

            # it means if the element is a new number
            if A[mid] != A[mid-1]:
                if mid % 2 == 0:
                    start = mid+1
                else:
                    end = mid-1

            # if it is not a new element
            # A[mid] == A[mid-1]
            else:
                if mid % 2 != 0:
                    start = mid+1
                else:
                    end = mid-1

        return A[end]


if __name__ == '__main__':
     arr = [1, 1, 7]
     # arr = [1, 1000000000, 1000000000 ]
     Solution().solve(arr)
