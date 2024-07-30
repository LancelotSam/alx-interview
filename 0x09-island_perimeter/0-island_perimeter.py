#!/usr/bin/python3
"""
A module: defines a function that calculates
the perimeter of an island on a given grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of any notable island in the given grid
    """
    length = len(grid)
    width = len(grid[0])
    perimeter = 0
    for x in range(length):
        for y in range(width):
            if grid[x][y] == 1:
                perimeter += 4
                # checking adjacent cells
                if (y < width - 1 and grid[x][y + 1] == 1):
                    perimeter -= 2
                if (x < length - 1 and grid[x + 1][y] == 1):
                    perimeter -= 2
    return perimeter
