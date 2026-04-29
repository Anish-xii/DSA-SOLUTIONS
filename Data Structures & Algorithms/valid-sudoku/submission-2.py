class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validate rows
        for row in range(9):
            s = set()
            for j in range(9):
                if board[row][j] in s:
                    return False
                if board[row][j] != '.':
                    s.add(board[row][j])  

        # validate columns
        for i in range(9):
            s = set()
            for col in range(9):
                if board[col][i] in s:
                    return False
                if board[col][i] != '.':
                    s.add(board[col][i])

        # validate 3X3 boxes
        box_starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i, j in box_starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in s:
                        return False
                    if board[row][col] != '.':
                        s.add(board[row][col])

        return True                
                    