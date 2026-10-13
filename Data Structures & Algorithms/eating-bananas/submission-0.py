class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], target: int) -> int:
        piles=sorted(piles)
        t=sum(piles)
        l=1
        up=max(piles)
        r=up
        low=0
        
        while (l<=r):
            mid=(l+r)//2
            rate=mid
            h=0
            for i in range(len(piles)):
                h+=math.ceil(piles[i]/rate)
               
            if (h<=target):
                
                low=rate
                r=mid-1

                
            elif (h>target):
                l=mid+1
           
        return low




                

                
