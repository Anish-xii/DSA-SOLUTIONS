class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1: return False
        
        st = {'(', '{', '['}
        d = {')':'(', '}':'{',']':'['}
        stk = []

        for c in s:
            if c in st: stk.append(c)
            if c not in st:
                if stk and stk[-1] == d[c]: stk.pop()
                else: return False

        return True if not stk else False        




# if emty or len = 1 return false
# set = {all open br}
# stk[]
# dict = {map close - open}
# when encounter a cl-brkt, the stk.top should be open of that kind
# for c in s, if c == some c/S - stk.push, if stk.top == c/E - stk.pop
# if len(stk) == 0 return true else false