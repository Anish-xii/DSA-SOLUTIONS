# by picking or not picking when we reach the end
# only then we add subset to res

# we chose - we let the num be chosen again - then chose diffrent num insted
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sub = [], []
        n = len(candidates)

        def dfs(i, s):
            if s == target:
                res.append(sub.copy())
                return
            if i == n or s > target:
                return
            # chose a path
            sub.append(candidates[i])
            # chose again !
            dfs(i, s+candidates[i])
            # un chose
            sub.pop()
            # next path chose insted
            dfs(i+1, s)
        

        dfs(0, 0) #(index, sum)
        return res

"""Unlike subsets, here I need combinations that sum to a target, and — critically — the same number can be reused unlimited times. So instead of a strict yes/no decision per element, at each step I'm asking: 'do I use candidates[i] again, or am I done with it and move to the next candidate?'""This is the same include/exclude backtracking skeleton as subsets, but the 'include' branch recurses on the same index instead of the next one — that single change is what allows unlimited reuse of each candidate, while the 'exclude' branch still permanently advances past it."""