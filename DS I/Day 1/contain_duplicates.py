class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        s=set(nums)
        print(s)
        print(nums)
        if len(s)==len(nums):
            return False
        else:
            return True