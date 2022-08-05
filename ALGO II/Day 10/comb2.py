class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(i, curr, total):
                
            if i >= len(candidates) or total > target:
                return 
            
            # Two Options:
            
            # With candidates[i]:
            
            curr.append(candidates[i])
            
            if total + candidates[i] == target:
                result.append(curr[::])
                
            dfs(i+1, curr, total+candidates[i])
            
            # Without candidates[i]:
            
            curr.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
                
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        
        return result
