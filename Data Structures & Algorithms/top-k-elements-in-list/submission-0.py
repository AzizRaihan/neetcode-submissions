class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        from collections import Counter
        count=Counter(nums)
        sd=dict(sorted(count.items(), key=lambda item:item[1],reverse=True))
        count=0
        
        for key,val in sd.items():
            if count>=k:
                break
            ans.append(key)
            count+=1
        return ans
            

            
            
            
        
        

        