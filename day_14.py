"""
This function generates all combinations of well-formed parentheses
for a given number of pairs.

Input:
    n : int
        Number of pairs of parentheses.

Output:
    Returns a list of strings representing all valid combinations
    of well-formed parentheses.
"""

def generateParenthesis(n):
    result = []

    def build(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            build(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            build(current + ")", open_count, close_count + 1)

    build("", 0, 0)
    return result
