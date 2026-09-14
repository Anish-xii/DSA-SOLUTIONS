class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sub = [], []
        n = len(candidates)
        candidates.sort()

        def dfs(i, s):
            if s == target:
                res.append(sub.copy())
                return
            if i == n or s > target: return
            
            # 1.chose a path
            sub.append(candidates[i])
            # 2.chose the next path
            dfs(i+1, s+candidates[i])

            # not chose a duplicate num in sorted arr
            while i+1 < n and candidates[i] == candidates[i+1]: i += 1

            # un chose apth 1
            sub.pop()
            # chose path 2 only insted
            dfs(i+1, s)
        

        dfs(0, 0)
        return res