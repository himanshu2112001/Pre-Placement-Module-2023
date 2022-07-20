class Solution:
    def isValid(self, s: str) -> bool:
        dic, stack = {')': '(', ']': '[', '}': '{'}, []       # dic: store each closing with its respective opening, stack: stack to add the openings.
        for i in s:                                           # traverse each paranthesis
            if stack and dic.get(i) == stack[-1]: stack.pop() # whenever any closing comes, we check we have its opening in top of our stack or not. 
            else: stack.append(i)                             # else we add that in stack 
        return not stack
