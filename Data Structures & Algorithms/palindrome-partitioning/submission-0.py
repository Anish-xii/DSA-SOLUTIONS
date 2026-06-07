class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs_backtrack(i):
            # base case - when have all str chars in partitions
            if i >= len(s):
                res.append(part.copy())
                return

            # check every parititions starting from each char
            for j in range(i, len(s)):
                # if this part is pal - add it
                if self.isPal(s, i, j):
                    part.append(s[i:j+1])
                    dfs_backtrack(j+1)
                    part.pop()         

        dfs_backtrack(0) # s[0] start
        return res

    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True 