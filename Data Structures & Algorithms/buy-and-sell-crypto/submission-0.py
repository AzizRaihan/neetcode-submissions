class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        l=0
        r=len(prices)-1
        while (l<=r):
            if (l==r):
                l+=1
                r=len(prices)-1
            else:
                p=prices[r]-prices[l]
                m=max(m,p)
                r-=1
        return m



        