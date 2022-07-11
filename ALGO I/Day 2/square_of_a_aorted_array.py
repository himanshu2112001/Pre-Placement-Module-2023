class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l = 0
        r = len(nums) - 1
        
        result = [None for i in range(len(nums))]
        
        
        for i in reversed(range(len(nums))):
            
            if abs(nums[r]) > abs(nums[l]):
                result[i] = nums[r]**2
                r -= 1
            
            else: 
                result[i] = nums[l]**2
                l += 1
                
        return result