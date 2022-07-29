class Solution:
    def countLetters(self, s: str) -> dict:
        counts = {}
        for char in s:
            try:
                counts[char] += 1
            except KeyError:
                counts[char] = 1
        return counts
    
    def isAnagram(self, sCounts: str, tCounts: str) -> bool:
        for char in sCounts:
            currentCount = sCounts[char]
            try:
                if tCounts[char] != currentCount:
                    return False
            except KeyError:
                if currentCount != 0:
                    return False
        return True