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


class Solution:
    def validate(self, root, left, right):
        if root is None:
            return True

        if left < root.val < right:
            return self.validate(root.left, left, root.val) and self.validate(root.right, root.val, right)
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -sys.maxsize, sys.maxsize)


class Solution2:
    def inorder(self, root, result):
        if root is None:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

        return result

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.inorder(root, result)

        print(result)

        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False

        return True


class Solution3:
    # @param A : root node of tree
    # @return an integer
    # approach 1
    def __init__(self):
        self.correct = True
        self.prev = float('-inf')

    def inorder(self, root):
        if root is None or not self.correct:
            return

        self.inorder(root.left)
        if root.val <= self.prev:
            self.correct = False
            return
        self.prev = root.val
        self.inorder(root.right)

    def isValidBST(self, A):
        self.inorder(A)
        if self.correct:
            return 1
        return 0

    # approach 2: iterative
    def isValidBST(self, A):
        # code here
        prev = float('-inf')

        stack = []

        current = A

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current.val <= self.prev:
                return 0

            self.prev = current.val

            current = current.right

        return 1

