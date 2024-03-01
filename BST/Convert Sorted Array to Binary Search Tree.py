import sys
from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_array(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    n = len(nodes)
    for i in range(n):
        if nodes[i] is not None:
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            if left_child_index < n:
                nodes[i].left = nodes[left_child_index]

            if right_child_index < n:
                nodes[i].right = nodes[right_child_index]

    return nodes[0]


class Solution2:
    # TC = O(n logn) --> n is because of slicing
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None

        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


class Solution1:
    # Here we are not doing any slicing operation, just using 2 pointers.
    # TC = O(N)
    # space complexity is O(log N) because of stack
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.make_bst(nums, 0, len(nums))

    def make_bst(self, nums, low, high):
        if low >= high:
            return None

        mid = (low + high) // 2
        return TreeNode(
            val=nums[mid],
            left=self.make_bst(nums, low, mid),
            right=self.make_bst(nums, mid + 1, high)
        )