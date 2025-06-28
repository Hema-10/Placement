def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        block = set()
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in row: return False
            row.add(board[i][j])
            if board[j][i] != '.' and board[j][i] in col: return False
            col.add(board[j][i])
            r, c = 3*(i//3)+j//3, 3*(i%3)+j%3
            if board[r][c] != '.' and board[r][c] in block: return False
            block.add(board[r][c])
    return True
