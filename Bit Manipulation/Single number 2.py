class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        # bit manipulation method - O(N)
        # the one variable will store the number that occurs once
        # the two variable will store the number that occurs twice
        # the number that occurs thrice for that number the one and two variable will become 0
        one, two = 0, 0

        for i in range(len(A)):
            one = (one ^ A[i]) & ~two
            two = (two ^ A[i]) & ~one

        return one

        # counting bits method
        # T.C = O(32*N) same for best average and worst case
        # for each bit position calculate the number of 1's
        # result = 0
        # for i in range(32):
        #     ones_count = 0
        #     for j in range(len(A)):
        #         if A[j] & (1 << i) != 0:
        #             ones_count += 1
        #     result = result | ((ones_count%3) << i)
        # print(result)

        # approach 3 - sorting + linear traversal
        """
        sort the array
        start i from 1st index position
        if arr[i] == arr[i-1] , then i+= 3
        repeat the above step
        
        corner case = if 1st element is the ans then in the start check if arr[0] != arr[1]
        corner case = if last element is the ans then in the start check if arr[-1] != arr[-2]
        
        T.C = O(NlogN + N)
        when N=int max
        then logN = 32
        therefore TC = O(N*32) for worst case
        """

A = [4, 4, 4, 2]
Solution().singleNumber(A)
