"""
This program checks whether one string contains a permutation of another string.

Given two strings s1 and s2, the program determines whether any permutation 
of s1 appears as a contiguous substring within s2.

Input:
    s1 : str
        A string whose permutations are to be checked.
    s2 : str
        A string in which permutations of s1 are searched for.

Output:
    Returns True if s2 contains any permutation of s1 as a substring.
    Returns False otherwise.
"""

from collections import Counter

def checkInclusion(s1, s2):
    len_s1 = len(s1)
    count_s1 = Counter(s1)

    for i in range(len(s2) - len_s1 + 1):
        substring = s2[i:i + len_s1]
        if Counter(substring) == count_s1:
            return True

    return False

#Example
s1 = "bobo"
s2 = "aboloboob"
print(checkInclusion(s1, s2))
