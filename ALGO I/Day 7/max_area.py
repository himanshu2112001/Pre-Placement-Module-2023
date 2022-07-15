class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        
        def dfs(r, c):
            if grid[r][c] != 1:                                     # 0 indicate no island, 2 indicate the island has been seen.
                return 0
            
            area = 1
            grid[r][c] = 2                                          # Change the num of current island, indicating it has been seen.
            for d in directs:
                if m > r + d[0] >= 0 and n > c + d[1] >= 0:
                    area += dfs(r + d[0], c + d[1])
            
            return area
        
        
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        
        return res