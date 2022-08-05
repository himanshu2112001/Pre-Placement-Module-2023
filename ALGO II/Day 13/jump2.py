class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        n = len(nums)
        dp = [n]*(n)
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, i+1+nums[i]):
                if j <= n-1:
                    dp[i] = min(dp[i], dp[j]+1)
                    
        return dp[0]
