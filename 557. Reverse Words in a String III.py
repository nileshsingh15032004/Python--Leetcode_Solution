class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
     
        reversed_words = []
        
    
        for word in words:
            reversed_word = ''.join(reversed(word))
            reversed_words.append(reversed_word)
            
        result = ' '.join(reversed_words)
        
        return result
