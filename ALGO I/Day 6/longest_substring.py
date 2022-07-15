class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if len(string) == 0:
            return 0

        start, end = 0, 0
        seen = {}
        max_so_far = 0

        for index, value in enumerate(string):
            if value in seen and seen[value]>=start:
                max_so_far = max(max_so_far, end - start + 1)
                start = seen[value] + 1
            seen[value] = index
            end = index
        max_so_far= max(max_so_far, end - start + 1)
        return max_so_far