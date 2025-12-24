from collections import Counter
"""
This program groups identical colors in a list so that all occurrences
of the same color appear adjacent to each other.

Input:
    colors : list
        A list containing color names, where elements may be repeated.

Output:
    Prints a list of colors arranged such that identical colors are
    placed next to one another.
"""

colors =["red", "yellow","black","red","green", "black","yellow","red","black","green", "black","green", "yellow"]
count_colors = Counter(colors)
sorted_colors = []
for color in count_colors:
    sorted_colors.extend([color]*count_colors[color])
print(sorted_colors)