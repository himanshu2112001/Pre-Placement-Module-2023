class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0]*26
        
        for letter in list(ransomNote):
            letters[ord(letter)-ord('a')] += 1
            
        for letter in list(magazine):
            if letters[ord(letter)-ord('a')] > 0:
                letters[ord(letter)-ord('a')] -= 1
            
        check = [0]*26
        
        return check == letters