class Solution:
    def reverseWords(self, s: str) -> str:

        words = list(s.split(" ")) 
        word_results = [] 
        
        for word in words:
            reverse_word = ""
            for letter in reversed(word):
                reverse_word += letter
            word_results.append(reverse_word)
        
        results = " ".join(word_results)                 
        return results