class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
                    return [0, 1]

        for i in range(len(nums)):
            first_number = nums[i]
            number_to_find = target - first_number
            
            for j in range(i + 1, len(nums)):
                second_number = nums[j]
                if second_number == number_to_find:
                    return [i, j]