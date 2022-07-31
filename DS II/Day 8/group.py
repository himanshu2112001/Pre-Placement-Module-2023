class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	
        di = Counter()
        mapp = defaultdict(list)
		
        for word in strs:
            curr = ''.join(sorted(word))
            di[curr]+=1
            mapp[curr].append(word)
			
        res = []
        for k,v in di.items():
            res.append(mapp[k])

        return res