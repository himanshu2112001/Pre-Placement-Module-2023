class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        else:
            temp = []
            for i in range(len(nums)):
                if nums[i] == target:
                    temp.append(i)
            result = []
            result.append(temp[0])
            result.append(temp[-1])
            return result