class MinStack:

    def __init__(self):
        self.stack=[]
        self.ms=[]
       


        

    def push(self, val: int) -> None:
        if (self.stack==[] and self.ms==[]):
            self.stack.append(val)
            self.ms.append(val)
        else:

            self.stack.append(val)
            x=self.ms[-1]
            m=min(val,x)
            self.ms.append(m)





        

    def pop(self) -> None:
        self.stack.pop()
        self.ms.pop()
        

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
