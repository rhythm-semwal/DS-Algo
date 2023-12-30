# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return root

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            # right node has to read first that's why I am pushing the left node first because then
            # the right node would be at the top of the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]

    def postorderTraversal1(self, A):
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

