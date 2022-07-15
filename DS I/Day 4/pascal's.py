class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        ans = [[1], [1,1]]
        for n in range(2, numRows):
            ans.append([1])
            for i in range(len(ans[-2]) - 1):
                ans[-1].append(ans[-2][i] + ans[-2][i+1])
            ans[-1].append(1)
            
        return ans