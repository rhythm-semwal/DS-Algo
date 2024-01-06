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


class Solution:

    def countNodes(self, root: TreeNode):
        if root is None:
            return 0

        left_node_count = self.countNodes(root.left)
        right_node_count = self.countNodes(root.right)
        return left_node_count + right_node_count + 1


input = [1,3,2,5,None,None,9,6,None,None,None,None,None,7]
tree_head = build_tree_from_array(input)
print(Solution().countNodes(tree_head))