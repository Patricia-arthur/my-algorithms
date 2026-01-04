"""
This function returns all elements of a matrix in spiral order.

The spiral order is obtained by repeatedly:
- taking the top row
- taking the right column
- taking the bottom row in reverse
- taking the left column from bottom to top
"""

def spiralOrder(matrix):
    result = []

    while matrix:
        result += matrix.pop(0)

        for row in matrix:
            result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        for row in reversed(matrix):
            result.append(row.pop(0))

    return result
