class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def build_tree_from_array(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val > -1 else None for val in arr]
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

    def is_leaf_node(self, root):
        return root.left is None and root.right is None

    def add_left_boundary(self, root, result):
        current = root.left
        while current:
            if not self.is_leaf_node(current):
                result.append(current.val)

            if current.left:
                current = current.left
            else:
                current = current.right

    def add_right_boundary(self, root, result):
        stack = []
        current = root.right

        while current:
            if not self.is_leaf_node(current):
                stack.append(current.val)

            if current.right:
                current = current.right
            else:
                current = current.left

        while stack:
            result.append(stack.pop())

    # To print the leaf nodes, we can do a simple preorder traversal
    def add_leaf_nodes(self, root, result):
        if root is None:
            return

        if self.is_leaf_node(root):
            result.append(root.val)
            return

        self.add_leaf_nodes(root.left, result)
        self.add_leaf_nodes(root.right, result)

    def traverseBoundary(self, root):
        if root is None:
            return

        result = []

        if not self.is_leaf_node(root):
            result.append(root.val)
        self.add_left_boundary(root, result)
        self.add_leaf_nodes(root, result)
        self.add_right_boundary(root, result)

        return result


# input = [3,5,1,6,2,0,8,-1,-1,7,4]
input = [10, 5, 20, 3, 8, 18, 25, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1 ]
tree_head = build_tree_from_array(input)
print(Solution().traverseBoundary(tree_head))