class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])

        def dfs(r, c, i):
            # when found all cahr
            if i == len(word): 
                return True
            
            # when char is not valid/useable
            if r<0 or c<0 or r>=row or c>=col or word[i]!=board[r][c] or board[r][c] == '#':
                return False
            
            # when char is considarable
            char = board[r][c]
            board[r][c] = '#'
            check = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)

            # check other paths (backtrack)
            board[r][c] = char
            
            return check


        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True

        return False