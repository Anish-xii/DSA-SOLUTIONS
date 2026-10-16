class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []
        sub = []

        n = len(candidates)

        def dfs(i, s):
            # 3 when hit target / invalid or unnesesury
            if s == target:
                res.append(sub.copy())
                return
            if i == n or s > target: return
            
            # 1 chose num multiple times, with updated sum
            sub.append(candidates[i])
            dfs(i, s+candidates[i])

            # 2 backtrack (recursive, so no need to s-nums[i])
            sub.pop()
            dfs(i+1, s)
        
        dfs(0, 0)
        return res