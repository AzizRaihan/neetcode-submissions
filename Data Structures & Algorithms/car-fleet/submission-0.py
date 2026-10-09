class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=sorted(zip(position,speed), reverse=True)
        stack=[]
        position,speed=zip(*pair)
        for i in range (len(position)):
            t=(target-position[i])/speed[i]
            if (stack==[]):
                stack.append(t)
            else:
                if (t>stack[-1]):
                    stack.append(t)
        return len(stack)
                
                


       