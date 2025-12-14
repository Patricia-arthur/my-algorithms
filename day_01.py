import numpy as np
"""
This program finds the indices of two distinct elements in a NumPy array
whose sum is equal to a given target value.

The algorithm scans the array once while storing previously seen elements
and their indices in a dictionary. For each element, it computes the
complement needed to reach the target. If the complement has already been
encountered, the indices of the two elements are printed and the search
terminates.

Input:
    A : numpy.ndarray
        A one-dimensional array of integers.
    T : int
        The target sum.

Output:
    Prints a tuple of two indices (i, j) such that A[i] + A[j] = T.
"""

A = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
T = 7
D = {}

for i in range(len(A)):
    x = A[i]
    y = T - x

    if y in D:
        print(D[y], i)
        break
    else:
        D[x] = i