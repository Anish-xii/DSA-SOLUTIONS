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


""" The duplicate-skip trick: "The tricky part is avoiding duplicate combinations in the output, not duplicate values within one combination — those are different things. [1,1,6] is valid because it uses two separate 1-elements. What I need to prevent is generating [1,2,5] twice just because there happen to be two 1s in the array. So specifically in the skip branch — right after deciding 'I'm not using this value at this position' — I skip over any immediately following duplicates of that same value too. That's because trying 'skip the first 1, then separately consider the second 1' would just rediscover the exact same combinations through a different path."""