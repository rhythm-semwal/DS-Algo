# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        if A is None:
            return A

        result, stack = [], []

        current = A

        while current is not None or stack:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                current = current.left
        return result[::-1]

