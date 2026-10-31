class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        h1=Counter(s1)
        h2={}
        r=len(s1)
        l=0
        
        if (len(s1)>len(s2)):
            return False
        else:
            for i in range(len(s1)):
                h2[s2[i]]=h2.get(s2[i],0)+1
            if h2==h1:
                return True
            while (r<=len(s2)-1):
                if h2==h1:
                    return True
                else:
                    
                    h2[s2[l]]-=1
                    if h2[s2[l]]==0:
                        del h2[s2[l]]

                    h2[s2[r]]= h2.get(s2[r],0)+1
                    l+=1
                    r+=1
                    if h2==h1:
                        return True
                    
        return False


              




