class Solution:
    

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            num=len(i)
            res+=str(num)+"#"+i
        return res
        
        

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while (i<len(s)):
            j=i
            while (s[j]!="#"):
                j+=1

            num=int(s[i:j])
            chunk=s[j+1:j+num+1]
            res.append(chunk)
            i=j+num+1
        return res

            