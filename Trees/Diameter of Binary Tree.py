# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
implement dfs
calculate left and right height of each node, calculate ans first
then return the updated height
"""


class Solution:
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