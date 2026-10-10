class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=0
        for i in range(len(heights)):
            if (stack==[]):
                stack.append(i)
            else:
                t=stack[-1]
                if(heights[i]>=heights[t]):
                    stack.append(i)
                elif (heights[i]<heights[t]):
                    
                    while(stack and heights[i]<heights[(stack[-1])]):
                        idx=stack.pop()
                        
                        
                        if (stack==[]):
                            l=-1
                            r=i
                            a=(r-l-1)*heights[idx]
                            area=max(a,area)
                        else:
                            l=stack[-1]
                            r=i
                            a=(r-l-1)*heights[idx]
                            area=max(a,area)
                    stack.append(i)
        while (stack):
            i=stack.pop()
            l=stack[-1] if stack else -1
            r=len(heights)
            a=(r-l-1)*heights[i]
            area=max(a,area)
        


            

        return area






        