class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            if target<=matrix[i][n-1]:
                try:
                    matrix[i].index(target)
                    return True
                except:
                    return False