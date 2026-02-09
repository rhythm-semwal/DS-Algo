# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
class Solution:
    def dfs(self, adj):
        def solve(u):
            visited[u] = True
            result.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    solve(v)
        
        visited = [False] * len(adj)
        result = []
        solve(0)
        return result
