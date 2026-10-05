class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
   

        for i in range(len(s)):
            x=s[i]
            if (x=='[' or x=='{' or x=='('):

                stack.append(x)
            elif(x==']'):
                if (stack==[]):
                    return False

                elif(stack[-1]!='['):
                    return False
                

                else:

                    stack.pop()
            elif(x=='}'):
                if (stack==[]):
                    return False

                elif(stack[-1]!='{'):
                    return False
                
                else:
                    stack.pop()
            elif(x==')'):
                if (stack==[]):
                    return False

                elif(stack[-1]!='('):
                    return False
                
                else:
                    stack.pop()
        if (stack==[]):
            return True
        else:
            return False
            
        

         
     
             



            
                

        
        
        

            

            
    
    

        