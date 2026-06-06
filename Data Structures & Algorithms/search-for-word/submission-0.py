class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        # i -> word[i]
        def dfs_backtrack(r, c, i):

            # base-case
            if i == len(word): return True

            # cancel cases
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i] or board[r][c] == '#': return False

            # recursion - as we found a char
            board[r][c] = '#'
            res = dfs_backtrack(r+1, c, i+1) or dfs_backtrack(r-1, c, i+1) or dfs_backtrack(r, c+1, i+1) or dfs_backtrack(r, c-1, i+1)

            # backtrack - no path lead to full res / check other combo
            board[r][c] = word[i]
            return res

        
        for r in range(rows):
            for c in range(cols):
                if dfs_backtrack(r, c, 0):
                    return True

        return False 