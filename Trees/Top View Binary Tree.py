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
    def topView(self, root):
        if root is None:
            return root

        result = []
        hash_map = dict()

        queue = [(root,0)]

        while queue:
            node, level = queue.pop(0)

            if level not in hash_map:
                hash_map[level] = node.val

            if node.left:
                queue.append((node.left, level-1))
            if node.right:
                queue.append((node.right, level+1))

        print(hash_map)
        for key in sorted(hash_map.keys()):
            result.append(hash_map[key])

        return result
