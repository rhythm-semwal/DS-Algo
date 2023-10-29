from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def is_cyclic(self, v, visited, recstack):
        visited[v] = True
        recstack[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic(i, visited, recstack):
                    return True
            elif recstack[v]:
                return True
        # The node needs to be poped from
        # recursion stack before function ends
        recstack[v] = False
        return False

    def solve(self, A, B):
        for i in range(len(B)):
            self.add_edge(B[i][0], B[i][1])

        print(self.graph)
        visited = [False]*(A+1)
        rec_stack = [False]*(A+1)

        for i in range(1, A):
            if not visited[i]:
                if self.is_cyclic(i, visited, rec_stack):
                    return True

        return False

#
# A = 5
# B = [[1, 2],
#         [2, 3],
#         [3, 4],
#         [4, 5]]
A = 3
B =[
  [1, 3],
  [2, 3],
  [3, 2]
]
A = 4
B =[
  [1, 2],
  [2, 3],
  [3, 4]
]
print(Solution().solve(A, B))