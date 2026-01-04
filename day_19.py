"""
This function checks if a given word exists in a 2D grid of characters.

The word can be formed by sequentially adjacent letters (up, down,
left, right). Each cell may be used only once.
"""

def exist(board, word):

    rows = len(board)
    cols = len(board[0])

    def search(r, c, index):
        if index == len(word):
            return True

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (
            search(r + 1, c, index + 1) or
            search(r - 1, c, index + 1) or
            search(r, c + 1, index + 1) or
            search(r, c - 1, index + 1)
        )

        board[r][c] = temp

        return found

    for r in range(rows):
        for c in range(cols):
            if search(r, c, 0):
                return True

    return False
