class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num, maxRow, maxCol = 0, len(grid), len(grid[0])

        def island(x, y):
            if x < 0 or x >= maxRow or y < 0 or y >= maxCol or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            for newx,newy in [[1,0], [-1,0], [0,1], [0,-1]]:
                island(x+newx, y+newy) 

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == "1":
                    num += 1
                    island(row, col)
        return num