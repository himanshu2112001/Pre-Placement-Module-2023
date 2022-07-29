class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort() 
        n = len(arr) 
        result = set()
        for i in range(n-2):
          j,k = i+1,n-1 
          
          while j<k:
            a,b,c = arr[i] , arr[j] ,arr[k] 
            if (a)+(b)+(c)==0:
              k-=1 
              j+=1 
              ans = (a,b,c) 
              
              result.add(ans) 
                
            elif (a)+(b)+(c)>0:
              k-=1 
            else:
              j+=1 
            
        return result