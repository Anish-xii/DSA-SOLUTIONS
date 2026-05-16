class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1: return False
        
        d = {')':'(', '}':'{',']':'['}
        stk = []

        for c in s:
            if c not in d: stk.append(c)
            if c in d:
                if stk and stk[-1] == d[c]: stk.pop()
                else: return False

        return True if not stk else False        

