"""
Qs. https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        queue = [(0, 0, 1)]
        grid[0][0] = 1

        for i,j,d in queue:
            if i == n-1 and j == n-1:
                return d
            
            directions = [(i-1, j), (i, j-1),(i+1, j-1),(i+1,j),(i+1,j+1),(i,j+1),(i-1,j+1),(i-1,j-1)]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x,y,d+1))
        
        return -1
'''
Below solution without updating the matrix by using a set.
'''
class Solution2:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]
        seen = set()
        seen.add((0, 0))

        for i, j, d in queue:
            if i == n - 1 and j == n - 1:
                return d

            directions = [(i - 1, j), (i, j - 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i, j + 1),
                          (i - 1, j + 1), (i - 1, j - 1)]

            for x, y in directions:
                if (0 <= x < n and 0 <= y < n) and ((x, y) not in seen and grid[x][y] == 0):
                    seen.add((x, y))
                    queue.append((x, y, d + 1))

        return -1
