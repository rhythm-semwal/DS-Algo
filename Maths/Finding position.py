class Solution:
    # @param A : integer
    # @return an integer
    def swap_elements(self, index, arr):
        i, j = 0, 1
        while j <= index:
            arr[i] = arr[j]
            i += 1
            j += 2
        k = i - 1
        return k, arr

    def solve(self, A): # -> O(N)
        array_list = [0]*A
        i, j = 0, 1
        while j <= A:
            array_list[i] = j+1
            i += 1
            j += 2
        k = i-1
        while k > 0:
            k, array_list = self.swap_elements(k, array_list)

        return array_list[0]
    # approach2 -> O(logN)
    # def solve(self, A):
    #     i = 1
    #     while i <= A/2:
    #         i = i*2
    #
    #     return i


if __name__ == '__main__':
    print(Solution().solve(5))
