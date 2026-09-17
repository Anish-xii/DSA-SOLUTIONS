# BFS: for each point of 'G' block increase all its surrounding "at once" by g_block_val+1 and ...
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row, col = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # all 'G' blocks has distence 0 and alredy visited
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c]) # the gates
                    visited.add((r,c))
        

        def add_valid(r, c):
            if r<0 or c<0 or r>=row or c>=col or ((r,c) in visited) or grid[r][c] == -1:
                return
            q.append([r,c])
            visited.add((r,c))


        distance = 0 # distance at 'G' block
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                
                # add next set of valid surrounding blocks to q
                add_valid(r+1, c)
                add_valid(r-1, c)
                add_valid(r, c+1)
                add_valid(r, c-1)
            
            distance += 1 # value next set of blocks will have
