# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if A is None:
            return 0

        B -= A.val

        if A.left is None and A.right is None:
            return B == 0

        return self.hasPathSum(A.left, B) or self.hasPathSum(A.right, B)


