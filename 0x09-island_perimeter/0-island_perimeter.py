#!/usr/bin/python3
"""This calculates the perimeter of the island in the grid"""


def island_perimeter(grid):
    """
    @grid grid with 0's and 1's
    @return int perimeter
    """
    n = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                n += 4 - grid[r+1][c] - grid[r-1][c] - \
                    grid[r][c-1] - grid[r][c+1]

    return n
