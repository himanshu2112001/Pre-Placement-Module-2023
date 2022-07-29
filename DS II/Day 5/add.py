class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1=len(num1)
        n2=len(num2)
        carry=0
        ans=''
        for i in range(max(n1,n2)):
            ch1=ord(num1[n1-i-1])-ord('0') if n1>i else 0
            ch2=ord(num2[n2-i-1])-ord('0') if n2>i else 0
            carry,cur=divmod(ch1+ch2+carry,10)
            ans=chr(ord('0')+cur)+ans
        if carry: ans ='1'+ans
        return ans