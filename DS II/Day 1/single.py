class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final_list = []
        for n in nums:
            if n in final_list:
                final_list.remove(n)
            
            else:
                final_list.append(n)
        return final_list[0]