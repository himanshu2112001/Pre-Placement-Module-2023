class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target < row[0] or target > row[-1]:
                continue
            if row[bisect_left(row, target)] == target:
                return True
        return False

