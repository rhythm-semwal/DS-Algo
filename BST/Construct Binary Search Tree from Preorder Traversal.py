# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    # TC = O(NlogN) - logN for the binary search on each node
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        i = 1

        while i < len(preorder) and preorder[i] < root.val:
            i += 1

        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root


class Solution2:
    # TC = O(N)
    # SC = O(N)
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)
            if value < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and value > stack[-1].val:
                    last = stack.pop()
                last.right = node

            stack.append(node)

        return root


preorder = [8,5,1,7,10,12]
Solution2().bstFromPreorder(preorder)
