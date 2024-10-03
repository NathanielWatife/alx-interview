#!/usr/bin/python3
def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = []  # Initialize the list to hold all rows of the triangle
    
    for i in range(n):
        # Start each row with a 1
        row = [1] * (i + 1)  # Each row has (i + 1) elements
        
        # Calculate the values for the internal elements (if any)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        # Add the completed row to the triangle
        triangle.append(row)
    
    return triangle

# Testing the function
if __name__ == "__main__":
    print(pascal_triangle(5))
