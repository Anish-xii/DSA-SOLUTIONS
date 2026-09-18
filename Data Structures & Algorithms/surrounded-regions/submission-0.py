# any box toching the walls can never be surrounded, 
#so find them and their connections, and flip all others

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        
        row, col = len(board), len(board[0])

        def dismiss(r, c):
            if r<0 or c<0 or r>=row or c>=col or board[r][c] != 'O':
                return
            board[r][c] = '#'
            dismiss(r+1, c)
            dismiss(r-1, c)
            dismiss(r, c-1)
            dismiss(r, c+1)


        # 1. find all boxes toeching walls
        for r in range(row):
            for c in range(col):
                # dismiss all 'O' and their 4-direction connected 'O'
                if r in [0, row-1] or c in [0, col-1]:
                    if board[r][c] == 'O':
                        dismiss(r,c)
        
        # 2. 'X' all remaining 'O' boxes
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O': board[r][c] = 'X'
        
        # 3. 'O' back all the valid boxes
        for r in range(row):
            for c in range(col):
                if board[r][c] == '#': board[r][c] = 'O'

                