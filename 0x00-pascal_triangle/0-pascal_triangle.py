#!/usr/bin/python3
"""
    Creating a function that returns list of lists of integers representing the pascal triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    # we initialize the triangle with the first row
    triangle = [[1]]

    # wwe build the rest of the rectangle
    for i in range(1, n):
        row = triangle[-1]
        new_row = [1]

        for k in range(1, i):
            new_row.append(row[k-1] + row[k])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
