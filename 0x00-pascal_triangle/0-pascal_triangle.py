#!/usr/bin/python3

def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []
    
    triangle = []

    for i in range(n):
        # Start each row with a 1
        row = [1] * (i + 1)
        # Calculate the values for the internal elements (if any)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Add the completed row to the triangle
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    """Print the row"""
    for row in triangle:
        print("[{}]".format("\n".join([str(x) for x in row])))

# Testing the function
if __name__ == "__main__":
    print(pascal_triangle(5))
