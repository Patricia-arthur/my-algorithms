"""
This function finds the smallest missing positive integer
from an unsorted list of integers.

The algorithm runs in O(n) time and uses constant extra space
by modifying the input list in place.

Input:
    nums : list of int
        An unsorted list of integers.

Output:
    int
        The smallest missing positive integer.
"""

def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    for i in range(n):
        x = abs(nums[i])
        if 1 <= x <= n:
            nums[x - 1] = -abs(nums[x - 1])

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1
