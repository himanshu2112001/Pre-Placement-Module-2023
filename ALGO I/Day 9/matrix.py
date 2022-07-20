class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visit = set()
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visit.add((i, j))
                    q.append((i, j, mat[i][j]))
        
        while q:
            num = len(q)
            for i in range(num):
                x, y, val = q.pop(0)
                if x > 0 and (x-1, y) not in visit:
                    visit.add((x-1, y))
                    mat[x-1][y] = val+1
                    q.append((x-1, y, mat[x-1][y]))
                if y > 0 and (x, y-1) not in visit:
                    visit.add((x, y-1))
                    mat[x][y-1] = val+1
                    q.append((x, y-1, mat[x][y-1]))
                if x < m-1 and (x+1, y) not in visit:
                    visit.add((x+1, y))
                    mat[x+1][y] = val+1
                    q.append((x+1, y, mat[x+1][y]))
                if y < n-1 and (x, y+1) not in visit:
                    visit.add((x, y+1))
                    mat[x][y+1] = val+1
                    q.append((x, y+1, mat[x][y+1]))
        
        return mat