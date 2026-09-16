class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        max_count = 0

        
        def dfs(r, c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] != 1:
                return 0
            grid[r][c] = '#'

            count = 1
            for rv, cv in [[1,0],[0,1],[-1,0],[0,-1]]:
                count += dfs(r+rv, c+cv)

            return count


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    new_count = dfs(r, c)
                    max_count = max(max_count, new_count)
        
        return max_count