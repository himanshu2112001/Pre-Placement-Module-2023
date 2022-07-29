class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]: #If currently in decreasing order of the list
                end = mid
            else: #If in increasing order of the list, start after mid element
                start = mid + 1
        return start