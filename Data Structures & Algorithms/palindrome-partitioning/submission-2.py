# base case - when have all str chars in partitions
# i == works juat fine >= is extra defence practice
# write the sol in BFS codde the sol in DFS
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sub = [], []

        def ispalandrom(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(sub.copy())
                return
            
            for j in range(i, len(s)):
                if ispalandrom(i, j):
                    sub.append(s[i:j+1]) # [0..j]
                    dfs(j+1) # [j:...] 
                    sub.pop()
        
        dfs(0)
        return res