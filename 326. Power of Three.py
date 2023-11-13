class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if  n==1 : return 1
        ans = 1
        i=1
        while i<n:
           ans = ans*3
           if ans==n :
               return 1 
           if ans > n : break  
           i=i+1  
        return 0       
