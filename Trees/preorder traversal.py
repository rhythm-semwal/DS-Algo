# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def return_preorder_list(self, node, result):
        if node is None:
            return None
        result.append(node.data)
        self.return_preorder_list(node.left, result)
        self.return_preorder_list(node.right, result)

        return result

    # recursive code
    def preorderTraversal1(self, root):
        return self.return_preorder_list(root, [])

    # iterative code 2
    def preorderTraversal2(self, A):
        if A is None:
            return []
        stack = []
        stack.append(A)
        result = []
        while stack:
            current = stack.pop()

            result.append(current.val)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    # iterative code
    def preorderTraversal(self, A):
        if A is None:
            return []

        result = []
        stack = []

        current = A

        while current is not None or stack:
            if current is not None:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return result

