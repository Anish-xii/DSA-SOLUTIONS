class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == '': return []
        res, sol = [], []
        
        p_book = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(i):
            # base case - when we got a combo with all digits
            if i >= len(digits):
                res.append(''.join(sol))
                return
            
            for c in p_book[digits[i]]:
                sol.append(c)
                backtrack(i+1)
                sol.pop()


        backtrack(0) # digits[0]
        return res