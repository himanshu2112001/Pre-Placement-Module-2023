class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str((sum(int(num1[i])*(10**(len(num1)-i-1)) for i in range(len(num1))))*(sum(int(num2[i])*(10**(len(num2)-i-1)) for i in range(len(num2)))))