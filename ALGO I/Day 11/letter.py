class Solution:
    def letterCasePermutationHelper(self, s: str, i: int, n: int, resultArr: List[str], res: str) -> None:
        #Base Case
        if i == n:
            resultArr.append(res)
            return
            
        asciiVal = ord(s[i])
        
        if 65 <= asciiVal <= 90:
            # Add/Subtract by 32 for converting because difference of ascii value of a and A is 32
            self.letterCasePermutationHelper(s, i+1, n, resultArr, res + chr(asciiVal + 32))
            self.letterCasePermutationHelper(s, i+1, n, resultArr, res+s[i])
        elif 97 <= asciiVal <= 122:
            self.letterCasePermutationHelper(s, i+1, n, resultArr, res + chr(asciiVal - 32))
            self.letterCasePermutationHelper(s, i+1, n, resultArr, res+s[i])
        else:
            self.letterCasePermutationHelper(s, i+1, n, resultArr, res+s[i])
    
    def letterCasePermutation(self, s: str) -> List[str]:
        resultArr = list()
        n = len(s)
        
        self.letterCasePermutationHelper(s, 0, n, resultArr, '')
        
        return resultArr