class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # similar to the longest increasing subsequence 
        if len(set(nums)) <3:
            return False
        dp = [1]*len(nums)
        flag = False
        for i in range(1,len(dp)):
            pre_max = 0
            for j in range(0, i):
                if nums[j]<nums[i]:
                    pre_max = max(pre_max,dp[j])
            dp[i]+=pre_max
            if dp[i] == 3:
                return True
        return False
        print(dp)