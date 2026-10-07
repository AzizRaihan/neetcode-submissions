class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in range(len(tokens)):
            if (tokens[i]!="/" and tokens[i]!="*" and tokens[i]!="-" and tokens[i]!="+"):
                stack.append(int(tokens[i]))
            
            elif (tokens[i]=="+"):
                res=0
                a=stack[-1]
                stack.pop()
                b=stack[-1]
                stack.pop()
                res=b+a
                stack.append(res)
            elif (tokens[i]=="-"):
                res=0
                c=stack[-1]
                stack.pop()
                d=stack[-1]
                stack.pop()
                res=d-c
                stack.append(res)
            elif (tokens[i]=="*"):

                res=0
                e=int(stack[-1])
                stack.pop()
                f=int(stack[-1])
                stack.pop()
                res=f*e
                stack.append(res)
            else:

                res=0    
                g=stack[-1]

                stack.pop()
                h=stack[-1]
                stack.pop()
                res=int(h/g)
                stack.append(res)

           
        return int(stack[-1])





        