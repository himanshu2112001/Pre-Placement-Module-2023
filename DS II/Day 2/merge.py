class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 173 ms, faster than 76.99% of Python3 online submissions for Merge Intervals.
        Memory Usage: 18.1 MB, less than 84.50% of Python3 online submissions for Merge Intervals.
        """
        # if only 1 interval in list, return
        if len(intervals) == 1:
            return intervals
        
        # sort the list of intervals so that:
        # [[1,4],[0,4]] becomes [[0, 4], [1, 4]]
        intervals = sorted(intervals)
        
        i = 0
        while True:
            
            # take interval i and interval i+1
            # itv_0[0] <= itv_f[0] because we sorted
            itv_0 = intervals[i]  
            itv_f = intervals[i+1]
            
            # if last of itv_0 >= first value of itv_f -> merge them
            # the merge will be [itv_0[0], max(itv_0[-1], itv_1[-1])] 
            # because we don't know which value is higher
            if itv_0[1] >= itv_f[0]:
                intervals[i] = [itv_0[0], max(itv_0[-1], itv_f[-1])]
                intervals.pop(i+1)
                
                # we start from same list index (new merged interval)
                i -= 1
                if i < 0:
                    i = 0
            else:
                # otherwise we proceed to next interval in list
                i += 1
            
            # and we're done once we've exhausted the list
            if i >= len(intervals) - 1:
                break
        
        return intervals