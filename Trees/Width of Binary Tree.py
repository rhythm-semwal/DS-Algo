import sys
from collections import defaultdict, deque


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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_width = 0
        queue = [(root, 0)]

        while queue:
            _, min_index = queue[0]
            for _ in range(len(queue)):
                node, index = queue.pop(0)

                if node.left:
                    queue.append((node.left, 2*index))

                if node.right:
                    queue.append((node.right, 2*index+1))

            max_width = max(max_width, index-min_index+1)

        return max_width



input = [1,2,3,4,5,6,7,None,8,None,None]
input = [10,20,30,40,60,90,100, None, 5, 70, 75, None, None, 111, 112]
# input = [20, 8, 22, 5, 3, None, 25, None, None, 10, 14]
# input = [1,3,2]
# input = [1,2,4,None,3,None,5,None,6]
input = [1,3,2,5,None,None,9,6,None,None,None,None,None,7]
tree_head = build_tree_from_array(input)
print(Solution().widthOfBinaryTree(tree_head))
