"""
This function finds the smallest substring of s that contains
all characters of t, including duplicates.

If no such substring exists, it returns an empty string.
"""

def minWindow(s, t):
    if not s or not t:
        return ""

    result = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            if contains_all(substring, t):
                if result == "" or len(substring) < len(result):
                    result = substring

    return result


def contains_all(substring, t):
    for char in t:
        if substring.count(char) < t.count(char):
            return False
    return True



s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
