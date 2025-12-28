"""
This program generates all possible subsets (the power set) of a list
of unique integers and returns them in a list.

Input:
    numbers : tuple or list of int
        A collection of unique integer elements.

Output:
    Returns a list of all possible subsets (including the empty set)
    where each subset is represented as a list.
"""

def powerSet(numbers):
     subsets = [[]]
     
     for num in numbers:
         new_subsets = []
         
         for subset in subsets:
             new_subsets.append(subset + [num])
         subsets.extend(new_subsets)
         
     return subsets    
         
         
#Example
numbers = 1,2,3,4
print(powerSet(numbers))
