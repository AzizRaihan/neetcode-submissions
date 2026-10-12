class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[]
        for i in matrix:
            pair=(min(i),max(i))
            res.append(pair)
            ind=0
            c=-1
        for a,b in res:
            c+=1
            if (target>=a and target<=b):
                ind=c
                l=0
                r=len(matrix[ind])-1
                while(l<=r):
                    m=(l+r)//2
                    if (matrix[ind][m]==target):
                        return True
                    elif (matrix[ind][m]>target):
                        r=m-1
                    elif (matrix[ind][m]<target):
                        l=m+1
            
        return False
        

   
                                                                
        
        