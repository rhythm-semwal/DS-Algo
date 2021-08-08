class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    # 	def paint(self, A, B, C):
    def feasibilty(self, arr, painters, time, target):
        count = 1
        temp = 0
        for i in range(len(arr)):
            temp += arr[i]*time

            if temp > target:
                count += 1
                temp = arr[i]*time

        return count <= painters


    def paint(self, A, B, C):
        # minimum time that will be taken to paint = max(Array)*time taken to paint board
        # maximum time taken will be when a single painter is there to paint all the boards.
        low = max(C)*B
        high = sum(C)*B
        ans = 1
        while low <= high:
            mid = (low+high)//2

            if self.feasibilty(C, A, B, mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans % 10000003


if __name__ == '__main__':
    # A = 2
    # B = 2
    # C = [1,2,3,4,5]
    # A = 10
    # B = 1
    # C = [1, 8, 11, 3]
    # A = 2
    # B = 5
    # C = [1, 10]
    A = 3
    B = 10
    C = [640, 435, 647, 352, 8, 90, 960, 329, 859]
    Solution().paint(A, B, C)
