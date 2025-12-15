import numpy as np
"""
This program computes the maximum sum of any contiguous subarray
within a given one-dimensional NumPy array of integers.

Input:
    P : numpy.ndarray
        A one-dimensional array of integers.

Output:
    Prints the largest possible sum of any contiguous subarray in P.
"""

P = np.array([-4,-3,-2,-1,0,1,2,3,4,5,6])
current_sum = P[0]
largest_sum = P[0]

for i in range(1,len(P)):
    current_sum = max(P[i], current_sum + P[i])
    largest_sum = max(largest_sum,current_sum)
print(largest_sum)
    
