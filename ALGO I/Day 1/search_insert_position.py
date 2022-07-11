class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lowBound = 0
        highBound = len(nums)
        
        while lowBound < highBound :
            mid = (highBound + lowBound)//2
            if nums[mid] < target :
                lowBound = mid + 1
            else :
                highBound = mid
        return lowBound