class Solution:
    # @param A : tuple of integers
    # @return an integer
    """
    Imagine that we have both max_prod[i] and min_prod[i] i.e. max product ending at i and min product ending at i.

Now if we have a negative number at arr[i+1] and if min_prod[i] is negative, then the product of the two
will be positive and can potentially be the largest product. So, the key point here is to maintain both the
max_prod and min_prod such that at iteration i, they refer to the max and min product ending at index i-1.

In short, One can have three options to make at any position in the array.

You can get the maximum product by multiplying the current element with the maximum product calculated so far. (might work when current
element is positive).
You can get the maximum product by multiplying the current element with minimum product calculated so far. (might work when current
element is negative).
The current element might be a starting position for maximum product subarray.
    """
    def maxProduct(self, A):
        n = len(A)

        ans = A[0]
        max_ans = ans
        min_ans = ans

        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremes by swapping them
            if A[i] < 0:
                max_ans, min_ans = min_ans, max_ans

            max_ans = max(A[i], A[i]*max_ans)
            min_ans = min(A[i], A[i]*min_ans)

            ans = max(ans, max_ans)
        print(ans)


    # O(N) TC
    # traverse the array 2 time to find the max product forward and backward
    # special case to handle the 0
    # def maxProduct(self, A):
    #     n = len(A)
    #     max_forward = float('-inf')
    #     max_backward = float('-inf')
    #
    #     is_zero = False
    #
    #     max_till_now = 1
    #
    #     for i in range(n):
    #         max_till_now *= A[i]
    #
    #         if max_till_now == 0:
    #             max_till_now = 1
    #             is_zero = True
    #
    #         else:
    #             max_forward = max(max_forward, max_till_now)
    #
    #     max_till_now = 1
    #     for i in range(n-1, -1, -1):
    #         max_till_now *= A[i]
    #
    #         if max_till_now == 0:
    #             is_zero = True
    #             max_till_now = 1
    #         else:
    #             max_backward = max(max_backward, max_till_now)
    #
    #     result = max(max_backward, max_forward)
    #
    #     if is_zero:
    #         result = max(result, 0)
    #         return result
    #
    #     return result

    # Brute force = O(N^2)
    # def maxProduct(self, A):
    #     n = len(A)
    #     ans = 0
    #
    #     if n == 1:
    #         return A[0]
    #
    #     for i in range(n):
    #         result = A[i]
    #
    #         for j in range(i+1, n):
    #             ans = max(ans, result)
    #             result *= A[j]
    #
    #         ans = max(ans, result)
    #
    #     return ans


A = [4, 2, -5, 1]
# A = [-3, 0, -5, 0]
# A = [ 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

print(Solution().maxProduct(A))
