class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l=0
        r=len(numbers)-1
        res=[]
        while (l<r):
            x=numbers[l]+numbers[r]
            if (x==target):
            

                res.append(l+1)
                res.append(r+1)
                return res
            elif (x<target):
                l+=1
            elif (x>target):
                r-=1



        