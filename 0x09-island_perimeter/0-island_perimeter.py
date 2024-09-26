#!/usr/bin/python3


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid
    """
    # Check if the grid is empty or if contains an empty row
    if not grid or not grid[0]:
        return 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check the left neighbour
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                # Check the top neighbour
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
