class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import math
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        while (l <= r):
            m = math.floor((l + r) / 2)
            if (nums[m] == target):
                return m
            elif (nums[m] > target):
                r = m-1
            elif (nums[m] < target):
                l = m+1
           

           
        return -1
                           
                                     

        