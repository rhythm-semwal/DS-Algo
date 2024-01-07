# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return helper(root) != -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.left.right.right = TreeNode(5)
# root.left.left.left = TreeNode(8)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
print(Solution().isBalanced(root))