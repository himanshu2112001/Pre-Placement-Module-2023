class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache1, cache2 = dict(), dict()
        def robHouse(i, nums, zeroStart=True):
            if zeroStart:
                if i >= len(nums)-1:
                    return 0
                if i in cache1:
                    return cache1[i]
            else:
                if i >= len(nums):
                    return 0
                if i in cache2:
                    return cache2[i]
            
            res = max(nums[i]+robHouse(i+2, nums, zeroStart), robHouse(i+1, nums, zeroStart))
            if zeroStart:
                cache1[i] = res
            else:
                cache2[i] = res
            return res
        
        return max(robHouse(0, nums), robHouse(1, nums, False))
