# **Grid System - Story 1**

This project defines a 10x10 grid where each cell corresponds to a unique coordinate (from `n1` to `n100`). The grid is printed to the terminal using Python’s `f-strings`, and the coordinates are organized into a matrix. This matrix is then converted into a more digestible array format for easier manipulation.

---

## **Overview**

The grid is generated and printed using Python’s `print` function and `f-strings`, with each coordinate (`n1`, `n2`, ..., `n100`) displayed in a 10x10 grid format. The grid's coordinates are initially stored in a matrix (a list of lists), and then they are integrated into an array format for easier processing and access.

---

## **How It Works**

1. **Grid Definition:**
   - A **10x10 matrix** is created, where each element corresponds to a coordinate from `n1` to `n100`.
   - The matrix structure allows easy access to specific coordinates, which can be referenced as `n1`, `n2`, etc.

2. **Formatted Printing:**
   - The grid is printed to the terminal using `f-strings`, ensuring the coordinates are clearly displayed with proper formatting.

3. **Array Representation:**
   - The matrix is converted into a **1D array** (a list) of coordinates, making it easier to process and access.

---

## **Code Example**

Here’s a Python script that generates the grid and prints it to the terminal:

```
# Function to generate and print the grid with coordinates
def print_grid():
    grid_size = 10  # Grid size: 10x10
    n = 1  # Starting point for coordinates (n1)
    
    # Create the grid as a matrix of coordinates
    grid = [[f"n{n + i + j * grid_size}" for i in range(grid_size)] for j in range(grid_size)]
    
    # Print the grid row by row
    for row in grid:
        print(" ".join(row))

# Call the function to display the grid
print_grid()
