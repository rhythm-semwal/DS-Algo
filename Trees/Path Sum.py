# Definition for a  binary tree node
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:  # dfs
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


class Solution2:  # dfs
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None and targetSum == root.val:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


class Solution2:  # bfs
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = [(root, targetSum)]

        while queue:
            node, current_sum = queue.pop(0)

            if node is None:
                continue

            if not node.left and not node.right and current_sum == node.val:
                return True

            queue.append((node.left, current_sum - node.val))
            queue.append((node.right, current_sum - node.val))

        return False
