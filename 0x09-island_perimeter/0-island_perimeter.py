#!/usr/bin/python3

def island_perimeter(grid):
    """
    @grid grid with 0's and 1's
    @return int perimeter
    """
    n = 0
    for r in range(len(grid)):
        if r == 0 or r == len(grid) - 1:
            continue
        for c in range(len(grid[0])):
            if c == 0 or c == len(grid[0]) - 1:
                continue
            if grid[r][c] == 1:
                n += 4 - grid[r+1][c] - grid[r-1][c] - \
                    grid[r][c-1] - grid[r][c+1]

    return n
