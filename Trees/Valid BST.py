# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    # approach 1
    def __init__(self):
        self.correct = True
        self.prev = float('-inf')

    def inorder(self, root):
        if root is None or not self.correct:
            return

        self.inorder(root.left)
        if root.val <= self.prev:
            self.correct = False
            return
        self.prev = root.val
        self.inorder(root.right)

    def isValidBST(self, A):
        self.inorder(A)
        if self.correct:
            return 1
        return 0

    # approach 2: iterative
    def isValidBST(self, A):
        # code here
        prev = float('-inf')

        stack = []

        current = A

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current.val <= self.prev:
                return 0

            self.prev = current.val

            current = current.right

        return 1

