from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, node):
        if root is None:
            return

        self.dfs(root.left, node)
        node.append(root.val)
        self.dfs(root.right, node)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.dfs(root, nodes)

        return nodes[k - 1]