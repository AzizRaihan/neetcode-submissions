class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        start=0
        for i in range(1,len(nums)):
            if(nums[start]==nums[i]):
                return True
            else:
                start=i
        return False


            
                    
                
            