class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rm,sl,l,r,m,rep=0,0,0,0,0,0
        hm={}
        while (r<=len(s)-1):
            sl=r-l+1
            if s[r] in hm:
                hm[s[r]]+=1
            else:
                hm[s[r]]=1
            x=max(hm.values())
            rep=sl-x
            if (rep>k):
                while (rep>k):
                    
                    hm[s[l]]-=1
                    l+=1
                    sl=r-l+1
                    x=max(hm.values())
                    rep=sl-x
                  
            
               
                
            rm=max(rm,sl)
            r+=1
        return rm




            
            
            







        