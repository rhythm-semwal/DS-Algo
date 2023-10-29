# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
import sys
sys.setrecursionlimit(1000000)
class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        if not A:
            return
        root = TreeNode(A.pop(0))
        queue = []
        queue.append(root)
        while A:
            current = queue.pop(0)

            val = A.pop(0)
            if val != -1:
                current.left = TreeNode(val)
                queue.append(current.left)
            else:
                current.left = None
            val = A.pop(0)
            if val != -1:
                current.right = TreeNode(val)
                queue.append(current.right)
            else:
                current.right = None
        return root

    def solve(self, A):

        queue = []
        root = TreeNode(A[0])
        queue.append(root)
        current_position = 1

        while queue:
            current = queue.pop(0)
            if A[current_position] != -1:
                current.left = TreeNode(A[current_position])
                queue.append(current.left)
            else:
                current.left = None
            current_position += 1
            if A[current_position] != -1:
                current.right = TreeNode(A[current_position])
                queue.append(current.right)
            else:
                current.right = None
            current_position += 1
        return root
