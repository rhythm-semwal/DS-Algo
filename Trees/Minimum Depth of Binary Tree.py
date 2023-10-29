class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not left or not right:
            return 1+left+right

        return 1+ min(left, right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)
print(Solution().minDepth(root))
