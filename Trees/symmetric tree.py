# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive - TC = O(N)
class Solution1:
    def solve(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.val == node2.val) and self.solve(node1.left, node2.right) and self.solve(node1.right, node2.left)

    def isSymmetric(self, root: Node) -> bool:
        return self.solve(root, root)

# iterative - TC = O(N)
class Solution2:
    def isSymmetric(self, A):
        queue = []
        queue.append(A)
        queue.append(A)

        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return 0

            if node1.val != node2.val:
                return 0

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)

        return 1


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
print(Solution().isSymmetric(root))