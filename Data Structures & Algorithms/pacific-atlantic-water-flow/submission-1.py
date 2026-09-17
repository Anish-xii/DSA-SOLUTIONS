from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        row, col = len(heights), len(heights[0])

        # check "bigger" values from eack block in que-recurse
        def bfs(blocks):
            visited = set(blocks)
            q = deque(blocks)
            while q:
                i, j = q.popleft()
                for iv, jv in [(1,0), (0,1), (-1,0), (0,-1)]:
                    r, c = i+iv, j+jv
                    # add them if they are valid (in-bound & bigger)
                    if 0<=r<row and 0<=c<col and (r,c) not in visited and heights[r][c] >= heights[i][j]:
                        visited.add((r,c))
                        q.append((r,c))
            return visited


        pacific_blk = []
        atlantic_blk = []

        # add vertical blocks
        for c in range(col):
            pacific_blk.append((0, c))
            atlantic_blk.append((row-1, c))
        
        # add horizontal blocks
        for r in range(row):
            pacific_blk.append((r, 0))
            atlantic_blk.append((r, col-1))
        
        # get set of all posible connected blocks
        pacific = bfs(pacific_blk) 
        atlantic = bfs(atlantic_blk)

        return list(pacific & atlantic)  

