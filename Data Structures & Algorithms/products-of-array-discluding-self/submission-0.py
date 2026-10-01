class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf,res=[],[],[]
        for i in range(len(nums)):
            if i==0:
                pre.append(1)
            else:
                x=pre[i-1]*nums[i-1]
                pre.append(x)
        c=0
        for i in range(len(nums)-1,-1,-1):
            if (i==len(nums)-1):
                suf.append(1)
                
                
            else:
                c+=1
                y=suf[c-1]*nums[i+1]
                suf.append(y)
        suf.reverse()
        for i in range(len(pre)):
            ans=pre[i]*suf[i]
            res.append(ans)
        return res



        