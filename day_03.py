import numpy as np
"""
This program computes the maximum sum obtained by adding any two
distinct elements from a one-dimensional NumPy array of integers.


Input:
    A : numpy.ndarray
        A one-dimensional array of integers.

Output:
    Prints the maximum sum of any two distinct elements in A.
"""

A = np.array([-12,-8,-4,0,4,8,12,16,20,24,28])
results= []

for i in range(len(A)):
    for j in range(i+1,len(A)):
        results.append(A[i] + A[j])
print(max(results))