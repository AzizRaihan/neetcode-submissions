class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=0
        hm=set()
        while (r<=len(s)-1):
            
                
            
            if(s[r] in hm):
                while (s[r] in hm):
                    hm.remove(s[l])
                    l+=1
                    res1=r-l+1
                    res=max(res,res1)
            else:
                hm.add(s[r])
                res=max(res,(r-l+1))
                r+=1
                    
        return res


        