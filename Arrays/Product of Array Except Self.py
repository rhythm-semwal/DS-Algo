class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        product = [1]

        for i in range(1, len(nums)):
            product.append(product[-1] * nums[i - 1])

        print(product)
        temp = 1

        for i in range(len(nums) - 1, -1, -1):
            product[i] = product[i] * temp
            temp = temp * nums[i]

        return product

array = [2,3,8]
# array = [-1,1,0,-3,3]
print(Solution().productExceptSelf(array))
