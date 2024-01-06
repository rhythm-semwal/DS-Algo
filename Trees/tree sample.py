import sys
from collections import defaultdict, deque
from typing import Optional


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


class Solution:

    def height(self, root):
        # code here
        if root is None:
            return 0

        left_tree_height = self.height(root.left)
        right_tree_height = self.height(root.right)

        return max(left_tree_height, right_tree_height) + 1

    # calculate the diameter of the Left Subtree
    # calculate the diameter of the Right Subtree
    # Calculate the height of Left and Right Tree from Root node
    # Answer would be the max of above 3
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_subtree_diameter = self.diameterOfBinaryTree(root.left)
        right_subtree_diameter = self.diameterOfBinaryTree(root.right)
        height = self.height(root.left) + self.height(root.right) + 1

        return max(height, left_subtree_diameter, right_subtree_diameter)


input = [1,2,3]
# input = [10,20,30,40,60,90,100, None, 5, 70, 75, None, None, 111, 112]
# input = [20, 8, 22, 5, 3, None, 25, None, None, 10, 14]
# input = [1,3,2]
# input = [1,2,4,None,3,None,5,None,6]
# input = [1,3,2,5,None,None,9,6,None,None,None,None,None,7]
tree_head = build_tree_from_array(input)
print(Solution().height(tree_head))
