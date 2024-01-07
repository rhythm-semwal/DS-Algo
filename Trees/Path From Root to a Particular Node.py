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
    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1

    def isBalanced(self, root):
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)




input = [3,5,1,6,2,0,8,None,None,7,4]
# p = TreeNode(5)
# q = TreeNode(1)
p = 6
q = 7
tree_head = build_tree_from_array(input)
print(Solution().lowestCommonAncestor(tree_head, p, q))