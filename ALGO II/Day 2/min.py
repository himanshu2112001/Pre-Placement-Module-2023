class Solution:
    def findMin(self, nums: List[int]) -> int:
        res,left,right = 0,0,len(nums)-1
        
        while(left <= right):
            mid = (left + right) >> 1
            if nums[mid] <= nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1