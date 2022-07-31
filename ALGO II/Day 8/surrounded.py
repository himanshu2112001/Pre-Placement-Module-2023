class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def capture(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != "O":
                return
            
            board[row][col] = "T"
            
            for curr_dir in directions:
                capture(row + curr_dir[0], col + curr_dir[1])
                
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [COLS - 1, 0]):
                    capture(row, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"