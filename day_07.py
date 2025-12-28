"""
This function removes the minimum number of parentheses from a string
so that the resulting string has valid parentheses.

Input:
    s : str
        A string containing '(', ')', and lowercase English letters.

Output:
    Returns a string with valid parentheses after removing the
    minimum number of invalid parentheses.
"""

def validString(s):
    results =[]
    count_p = 0
    
    for p in s:
        if p == '(':
            results.append(p)
            count_p +=1
        elif p ==')':
            if count_p > 0:
                results.append(p)
                count_p -= 1
        else:
            results.append(p)
    
    final_results = []
    for p in reversed(results):
        if p == '(' and count_p > 0:
            count_p -=1
        else:
            final_results.append(p)
    return ''.join(reversed(final_results))

#Example
s = "a)b(c)d"
print(validString(s))   
    