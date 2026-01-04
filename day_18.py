"""
This function checks whether a 9x9 Sudoku board is valid.

A Sudoku board is valid if:
- No row contains duplicate digits (1-9)
- No column contains duplicate digits (1-9)
- No 3x3 sub-box contains duplicate digits (1-9)

Empty cells represented by '.' are ignored.
"""

def isValidSudoku(board):

    # Check each row
    for row in board:
        seen = set()
        for cell in row:
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    # Check each column
    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    # Check each 3×3 sub-box
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    cell = board[box_row + i][box_col + j]
                    if cell != ".":
                        if cell in seen:
                            return False
                        seen.add(cell)

    return True
