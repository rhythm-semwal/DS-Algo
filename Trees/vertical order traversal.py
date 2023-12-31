# Definition for a  binary tree node
from collections import defaultdict


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
leet-ocde solution for this use case - There may be multiple nodes in the same row and same column. 
In such a case, sort these nodes by their values.
"""


class Solution1:
    def verticalTraversal(self, root):
        if root is None:
            return root

        hash_map = defaultdict(list)
        queue = [(root, 0, 0)]

        while queue:
            node, pos, depth = queue.pop(0)

            hash_map[(pos, depth)].append(node.val)
            hash_map[(pos, depth)].sort()

            if node.left:
                queue.append((node.left, pos - 1, depth + 1))
            if node.right:
                queue.append((node.right, pos + 1, depth + 1))

        res = defaultdict(list)
        keys = sorted(list(hash_map.keys()), key=lambda x: (x[0], x[1]))

        for k in keys:
            pos, depth = k
            res[pos].extend(hash_map[k])
        return res.values()


"""
approach if nodes on the same vertical level order is not important
"""


class Solution2:
    def verticalOrderTraversal(self, A):
        if A is None:
            return []

        queue = []
        queue.append((A, 0))

        hash_map = dict()

        while queue:
            temp_queue = []
            for node, dist in queue:
                if dist in hash_map:
                    hash_map[dist].append(node.val)
                else:
                    hash_map[dist] = [node.val]
                if node.left:
                    temp_queue.append((node.left, dist-1))

                if node.right:
                    temp_queue.append((node.right, dist+1))

            queue = temp_queue

        print(hash_map)

        print([hash_map[x] for x in sorted(hash_map.keys())])


"""
approach if nodes on the same vertical level order is important i.e the increasing vertical order
"""


class Solution3:
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
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))

        result = []

        for i in range(self.min_value, self.max_value + 1):
            result.append(hash_map[i])

        return result
