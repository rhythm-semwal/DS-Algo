from typing import Optional, List


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


class Solution1:  # dfs solution
    def dfs(self, root, path, result, running_sum):
        if root is None:
            return

        path.append(root.val)

        if root.left is None and root.right is None and running_sum == root.val:
            result.append(list(path))

        self.dfs(root.left, path, result, running_sum-root.val)
        self.dfs(root.right, path, result, running_sum-root.val)

        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, [], result, targetSum)
        return result

class Solution2:  # bfs solution
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        queue, result = [(root, targetSum, [])], []

        while queue:
            node, current_sum, path = queue.pop()

            if not node.left and not node.right and current_sum == node.val:
                result.append(path + [node.val])
            else:
                if node.left:
                    queue.append((node.left, current_sum - node.val, path + [node.val]))
                if node.right:
                    queue.append((node.right, current_sum - node.val, path + [node.val]))

        return result