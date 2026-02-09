# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
class Solution:
    def bfs(self, adj):
        result = []
        queue = []
        visited = [False] * len(adj)
        
        queue.append(0)
        visited[0] = True
        
        while queue:
            u = queue.pop(0)
            result.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        
        return result
