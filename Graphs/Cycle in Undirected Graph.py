# class Graph:
#     def __init__(self, vertices):
#         self.v = vertices
#         self.graph = dict()
#
#     def add_edge(self, v, w):
#         self.graph[v].append(w)
#         self.graph[w].append(v)

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
        self.graph[w].append(v)

    def is_cyclic(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.is_cyclic(i, visited, v)
            elif parent != i:
                return True

    def solve(self, A, B):
        for i in range(len(B)):
            self.add_edge(B[i][0], B[i][1])

        # print(self.graph)
        visited = [False]*(A+1)

        for i in range(1, A):
            if not visited[i]:
                if self.is_cyclic(i, visited, -1):
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
print(Solution().solve(A, B))