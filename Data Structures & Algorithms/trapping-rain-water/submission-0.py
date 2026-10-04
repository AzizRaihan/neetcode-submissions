class Solution:
    def trap(self, height: List[int]) -> int:
        pre,suf=[0],[0]
        pmax=0
        smax=0
        for i in range(1,len(height)):
            if(height[i-1]>pmax):
                pmax=height[i-1]
                pre.append(pmax)
            else:
                pre.append(pmax)
        c=1
        for i in range(len(height)-2,-1,-1):
            if (height[i+1]>smax):
                smax=height[i+1]
                suf.append(smax)
            else:
                suf.append(smax)
        suf=suf[::-1]
        output=0
        for i in range(len(pre)):
            a=pre[i]
            b=suf[i]
            h=height[i]
            x=min(a,b)-h
            if (x>0):
                output+=x
        return output


       
        



        