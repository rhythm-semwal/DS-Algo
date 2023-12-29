
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # recursive approach
    def solve(self, node, result):
        if node is None:
            return None
        self.solve(node.left, result)
        result.append(node.val)
        self.solve(node.right, result)

        return result

    def inorderTraversal(self, root):
        return self.solve(root, [])

    # iterative approach
    def inorderTraversal(self, A):
        if A is None:
            return []

        result = []
        stack = []

        current = A

        while current is not None or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result

