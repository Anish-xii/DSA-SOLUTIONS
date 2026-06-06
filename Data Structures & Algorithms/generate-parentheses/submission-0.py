class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, stk = [], []

        def backtrack(opn_c, cls_c):
            if opn_c == cls_c == n:
                res.append(''.join(stk))
                return

            # when to add opn
            if opn_c < n:
                stk.append('(')
                backtrack(opn_c+1, cls_c)
                stk.pop()

            # when to add cls
            if opn_c > cls_c:
                stk.append(')')
                backtrack(opn_c, cls_c+1)
                stk.pop()

        backtrack(0, 0)
        return res