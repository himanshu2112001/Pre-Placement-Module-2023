class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def robFrom(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            ans = max(robFrom(i+1), robFrom(i+2) + nums[i])
            cache[i] = ans
            return ans
        return robFrom(0)
