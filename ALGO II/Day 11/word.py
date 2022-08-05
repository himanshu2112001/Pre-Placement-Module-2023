class Solution:
    def exist(self, B: List[List[str]], W: str) -> bool:
    	M, N, L, S = len(B), len(B[0]), len(W)-1, sum(B,[])
    	if any(S.count(i) < W.count(i) for i in set(W)): return False
    	def dfs(i,j,c):
    		if B[i][j] != W[c]: return False
    		if c == L: return True
    		B[i][j] = 0
    		for k,l in (i-1,j),(i,j+1),(i+1,j),(i,j-1):
    			if 0 <= k < M and 0 <= l < N and B[k][l] and dfs(k,l,c+1): return True
	    	B[i][j] = W[c]
	    	return False
    	for i,j in itertools.product(range(M),range(N)):
    		if dfs(i,j,0): return True
    	return False
