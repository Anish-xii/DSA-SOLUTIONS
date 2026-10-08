class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        for r in range(9):
            seen = set()
            for b in range(9):
                if board[r][b] in seen: return False
                if board[r][b] != '.':
                    seen.add(board[r][b])
        
        for c in range(9):
            seen = set()
            for b in range(9):
                if board[b][c] in seen: return False
                if board[b][c] != '.':
                    seen.add(board[b][c])
        
        box_starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i, j in box_starts:
            seen = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if board[r][c] in seen: return False
                    if board[r][c] != '.':
                        seen.add(board[r][c])
        
        return True