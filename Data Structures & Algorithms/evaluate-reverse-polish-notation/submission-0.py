class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        st = {'*','-','+','/'}
        d = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

        for c in tokens:

            if c not in st: 
                stk.append(int(c))
            else:
                x = stk.pop()
                y = stk.pop()

                res = d[c](int(y), int(x))
                stk.append(res)
        
        return stk[0]        
