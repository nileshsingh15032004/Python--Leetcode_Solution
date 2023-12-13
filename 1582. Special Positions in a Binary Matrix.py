def column(matrix, i):
        return [row[i] for row in matrix]
class Solution:
    
    def numSpecial(self, mat: List[List[int]]) -> int:
        c=0
        for i in range(len(mat)):
            if(mat[i].count(1)==1):
                i=mat[i].index(1)
                col=column(mat,i)
                if(col.count(1)==1):
                    c+=1
        
        return c        
                
        
                
