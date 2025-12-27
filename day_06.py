"""
This function merges all overlapping intervals in a list of intervals
and returns a list of non-overlapping intervals that cover the same range.

Input:
    inter : list of list of int
        A list of intervals, where each interval is represented as
        [start, end].

Output:
    Returns a list of merged non-overlapping intervals.
"""

def interval(inter):
    inter.sort()
    merged = []
    merged.append(inter[0])
    
    for i in inter[1:]:
        last_end = merged[-1][-1]
        
        if i[0] <= last_end:
            merged[-1][-1] = max(last_end, i[1])
        else:
            merged.append(i)
    return merged        
       
 #Example      
inter = [[1,3], [2,6], [8,10], [9,12], [15,18], [19,25]]
print(interval(inter))