class Solution:
    def addDigits(self, num: int) -> int:
         ans = 0
         while( num > 0 ):
           ans = ans+(num%10)
           num = num//10

         if ans>=10: 
           return self.addDigits(ans)   
         return ans   
