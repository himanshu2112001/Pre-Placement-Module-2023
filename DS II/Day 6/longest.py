class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        max_len = 0
        
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
            max_len += 1
    
        odd_count = 0
        for char in char_count:
            if char_count[char] % 2 != 0:
                max_len -= 1
                odd_count += 1
                
        if odd_count:
            max_len += 1
            
        return max_len