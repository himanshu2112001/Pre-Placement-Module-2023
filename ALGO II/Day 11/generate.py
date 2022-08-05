from itertools import product

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def verifyCandinate(s: str, n: int) -> bool:
            left, right = 0, 0
            for ch in s:
                if ch == '(':
                    left += 1
                if ch == ')':
                    right += 1
                if left < right:
                    return False
            return left == n and right == n

        candinate = [''.join(x) for x in product('()', repeat=2*n)]
        result = [s for s in candinate if verifyCandinate(s, n)]
        return result
