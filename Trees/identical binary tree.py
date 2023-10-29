# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def inorder_traversal(self, node):
        result = []
        stack = []

        while node or stack:
            if node:
                stack.append(node.left)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

    def postorder_traversal(self, node):
        result = []
        stack = []

        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node.right)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return result

    def isSameTree(self, A, B):
        node1_inorder = self.inorder_traversal(A)
        node2_inorder = self.inorder_traversal(B)

        node1_postorder = self.postorder_traversal(A)
        node2_postorder = self.postorder_traversal(B)

        if node1_postorder == node2_postorder and node1_inorder == node2_inorder:
            return 1
        else:
            return 0
        # if A is None and B is None:
        #     return 1
        # if A is None or B is None:
        #     return 0
        #
        # if A.val == B.val:
        #     return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
        # else:
        #     return 0
