# User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):
        # code here
        max_product = float('-inf')

        most_negative, most_positive = 1, 1

        for num in arr:
            most_positive, most_negative = max(num, most_positive * num, most_negative * num), \
                                           min(num, num * most_negative, num * most_positive)

            max_product = max(max_product, most_positive, most_negative)

        return max_product


arr = [8, -2, -2, 0, 8, 0, -6, -8, -6, -1]
n = len(arr)
print(Solution().maxProduct(arr, n))