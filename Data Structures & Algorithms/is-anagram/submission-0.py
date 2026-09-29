class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        st=sorted(t)
        ss=sorted(s)
        if ss==st:
            return True
        else:
            return False
            
    
     
        
            
        
        
        