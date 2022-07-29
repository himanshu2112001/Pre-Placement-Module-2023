class Solution:
    def maxArea(self, height: List[int]) -> int:
        rightindex=len(height)-1
        leftindex=0
        maxres=0
        while(rightindex== leftindex or rightindex>leftindex):
            print(str(leftindex)+" "+str(rightindex))
            maxres=max((abs(leftindex-rightindex))*min(height[leftindex],height[rightindex]),maxres)
            if(height[leftindex]>=height[rightindex] ):
                rightindex-=1
            else:
                leftindex+=1
        return maxres