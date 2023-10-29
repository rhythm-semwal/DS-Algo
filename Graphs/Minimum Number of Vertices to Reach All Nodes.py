from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_incoming_edge_exist = [False] * n

        for i in range(len(edges)):
            is_incoming_edge_exist[edges[i][1]] = True

        result = [index for index, value in enumerate(is_incoming_edge_exist) if not value]
        return result


n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(Solution().findSmallestSetOfVertices(n, edges))