"""
This function generates all possible palindrome partitions of a given string.

The string is partitioned such that every substring in each partition
is a palindrome. The function explores all possible ways to cut the string
using a backtracking approach and collects every valid partition.

Input:
    s : str
        A string consisting of lowercase English letters.

Output:
    Returns a list of lists, where each inner list represents a valid
    palindrome partition of the input string.
"""

def palindromePartition(s):
    results = []
    current = []

    def helper(start):
        if start == len(s):
            results.append(current.copy())
            return

        for i in range(start + 1, len(s) + 1):
            piece = s[start:i]

            if piece == piece[::-1]:
                current.append(piece)
                helper(i)
                current.pop()

    helper(0)
    return results

# Example
s = "aab"
print(palindromePartition(s))

s="mnpoo"
print(palindromePartition(s))