class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        stack=[0]
        
        for i in range(len(temperatures)):
            res.append(0)
        for i in range(len(temperatures)):

            if( stack==[]):
                stack.append(i)
            elif (temperatures[(stack[-1])]<temperatures[i] ):
                while (stack and temperatures[(stack[-1])]<temperatures[i] ):

                    res[(stack[-1])]=i-stack[-1]
                    stack.pop()
                stack.append(i)
                  
            else:
                stack.append(i)
        return res
        
        
        



        