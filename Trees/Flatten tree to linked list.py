# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if A is None:
            return None

        left = self.flatten(A.left)
        right = self.flatten(A.right)

        A.left = None

        if left is None:
            A.right = right

        else:
            A.right = left

            while left.right is not None:
                left = left.right

            left.right = right

        return A


def display(root):
    if root is None:
        return

    while root is not None:
        print(root.val, end='->')
        root = root.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
result = Solution().flatten(root)
display(root)
