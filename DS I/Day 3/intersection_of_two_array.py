class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                a = nums2.index(nums1[i])
                nums1[i],nums2[a] = 1001,1002
        return ans