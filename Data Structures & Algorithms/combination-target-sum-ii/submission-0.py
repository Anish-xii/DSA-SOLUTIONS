class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        res, sub = [], []
        candidates.sort()

        def dfs_backtrack(i, s):
            # base case for recrtion
            if s == target:
                res.append(sub.copy())
                return
            if s > target or i == n: return    

            # 1. pic the num -> go next
            sub.append(candidates[i])
            dfs_backtrack(i+1, s+candidates[i])

            # 2. dont-pic/clear -> go next while its not same as last
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            sub.pop()
            dfs_backtrack(i+1, s)

        dfs_backtrack(0, 0)
        return res