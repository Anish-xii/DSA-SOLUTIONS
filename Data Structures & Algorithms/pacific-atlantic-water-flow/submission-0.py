from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])

        p_que, a_que = deque(), deque()
        p_set, a_set = set(), set()

        # Add all pecific blocks

        ## top blocks:-
        for j in range(n): 
            p_que.append((0,j))
            p_set.add((0,j))
        ## side blocks:-
        for i in range(1,m):
            p_que.append((i,0))
            p_set.add((i,0))


        # Add all atlantic blocks

        # bottom blocks:-
        for j in range(n):
            a_que.append((m-1,j))
            a_set.add((m-1,j))
        # side blocks:-
        for i in range(m-1):
            a_que.append((i,n-1))
            a_set.add((i,n-1))


        def bfs(que, sett): 
            blocks = set() # all unique blocks
            while que:
                i, j = que.popleft()
                blocks.add((i,j))
                # check 4 sides
                for i_off, j_off in [(1,0), (0,1), (-1,0), (0,-1)]:
                    r, c = i+i_off, j+j_off
                    # if the block is valid | bigger= | not-visited
                    # as we have all the sides in store, only blocks bigger than it
                    # can push water to ocian 
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in sett:
                        sett.add((r,c))
                        que.append((r,c))
            
            return blocks            


        p_blocks = bfs(p_que, p_set)
        a_blocks = bfs(a_que, a_set)

        return list(p_blocks.intersection(a_blocks))    