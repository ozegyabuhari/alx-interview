#!/usr/bin/python3
"""a function def island_perimeter(grid):
that returns the perimeter of the island
"""


def island_perimeter(grid):
    if not grid:
        return 0

    index = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                index += 4
                if i > 0 and grid[i - 1][j] == 1:
                    index -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    index -= 2

    return index
