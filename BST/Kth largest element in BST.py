class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, node):
        if root is None:
            return

        self.dfs(root.left, node)
        node.append(root.data)
        self.dfs(root.right, node)

    def kthLargest(self, root, k):
        # your code here
        nodes = []
        self.dfs(root, nodes)

        return nodes[len(nodes) - k]
