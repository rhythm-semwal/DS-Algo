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

    def get_path(self, root, path, result):
        if not root:
            return

        path.append(root.val)

        if not root.left and not root.right:
            result.append(list(path))
            del path[-1]
            return

        self.get_path(root.left, path, result)
        self.get_path(root.right, path, result)
        del path[-1]

    def Paths(self, root: TreeNode):
        if root is None:
            return []
        result = []
        self.get_path(root, [], result)

        return result


input = [10, 8, 2, 3, 5, 2, None]
tree_head = build_tree_from_array(input)
print(Solution().Paths(tree_head))
