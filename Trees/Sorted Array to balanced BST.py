# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)

    def insert_node(self, current_node, value):
        if value == current_node.val:
            return
        if value < current_node.val:
            if current_node.left:
                self.insert_node(current_node.left, value)
            else:
                current_node.left = TreeNode(value)
        if value > current_node.val:
            if current_node.right:
                self.insert_node(current_node.right, value)
            else:
                current_node.right = TreeNode(value)

    def sortedArrayToBST(self, A):

        for i in range(len(A)):
            if self.root is None:
                self.set_root(A[i])
            else:
                self.insert_node(self.root, A[i])

        return self.root


def inorder_display(node):
    if node is None:
        return
    inorder_display(node.left)
    print(node.val, end=' ')
    inorder_display(node.right)


A = [1, 4, 8]
res = Solution().sortedArrayToBST(A)
inorder_display(res)
