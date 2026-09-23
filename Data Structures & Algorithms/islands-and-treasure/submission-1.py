class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row, col = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))
        
        
        def add_nei(r, c):
            if r<0 or c<0 or r>=row or c>=col or ((r,c) in visited) or grid[r][c] == -1:
                return
            q.append([r, c])
            visited.add((r, c))

            
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                add_nei(r+1, c)
                add_nei(r-1, c)
                add_nei(r, c+1)
                add_nei(r, c-1)
            
            distance += 1