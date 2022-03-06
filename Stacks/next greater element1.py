class Solution:
    def nextGreaterElement(self, nums1, nums2):
        element_index_mapping = {}

        for i in range(len(nums2)):
            element_index_mapping[nums2[i]] = i

        next_greater_element_array = [-1]*len(nums2)
        stack = []
        stack.append(0)
        for i in range(1, len(nums2)):
            while len(stack) > 0 and nums2[i] >= nums2[stack[-1]]:
                index = stack.pop()
                next_greater_element_array[index] = nums2[i]

            stack.append(i)

        result = []
        for i in range(len(nums1)):
            index = element_index_mapping[nums1[i]]
            print(index)
            result.append(next_greater_element_array[index])

        print(result)

if __name__ == "__main__":
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    Solution().nextGreaterElement(nums1, nums2)