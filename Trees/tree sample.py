class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.correct = True
        self.prev = float('-inf')

    def __set_root_node__(self, value):
        self.root = Node(value)

    def insert_node(self, current_node, value):
        # if value <= current_node.data:
        if current_node.left:
            self.insert_node(current_node.left, value)
        else:
            current_node.left = Node(value)

        # elif value > current_node.data:
        if current_node.right:
            self.insert_node(current_node.right, value)
        else:
            current_node.right = Node(value)

    def insert(self, value):
        if self.root is None:
            self.__set_root_node__(value)
        else:
            self.insert_node(self.root, value)

    def levelOrder(self, root):
        if root is None:
            return []

        nodes_queue = []
        result = []
        nodes_queue.append(root)
        while len(nodes_queue) > 0:
            level = []
            for i in range(len(nodes_queue)):
                node = nodes_queue.pop(0)
                level.append(node.data)

                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)

            result.append(level)
        print(result)

    def postorderTraversal(self, A):
        if A is None:
            return []

        result = []
        stack = []

        current = A

        while current is not None or stack:
            if current:
                result.append(current.data)
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                current = current.left

        print(result[::-1])


    def inorderTraversal(self, root):
        if root is None:
            return []

        result = []
        stack = []
        current = root
        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)
            current = current.right

        print(result)

    def preorderTraversal(self, A):
        if A is None:
            return []

        result = []
        current = A
        stack = []
        while current is not None or len(stack):
            if current:
                result.append(current.data)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

        print(result)

    def inorderTraversal1(self, root):
        if root is None:
            return None
        result = []
        stack = []

        current = root

        while current is not None or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.data)
                current = current.right
        print(result)

    def return_preorder_list(self, node, result):
        if node is None:
            return None
        result.append(node.data)
        self.return_preorder_list(node.left, result)
        self.return_preorder_list(node.right, result)

        return result

    def preorderTraversal1(self, root):
        return self.return_preorder_list(root, [])


    def hasPathSum(self, A, B):
        if A is None:
            return 0

        B -= A.val

        if A.left is None and A.right is None:
            return B == 0

        return self.hasPathSum(A.left, B) or self.hasPathSum(A.right, B)

    def minDepth(self, A):
        if A is None:
            return 0

        left = self.minDepth(A.left)
        right = self.minDepth(A.right)

        if not left or not right:
            return 1+left+right

        return 1+min(left, right)

    def buildTree(self, A, B):
        if not B:
            return

        inorder_index = B.index(A.pop(0))
        root = Node(B[inorder_index])

        root.left = self.buildTree(A, B[:inorder_index])
        root.right = self.buildTree(A, B[inorder_index+1:])

        return root

    def buildTree1(self, A, B):
        # A = inorder
        # B = postorder
        if not A:
            return

        inorder_index = A.index(B.pop())
        root = Node(A[inorder_index])

        root.right = self.buildTree1(A[inorder_index+1:], B)
        root.left = self.buildTree1(A[:inorder_index], B)

        return root

    def deserialsize(self, data):
        root = Node(data.pop(0))
        queue = []
        queue.append(root)
        while data:
            current = queue.pop(0)

            val = data.pop(0)
            if val != -1:
                current.left = Node(val)
                queue.append(current.left)
            else:
                current.left = None
            val = data.pop(0)
            if val != -1:
                current.right = Node(val)
                queue.append(current.right)
            else:
                current.right = None
        return root

    def serial(self, root):
        result = []

        queue = []
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                current = queue.pop(0)

                result.append(current.data)

                if current.data != -1:
                    if current.left:
                        queue.append(current.left)
                    else:
                        new_node = Node(-1)
                        current.left = new_node
                        queue.append(current.left)

                    if current.right:
                        queue.append(current.right)
                    else:
                        new_node = Node(-1)
                        current.right(new_node)
                        queue.append(current.right)

        return result


    def isSubtree(self, root, subRoot) -> bool:
        def serialise(node):
            if not node:
                serial.append("#")
                return

            serial.append(',')
            serial.append(str(node.data))
            serialise(node.left)
            serialise(node.right)

        serial = []
        serialise(root)
        print(serial)
        root_serial = "".join(serial)
        print("root_serial = ", root_serial)

        serial = []
        serialise(subRoot)
        print(serial)
        subRoot_serial = "".join(serial)
        print("subRoot_serial = ", subRoot_serial)

        return subRoot_serial in root_serial

    def mergeTrees(self, root1: Node, root2: Node) -> Node:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root1.data += root2.data
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def isValidBST(self, root) -> bool:
        prev = float('-inf')

        stack = []
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left

            else:
                current = stack.pop()
                if current.data <= prev:
                    return False
                prev = current.data
                current = current.right

        return True

# root = [3,4,5,1,2]
# subRoot = [4,1,2]
# root = Tree().deserialsize(root)
# subRoot = Tree().deserialsize(subRoot)
#
# print(Tree().isSubtree(root, subRoot))

root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)
# root.left.left = Node(3)
# root.left.right = Node(4)
# root.left.right.right = Node(5)
# root.left.left.left = Node(8)
# root.right.left = Node(4)
# root.right.right = Node(4)
# print(Tree().zigzagLevelOrder(root))
# print(Tree().isValidBST(root))
# print(Tree().correct)
# # print(Tree().preorderTraversal(root))
# # print(Tree().preorderTraversal1(root))
# print(Tree().minDepth(root))

# Inorder = [2, 1, 3]
# Postorder = [2, 3, 1]
# result = Tree().buildTree1(Inorder, Postorder)
# Tree().levelOrder(result)

print(Tree().isValidBST(root))