# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    # approach 1
    # def verticalOrderTraversal(self, A):
    #     if A is None:
    #         return []
    #
    #     queue = []
    #     queue.append((A, 0))
    #
    #     hash_map = dict()
    #
    #     while queue:
    #         temp_queue = []
    #         for node, dist in queue:
    #             if dist in hash_map:
    #                 hash_map[dist].append(node.val)
    #             else:
    #                 hash_map[dist] = [node.val]
    #             if node.left:
    #                 temp_queue.append((node.left, dist-1))
    #
    #             if node.right:
    #                 temp_queue.append((node.right, dist+1))
    #
    #         queue = temp_queue
    #
    #     print(hash_map)
    #
    #     print([hash_map[x] for x in sorted(hash_map.keys())])

    # approach if nodes on the same vertical level order is not important
    def __init__(self):
        import sys
        self.min_value = sys.maxsize
        self.max_value = -sys.maxsize

    def verticalOrderTraversal(self, A):
        if A is None:
            return None

        hash_map = {}
        queue = []
        queue.append((A, 0))

        while queue:
            current = queue.pop(0)
            node = current[0]
            level = current[1]
            if level in hash_map:
                hash_map[level].append(node.val)
            else:
                hash_map[level] = [node.val]
            self.max_value = max(self.max_value, level)
            self.min_value = min(self.min_value, level)

            if node.left:
                queue.append((node.left, level-1))
            if node.right:
                queue.append((node.right, level+1))

        print(hash_map)
        result = []
        print(self.min_value)
        print(self.max_value)
        for i in range(self.min_value, self.max_value+1):
            result.append(hash_map[i])

        print("'*****=", result)

    def level_order_traversal(self, root):
        if root is None:
            return None

        result = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        print(result)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
print(Solution().level_order_traversal(root))
print(Solution().verticalOrderTraversal(root))
