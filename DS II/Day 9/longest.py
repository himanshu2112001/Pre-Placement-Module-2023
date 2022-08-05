class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
            
        def getPalindrome(s,s1,s2):
            while s1>=0 and s2<len(s) and s[s1]==s[s2]:
                s1 -= 1
                s2 += 1
            return s[s1+1:s2]
        maxPalind = ''
        s1=0
        s2=0
        while True:
            temp = getPalindrome(s,s1,s2)
            if len(temp) > len(maxPalind):
                maxPalind = temp
            s2+=1
            if (len(s)-s2)<=(len(maxPalind)/2):
                break
            temp = getPalindrome(s,s1,s2)
            if len(temp) > len(maxPalind):
                maxPalind = temp
            s1+=1
        return maxPalind
