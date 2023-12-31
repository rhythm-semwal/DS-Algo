# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def rightSideView(self, root):
        if root is None:
            return root

        queue = [root]
        result = []

        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return result


class Solution2:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(node.val)

        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().rightSideView(root))
