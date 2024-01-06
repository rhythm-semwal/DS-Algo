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
    def bottomView(self, root):
        # code here
        if root is None:
            return root

        from collections import defaultdict

        queue = [(root, 0)]
        hash_map = defaultdict(int)

        while queue:
            current, level = queue.pop(0)

            hash_map[level] = current.val

            if current.left:
                queue.append((current.left, level-1))
            if current.right:
                queue.append((current.right, level+1))

        result = []
        for key in sorted(hash_map.keys()):
            result.append(hash_map[key])

        return result