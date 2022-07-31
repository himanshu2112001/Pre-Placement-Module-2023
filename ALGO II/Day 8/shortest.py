from collections import deque
class Solution:
    def isSafe(self,i,j, grid):
        n = len(grid)
        return 0 <= i < n and 0 <= j < n
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        source = [0,0]
        destination = [n-1, n-1]
        
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if grid[0][0] == 0 and n == 1:
            return 1
        
        visited = [[False]*n for i in range(n)]
        queue = deque([[source, 1]])
        visited[0][0] = True
        
        while queue:
            coordinates, shortestPath = queue.popleft()
            
            x = coordinates[0]
            y = coordinates[1]
            
            neighbours = [[-1,0], [1,0], [0,-1], [0,1], [1,1], [1,-1], [-1,1], [-1,-1]]
            
            for neighbour in neighbours:
                xNew = x + neighbour[0]
                yNew = y + neighbour[1]
                
                if self.isSafe(xNew, yNew, grid) and grid[xNew][yNew] == 0 and visited[xNew][yNew] == False:
                    queue.append([[xNew, yNew], shortestPath + 1])
                    visited[xNew][yNew] = True
                
                if [xNew, yNew] == destination:
                    return shortestPath + 1
        return -1