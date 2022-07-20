class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(ind, dp):
            if ind<=0:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            first = helper(ind-1, dp)
            second=0
            if ind>1:
                second=helper(ind-2, dp)
            dp[ind]=first + second
            return dp[ind]
        dp=[-1]*(n+1)
        return helper(n, dp)
