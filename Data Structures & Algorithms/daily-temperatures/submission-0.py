class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stk = [] # monotonic decrising (t,i)

        for i, n in enumerate(temperatures):
            
            while stk and stk[-1][0] < n:
                stk_n, stk_i = stk.pop()
                res[stk_i] = i - stk_i

            stk.append((n, i))

        return res  