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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if node is None:
                return 0
        
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left+right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


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
