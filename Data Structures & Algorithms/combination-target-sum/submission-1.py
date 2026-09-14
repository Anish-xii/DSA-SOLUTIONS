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