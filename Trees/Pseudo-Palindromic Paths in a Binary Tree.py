import sys
from collections import defaultdict, deque
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


class Solution1:
    # TC = O(N)
    # SC = O(H), where H is the height of the binary tree.
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def traverse(node, pairs):
            if not node:
                return 0

            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)

            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0

            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))

            return left + right

        return traverse(root, set())


# Memory Limit Exceeded
# TC = O(N*D) where N is to find root to leaf path and D is for the loop where D is the height of tree
# O(D), where D is the maximum depth (height) of the binary tree.
class Solution:
    def root_to_leaf_path(self, root, path, result):
        if not root:
            return

        path.append(root.val)

        if not root.left and not root.right:
            result.append(list(path))
            del path[-1]
            return

        self.root_to_leaf_path(root.left, path, result)
        self.root_to_leaf_path(root.right, path, result)

        del path[-1]

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        result = []

        self.root_to_leaf_path(root, [], result)

        ans = 0

        for arr in result:
            visited = set()
            for each in arr:
                if each not in visited:
                    visited.add(each)
                else:
                    visited.remove(each)
            ans += 1 if len(visited) <= 1 else 0

        return ans


# input = [10,20,30,40,60,90,100, None, 5, 70, 75, None, None, 111, 112]
# input = [20, 8, 22, 5, 3, None, 25, None, None, 10, 14]
# input = [1,3,2]
# input = [1,2,4,None,3,None,5,None,6]
# input = [1,3,2,5,None,None,9,6,None,None,None,None,None,7]
input = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
input = [4, 2, 7, 1, 3]

root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 8, 9]

root = [2, 1, 3]
root = [2,3,1,3,1,None,1]
tree_head = build_tree_from_array(root)
print(Solution().pseudoPalindromicPaths(tree_head))