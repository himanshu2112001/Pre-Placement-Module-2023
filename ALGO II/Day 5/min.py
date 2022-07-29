class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start,sum_val =0,0
        min_cnt=float('inf')
        for end in range(len(nums)):
            sum_val+=nums[end]
            while sum_val>=s:
                min_cnt=min(min_cnt, end-start+1)
                sum_val-=nums[start]
                start+=1
        return min_cnt if min_cnt!=float('inf') else 0