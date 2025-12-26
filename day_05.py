import numpy as np
"""
This program finds all quadruplets of distinct elements in a list of integers
whose sum is equal to a given target value.

The algorithm works by first sorting the list, then fixing two elements using
nested loops. For the remaining two elements, a two-pointer technique is used
to efficiently search for combinations that satisfy the target sum.

Input:
    nums : list
        A list of integers.
    target : int
        The target sum for the quadruplets.

Output:
    Returns a list of lists, where each inner list contains four integers
    whose sum is equal to the target value.
"""

def quaSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i+1,n):
            third_num = j+1
            fourth_num = n-1
            while third_num < fourth_num:
                sum = nums[i] + nums[j] + nums[third_num] + nums[fourth_num]
                if sum == target:
                    result.append([nums[i], nums[j], nums[third_num], nums[fourth_num]])
                    third_num += 1
                    fourth_num -= 1
            
                elif  sum < target:
                    third_num += 1
                
                else:
                    fourth_num -= 1
    return result

# test example
nums = [2,3,5,4,7,5,6,9,0]
target = 15
print(quaSum(nums, target))