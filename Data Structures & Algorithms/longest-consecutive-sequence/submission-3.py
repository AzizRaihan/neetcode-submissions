class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        max=0
        
        
        for i in hs:
            
            n=i
            c=0
            
            if (i-1 not in hs):
                while(n in hs):
                    c+=1
                    n+=1
            if (c>max):
                max=c


           
        return max
            

            

            
            
        