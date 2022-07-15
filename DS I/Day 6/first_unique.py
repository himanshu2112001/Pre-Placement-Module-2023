class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in dict.fromkeys(s):
            if s.count(i)==1:
                return s.index(i)
        else:
            return -1