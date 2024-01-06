# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    TC = O(N**2)
    So there are 3 cases:
    1. when the max diameter does not pass from root and lies in the Left subtree
    2. when the max diameter does not pass from root and lies in the right subtree
    3. when the max diameter pass from root and for that we calculate the height of LST and RST + 1
    """

    def height(self, root):
        if root is None:
            return 0

        left_tree_height = self.height(root.left)
        right_tree_height = self.height(root.right)

        return max(left_tree_height, right_tree_height) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_subtree_diameter = self.diameterOfBinaryTree(root.left)
        right_subtree_diameter = self.diameterOfBinaryTree(root.right)
        height = self.height(root.left) + self.height(root.right)

        return max(height, left_subtree_diameter, right_subtree_diameter)


class Solution2:
    """
    We need to calculate the diameter at each node and find the maximum diameter
    """
    def __init__(self):
        self.diameter = 0

    def depth(self, node):
        """
        1. Calculate the maximum depth of the left and right sides of the given node
        2. Determine the diameter at the given node and check if it's the maximum
        """
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        if left_depth + right_depth > self.diameter:
            self.diameter = left_depth + right_depth

        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter


class Solution:
    """
    implement dfs
    calculate left and right height of each node, calculate ans first
    then return the updated height
    """

    def helper(self, node, diameter):
        if node is None:
            return 0

        left = self.helper(node.left, diameter)
        right = self.helper(node.right, diameter)

        diameter[0] = max(diameter[0], left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # passing list because of call by reference, then the value will be updated in result list and return it
        result = [0]
        self.helper(root, result)
        return result[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.right.right = TreeNode(5)
# root.left.left.left = TreeNode(8)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(8)
print(Solution().diameterOfBinaryTree(root))