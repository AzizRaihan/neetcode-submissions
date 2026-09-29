class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        res=[]
        for i in range(len(nums)):
            cn=nums[i]
            diff=target-cn
            if (diff in hm):
                res.append(hm[diff])
                res.append(i)
           
            else:
                hm[cn]=i
        return res
        
            

        
        

        

            
        
            

                
                
       

        
        