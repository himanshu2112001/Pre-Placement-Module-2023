class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(n):
            if n == 0:
                return 1
            return n*fact(n-1)
        
        def ncr(n,r):
            return (fact(n)/(fact(n-r)*fact(r)))
        
        c = m+n-2
        return int(ncr(c,m-1))
