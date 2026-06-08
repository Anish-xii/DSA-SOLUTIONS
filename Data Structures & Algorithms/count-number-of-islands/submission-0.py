class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, col = len(grid), len(grid[0])
        sides = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        island = 0

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=col or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            # trivers all sides
            for dr, dc in sides:
                dfs(r+dr, c+dc)    


        # for all '1's add all conected -> 1 island
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    island += 1

        return island 