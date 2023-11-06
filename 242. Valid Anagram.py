class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(s)==sorted(t):
            return 1
        else :
            return 0    
