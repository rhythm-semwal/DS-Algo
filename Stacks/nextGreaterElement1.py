from typing import List


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [-1] * len(nums1)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:

                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            answer[i] = nums2[k]
                            break

        return answer


"""
Basically the problem says, if in nums1 we are working on 4, then in nums2 first find where is 4 and from that index find the next number greater than 4 in nums2. We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.

Steps:

We traverse nums2 and start storing elements on the top of stack.
If current number is greater than the top of the stack, then we found a pair. Keep popping from stack till the top of stack is smaller than current number.
After matching pairs are found, push current number on top of stack.
Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't found for them. Hence we'll put -1 for the remaining elements in stack.
"""

"""
Time complexity:
O(len(nums2) + len(nums1))
len(nums2) to iterate over nums2 and build hashmap, len(nums1) to iterate over hashmap finally

Space complexity:
O(len(nums1)) to keep additional hashmap
"""


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for element in stack:
            mapping[element] = -1

        return [mapping[each] for each in nums1]


if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution2().nextGreaterElement(nums1, nums2))