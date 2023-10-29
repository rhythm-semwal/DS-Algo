# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    # T.C = O(N**2) in case of skewed tree
    
    def sum_binary_tree(self, node):
        if node is None:
            return 0

        return node.val + self.sum_binary_tree(node.left) + self.sum_binary_tree(node.right)

    def solve(self, A):
        if A is None or (A.left is None and A.right is None):
            return 1

        left_sum = self.sum_binary_tree(A.left)
        right_sum = self.sum_binary_tree(A.right)

        if A.val == left_sum+right_sum and self.solve(A.left) and self.solve(A.right):
            return 1
        else:
            return 0


root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(8)
print(Solution().solve(root))
