class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # if all the array has uniq 1-9
        for r in board:
            seen = set()
            for n in r:
                if n in seen: return False
                if n != '.':
                    seen.add(n)

        # if all the vertical [i] has uniq 1-9
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen: return False
                if board[j][i] != '.':
                    seen.add(board[j][i])

        # dose all the 9 boxes have uniq 1-9
        start_pos = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i, j in start_pos:
            seen = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if board[r][c] in seen: return False
                    if board[r][c] != '.':
                        seen.add(board[r][c])
        
        return True
