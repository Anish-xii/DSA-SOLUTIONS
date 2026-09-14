# pic a number (for loop track what point) - backtrack 
# - next pic a diffrent num - backtrack - pop go back - pic num not in sol - backtrack

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []
        l = len(nums)

        def dfs():
            if len(sol) == l:
                res.append(sol.copy())
                return
            
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    dfs()
                    sol.pop()


        dfs()
        return res

# Every element must appear — so need to check completion (all elements used)
# No element can repeat — so at each position, need to know what's already used
# pic/pop and run over the arr again to chose a path thats stuck in a prev recursion