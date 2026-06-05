class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        res, sub = [], []

        def dfs_backtrack(i, s):
            # base case for recrtion
            if s == target:
                res.append(sub.copy())
                return
            if s > target or i == n: return    

            # 1. pic the num -> go next
            sub.append(candidates[i])
            dfs_backtrack(i, s+candidates[i])

            # 2. dont-pic/clear -> go next
            sub.pop()
            dfs_backtrack(i+1, s)

        dfs_backtrack(0, 0)
        return res 