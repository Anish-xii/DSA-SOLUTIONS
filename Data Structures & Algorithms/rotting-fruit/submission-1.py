# BFS: all conected eliment change values at once for the next iteration
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        self.fresh_org = 0 
        bad_org = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1: self.fresh_org += 1
                elif grid[r][c] == 2:
                    bad_org.append([r,c])
        if self.fresh_org == 0: return 0
        

        def make_bad(r, c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] != 1:
                return
            grid[r][c] = 2
            self.fresh_org -= 1
            bad_org.append([r,c])


        time = -1 # time starts when loop starts
        
        while bad_org:
            time += 1

            # make all conected "ORG" bad at-once BFS
            for _ in range(len(bad_org)):
                r, c = bad_org.popleft()
                
                make_bad(r+1, c)
                make_bad(r-1, c)
                make_bad(r, c-1)
                make_bad(r, c+1)


        return time if self.fresh_org == 0 else -1

  