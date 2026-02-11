# https://leetcode.com/problems/evaluate-division/
#TC = O(Q.(N + E)) where Q is the number of queries and N is the number of node and E is the edges. DFS for each query Q takes O(N+E) time
#SC = O(N+E)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(dict)

        for (a,b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value
        
        def dfs(current, target, visited):
            if current not in graph:
                return -1.0
            if current == target:
                return 1.0
            
            visited.add(current)

            for u, weight in graph[current].items():
                if u not in visited:
                    res = dfs(u, target, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0

        result = []

        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a, b, set()))
        
        return result
