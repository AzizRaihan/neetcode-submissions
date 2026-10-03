class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res2=[]
        
        for i in range(len(nums)):
            l=0
            r=len(nums)-1
           
            while (l<r):
                res1=[]

                

                if(l==i):
                    l+=1
                elif (r==i):
                    r-=1
                else:

                    
                    if(-nums[i]==(nums[l]+nums[r])):
                        res1.append(nums[i])
                        res1.append(nums[l])
                        res1.append(nums[r])
                        l+=1
                        r-=1
                        res1.sort()
                        if (res1 not in res2 and res1!=[]):
                            res2.append(res1)
                            res1=[]
                    elif(-nums[i]>(nums[l]+nums[r])):
                        l+=1
                    elif(-nums[i]<(nums[l]+nums[r])):

                        r-=1
            
            
        return res2


        
        
        
        