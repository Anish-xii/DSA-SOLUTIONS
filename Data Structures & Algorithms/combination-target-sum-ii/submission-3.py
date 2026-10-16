class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        res = []
        sub = []

        n = len(candidates)

        def dfs(i, s):
            # 4 when hit target / invalid or unnesesury
            if s == target:
                res.append(sub.copy())
                return
            if i == n or s > target: return
            
            # 1 chose each num one times, with updated sum
            sub.append(candidates[i])
            dfs(i+1, s+candidates[i])

            # 2 no duplicate
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1

            # 3 backtrack (recursive, so no need to s-nums[i])
            sub.pop()
            dfs(i+1, s)
        
        dfs(0, 0)
        return res