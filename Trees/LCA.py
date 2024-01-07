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
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root


class Solution2:
    # TC = O(N)
    # SC = O(N) + O(N)
    def path(self, root, node, result):
        if root is None:
            return False

        result.append(root)

        if root.val == node.val:
            return True

        if self.path(root.left, node, result) or self.path(root.right, node, result):
            return True

        result.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p, q) -> 'TreeNode':
        path1, path2 = [], []
        self.path(root, p, path1)
        self.path(root, q, path2)

        print(path1)
        print(path2)

        for node1, node2 in zip(path1, path2):
            if node1 == node2:
                common_ancestor = node1
            else:
                break

        return common_ancestor


input = [3,5,1,6,2,0,8,None,None,7,4]
p = TreeNode(7)
q = TreeNode(8)
tree_head = build_tree_from_array(input)
result = Solution1().lowestCommonAncestor(tree_head, p, q)
