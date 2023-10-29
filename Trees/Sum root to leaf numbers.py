# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def is_leaf(self, node):
        if node.left is None and node.right is None:
            return True
        return False

    def solve(self, node, value):
        if node is None:
            return 0
        if self.is_leaf(node):
            return 10 * value + node.val
        new_value = 10 * value + node.val
        left = self.solve(node.left, new_value)
        right = self.solve(node.right, new_value)

        return left + right

    def sumNumbers(self, root: TreeNode) -> int:
        return self.solve(root, 0)


root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(Solution().sumNumbers(root))