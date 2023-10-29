"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # iterative
    # def maxDepth(self, root):
    #     # write your code here
    #     if root is None:
    #         return 0
    #     queue = []
    #     count = 0
    #     queue.append(root)
    #
    #     while queue:
    #         count += 1
    #         for i in range(len(queue)):
    #             current = queue.pop(0)
    #
    #             if current.left:
    #                 queue.append(current.left)
    #
    #             if current.right:
    #                 queue.append(current.right)
    #
    #     return count

    # recursive
    def maxDepth(self, root):
        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))