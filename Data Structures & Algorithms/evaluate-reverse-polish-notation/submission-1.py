class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        oprnd = '+-/*'

        for c in tokens:
            if c in oprnd:

                b, a = stk.pop(), stk.pop()
                if c == '+':
                    stk.append(a+b)
                elif c == '-':
                    stk.append(a-b)
                elif c == '*':
                    stk.append(a*b)
                else:
                    stk.append(int(a/b))            

            else:
                stk.append(int(c))  
        
        return stk.pop()                
