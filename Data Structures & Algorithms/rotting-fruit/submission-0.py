class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_q = deque()

        # track how many good and bad orng we have
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1: 
                    fresh_oranges += 1
                elif grid[r][c] == 2: 
                    rotten_q.append((r, c))
        
        if fresh_oranges == 0: return 0


        time = -1 # as the time starts after the first pic
        bfs_pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        while rotten_q:
            time += 1

            # for every bad orange 
            for _ in range(len(rotten_q)):
                r, c = rotten_q.popleft()

                # check their surrounding
                for pr, pc in bfs_pos:
                    x, y = r+pr, c+pc

                    # if connected valid good oranges
                    if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_oranges -= 1
                        rotten_q.append((x, y))

        return time if fresh_oranges == 0 else -1   