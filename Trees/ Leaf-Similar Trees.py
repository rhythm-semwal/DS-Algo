import sys
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_array(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    n = len(nodes)
    for i in range(n):
        if nodes[i] is not None:
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            if left_child_index < n:
                nodes[i].left = nodes[left_child_index]

            if right_child_index < n:
                nodes[i].right = nodes[right_child_index]

    return nodes[0]


class Solution1:
    def is_leaf_node(self, root):
        return root.left is None and root.right is None

    def print_leaf_node(self, root, leaf_node):
        if root is None:
            return

        if self.is_leaf_node(root):
            leaf_node.append(root.val)
            return leaf_node

        self.print_leaf_node(root.left, leaf_node)
        self.print_leaf_node(root.right, leaf_node)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_node1, leaf_node2 = [], []

        self.print_leaf_node(root1, leaf_node1)
        self.print_leaf_node(root2, leaf_node2)

        print(leaf_node1)
        print(leaf_node2)

        return leaf_node1 == leaf_node2


class Solution2:
    def dfs(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        return self.dfs(root.left) + self.dfs(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1) == self.dfs(root2)


root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

root1 = [1,2,3]
root2 = [1,3,2]
tree_head1 = build_tree_from_array(root1)
tree_head2 = build_tree_from_array(root2)
print(Solution2().leafSimilar(tree_head1, tree_head2))
